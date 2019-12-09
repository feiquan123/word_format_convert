'''
阿拉伯数字处理的工具:
    各种数字转阿拉伯数字
'''

import re


# 数字转换
def NumberUniform(src):
    """把各种类型数字转换为阿利伯字母"""
    src = src.replace('①', '1').replace('⑴', '1').replace('⒈', '1').replace('Ⅰ', '1').replace('一', '1').replace('1️⃣',
                                                                                                                '1').replace(
        '壹', '1').replace('Ⅰ', '1')
    src = src.replace('②', '2').replace('⑵', '2').replace('⒉', '2').replace('Ⅱ', '2').replace('二', '2').replace('2️⃣',
                                                                                                                '2').replace(
        '贰', '2').replace('Ⅱ', '2')
    src = src.replace('③', '3').replace('⑶', '3').replace('⒊', '3').replace('Ⅲ', '3').replace('三', '3').replace('3️⃣',
                                                                                                                '3').replace(
        '叁', '3').replace('Ⅲ','3')
    src = src.replace('④', '4').replace('⑷', '4').replace('⒋', '4').replace('Ⅳ', '4').replace('四', '4').replace('4️⃣',
                                                                                                                '4').replace(
        '肆', '4').replace('Ⅳ','4')
    src = src.replace('⑤', '5').replace('⑸', '5').replace('⒌', '5').replace('Ⅴ', '5').replace('五', '5').replace('5️⃣',
                                                                                                                '5').replace(
        '伍', '5').replace('Ⅴ','5')
    src = src.replace('⑥', '6').replace('⑹', '6').replace('⒍', '6').replace('Ⅵ', '6').replace('六', '6').replace('6️⃣',
                                                                                                                '6').replace(
        '陆', '6').replace('Ⅵ','6')
    src = src.replace('⑦', '7').replace('⑺', '7').replace('⒎', '7').replace('Ⅶ', '7').replace('七', '7').replace('7️⃣',
                                                                                                                '7').replace(
        '柒', '7').replace('Ⅶ','7')
    src = src.replace('⑧', '8').replace('⑻', '8').replace('⒏', '8').replace('Ⅷ', '8').replace('八', '8').replace('8️⃣',
                                                                                                                '8').replace(
        '捌', '8').replace('Ⅷ','8')
    src = src.replace('⑨', '9').replace('⑼', '9').replace('⒐', '9').replace('Ⅸ', '9').replace('九', '9').replace('9️⃣',
                                                                                                                '9').replace(
        '玖', '9').replace('Ⅸ','9')
    src = src.replace('零', '0').replace('0️⃣', '0').replace('〇', '0').replace('０', '0')
    src = src.replace('拾', '10').replace('十', '10').replace('Ⅹ','10')
    src = src.replace('佰', '00').replace('百', '00')
    src = src.replace('仟', '000').replace('千', '000')
    src = re.sub('\s+', "", src)
    return src


if __name__ == '__main__':
    msg = "⑴十四 灵拾0⑨ⅩⅢ"
    print(NumberUniform(msg))
