'''
字符处理的工具:
    将各种可见字符去除,包含空格,换行等
'''

from symbol_black import symbol_black_set
import re


def SymbolUniform(msg, exclude=False):
    '''将在字符黑名单中的字符去除或者替换'''
    msg = msg.replace("＋", "+")
    mean_str = ["+"]  # 有意义的字符不能直接去除
    for w in msg:
        if w in symbol_black_set:
            if exclude and w in mean_str:
                # 如果 exlude 为 Ture，并且包含有意义字符直接跳过不处理
                continue
            msg = msg.replace(w, '')
    msg = re.sub(r'\s{2,}', '', msg.strip())

    return msg


if __name__ == '__main__':
    msg = "逆市大幅 ҉ 手动阀手动阀 Ψ +vx"
    print(SymbolUniform(msg))
    print(SymbolUniform(msg, True))
