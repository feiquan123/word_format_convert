'''
特殊清洗规则：
OtherUniform 负责统一清洗后的特殊清洗
    1.url ->H
    2.q -> 扣
    3.+ -> 加
    4.w,v -> 微
    5.x -> 信
    6.b -> 博
'''
import re


def url2H(src):
    """对url地址做标注替换 H"""
    src = src.lower()
    return re.sub(r'(http://www\.|https://|www\.)[a-z0-9./?&_-]*', 'H', src)  # 网址


def puls2加(src):
    '''将 + 替换为 加'''
    return src.replace("+", "加").replace("⊕", "加")


def v2微(src):
    '''将 v 替换为 微'''
    return re.sub("[vVWw]{1,}", "微",src)


def x2信(src):
    '''将 x 替换为 信'''
    return re.sub("[xX]{1,}","信",src)

def q2扣(src):
    """qq替换为kou kou"""
    src = src.replace('q M', 'qq M').replace('qi e M', 'qq M').replace('kou kou', 'qq').replace('kou M', 'qq M')
    src = re.sub(r'q{3,} M', 'qq M', src)
    # qq换成kou kou
    src = src.replace('q','扣')
    return src

def b2博(src):
    '''将 b 替换为 博'''
    return src.replace("b", "博").replace('B', "博")

def replace加微信(src):
    ''' 替换 +vx 为 加微信  '''
    src = puls2加(src)
    src = v2微(src)
    src = x2信(src)
    return src

def replace加qq(src):
    ''' 替换 +qq -> 加kou kou '''
    src = puls2加(src)
    src = q2扣(src)
    return src

def replace加微博(src):
    ''' 替换 +wb -> 加微博 '''
    src = puls2加(src)
    src = v2微(src)
    src = b2博(src)
    return src

def OtherUniform(src):
    '''替换 url->H | q->扣 |  +wx ->加微信 | +wb ->加微博  '''
    src = url2H(src)
    src = replace加qq(src)
    src = replace加微信(src)
    src = replace加微博(src)
    return src

if __name__ == '__main__':
    t = "+qq +q    +wx   +vb"
    print(replace加qq(t))
    print(replace加微信(t))
    print(replace加微博(t))

    print(OtherUniform(t))
