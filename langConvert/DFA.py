'''
根据敏感词数组创建一个树，使用字典结构存储
'''


# 节点
class Node:
    def __init__(self, end=False):
        self.children = None
        self.isEnd = end

    def setIsEnd(self):
        self.isEnd = True


# word and message must encode utf-8
# Deterministic Finite Automaton （确定有穷自动机）  还有  Nondeterministic Finite Automaton,NFA（不确定的有穷自动机）
class DFA:
    # 根据敏感词数组构造树
    def __init__(self, words):
        '''
        :param words:  敏感词列表
        '''
        self.root = Node()
        for w in words:
            self.addWord(w)

    # 添加单个敏感词
    def addWord(self, word):
        node = self.root
        iEnd = len(word) - 1
        for i in range(len(word)):
            char = word[i]
            # 没有节点
            if node.children == None:
                node.children = {}
                if i != iEnd:
                    node.children[char] = Node()
                else:
                    node.children[char] = Node(True)

            # 有节点，但是没有包含 word 中的字符
            elif char not in node.children:
                if i != iEnd:
                    node.children[char] = Node()
                else:
                    node.children[char] = Node(True)

            # 有节点，节点中以及包含了 word 的所有字符, 最后的节点为结束节点
            else:
                if i == iEnd:
                    node.children[char].setIsEnd()

            # 节点下移
            node = node.children[char]

    # 判断 msg 是否包含敏感词
    def isContain(self, msg):
        root = self.root
        msgLen = len(msg)
        for i in range(msgLen):
            p = root  # 当前节点
            j = i  # 结束位置
            while (j < msgLen and p.children != None and msg[j] in p.children):
                p = p.children[msg[j]]
                if p.isEnd:
                    return True
                j += 1
        return False

    # 过滤消息
    def filter(self, msg, replace_map={}, replace_char="*"):
        ''' 返回过滤后的消息和匹配到的消息 '''
        match_text =[] # 匹配到的消息
        if not replace_map and not replace_char:
            return msg,match_text

        newMsg = []
        root = self.root
        msgLen = len(msg)
        i = 0
        isContinue = False

        while i < msgLen:
            p = root
            j = i
            while (j < msgLen and p.children != None and msg[j] in p.children):
                p = p.children[msg[j]]
                # 检测到敏感词
                if p.isEnd:
                    match_text.append(msg[i:j + 1])
                    replace = self._replace(msg[i:j + 1], replace_map, replace_char)
                    newMsg.append(replace)
                    i = j + 1
                    isContinue = True
                    break
                j += 1

            # 在从 i 开始替换第一次的敏感词后，继续从 i 开始替换 msg 后续的其它敏感词 （msg 中存在多个敏感词）
            if isContinue:
                isContinue = False
                continue

            newMsg.append(msg[i])
            i = i + 1

        return ''.join(newMsg),match_text

    # 替换规则
    def _replace(self, sensitive_word, replace_map, replace_char="*"):
        # print(sensitive_word)
        # 优先根据字典替换
        if replace_map and sensitive_word in replace_map.keys():
            return replace_map.get(sensitive_word)

        # 如果  replace_char 存在，根据 replace_char 替换
        if replace_char:
            return replace_char * len(sensitive_word)  # 使用 * 替换敏感词

        # replace_char 为 None 不替换直接返回原词
        return sensitive_word  # 使用 * 替换敏感词


if __name__ == '__main__':
    words = ['你好', 'hello', 'name', "namb"]
    words_map = {"hello": "小狗", "namb": "朋友"}

    msg = "你好，hello。My name is 小红 namb"

    dfa = DFA(words)
    print(dfa.isContain(msg))
    # 根据 map 替换
    print(dfa.filter(msg, words_map, None))
    # 根据 replace 替换
    print(dfa.filter(msg, None, '^'))
    # 结合 map 和 replace 替换
    print(dfa.filter(msg, words_map, '^'))
    # 原文不动
    print(dfa.filter(msg, None, None))