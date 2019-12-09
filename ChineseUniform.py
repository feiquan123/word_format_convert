"""
中文字符处理的工具:
    繁体转简体
    简体转拼音
"""

from langConvert.ft2jt import getFt2JtMap
from langConvert.ft2jt import ft2jt_dfa
from hz2py import hanzi2pinyin


def ChineseUniform(msg):
    ''' 繁体转简体 '''
    return ft2jt_dfa.filter(msg, replace_map=getFt2JtMap(), replace_char=None)[0]


def Chinese2Pinyin(msg):
    '''简体转拼音'''
    return hanzi2pinyin(msg)


if __name__ == '__main__':
    msg = "修鬍刀儘快 年后 參與感 嘉伟"
    zh = ChineseUniform(msg)
    pinyin = Chinese2Pinyin(zh)
    print(pinyin)
    print(zh)
