from langConvert.ft2jt_dic import zh2TW, zh2Hant, zh2CN, zh2SG, zh2Hans, zh2HK
from langConvert.DFA import DFA

'''
zh2Hant: 简体 -> 繁体
zh2TW： 简体 -> 台湾繁体
zh2HK： 简体 -> 香港繁体

zh2Hans: 繁体 -> 简体
zh2CN： 国内繁体 -> 简体
zh2SG： 新加坡繁体 -> 简体
'''


def changeMapKeyValue(map):
    re = {}
    for k, v in map.items():
        re[v] = k
    return re


# 获取 繁体=> 简体映射表
def getFt2JtMap():
    zh2hant = changeMapKeyValue(zh2Hant)
    zh2tw = changeMapKeyValue(zh2TW)
    zh2hk = changeMapKeyValue(zh2HK)

    new = zh2hant
    new.update(zh2tw)
    new.update(zh2hk)
    new.update(zh2Hans)
    new.update(zh2CN)
    new.update(zh2SG)

    return new


# 繁体2简体的替换算法
ft2jt_dfa = DFA(words=getFt2JtMap().keys())

if __name__ == '__main__':
    for k, v in getFt2JtMap().items():
        print(k, v)
