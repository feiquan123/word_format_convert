'''
统一的数据清洗, 数据清洗规则
    1.将汉字 繁体转简体
    2. 将英文 全角转半角，大写转小写
    3. 将各种 任何数字 转化为 阿拉伯数字
'''

from ChineseUniform import Chinese2Pinyin, ChineseUniform
from EnglishUniform import EnglishUniform
from NumberUniform import NumberUniform
from SymbolUniform import SymbolUniform
from OtherUniform import OtherUniform

def NomalTextClearResult(msg,exclude=False):
    ''' 对消息格式清洗:
            1. 删除特殊字符
            2. 统一格式化字符串，完成全角转半角，大写转小写
            3. 繁体转简体
            4. 统一数字,去除空格

    exclude : 是否排除有意义字符
    '''
    # 删除特殊字符
    msg = SymbolUniform(msg,exclude=exclude)
    # 统一格式化字符串，完成全角转半角，大写转小写
    msg = EnglishUniform(msg)
    # 繁体转简体
    msg = ChineseUniform(msg)
    # 统一数字
    msg = NumberUniform(msg)
    return msg

def SpecialTextClearResult(msg,exclude=False):
    # 正常清洗
    msg = NomalTextClearResult(msg,exclude)
    '''
    其它清洗规则
    OtherUniform 负责统一清洗后的特殊清洗
        1.url ->H
        2.q -> 扣
        3.+ -> 加
        4.w,v -> 微
        5.x -> 信
        6.b -> 博
    '''
    msg = OtherUniform(msg)
    return msg


if __name__ == '__main__':
    src = '美眉能污能yue。，让你yu罢不能。有性取向+V欣:fk5662'
    str=NomalTextClearResult(src)
    print(str)
    str = SpecialTextClearResult(src,True)
    print(str)
    pinyin = Chinese2Pinyin(str)
    print(pinyin)

    src = '微信零①③０③０③①②⑨'
    str = NomalTextClearResult(src)
    print(str)
