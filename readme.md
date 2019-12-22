# word_format_convert
Chinese to Pinyin,symbol,number,char,string or word  uniform format  

1. ## NomalTextClearFlow

    1. `SymbolUniform` 删除特殊字符   
    2. `EnglishUniform` 统一格式化字符串，完成全角转半角，大写转小写
    3. `ChineseUniform` 繁体转简体 or `Chinese2Pinyin` 汉字转拼音
    4. `NumberUniform` 统一数字,去除空格

2. ## Notice 

    1. You can add your own process anywhere in the `NomalTextClearFlow`, then generate `CustomTextClearFlow`
    2. You can add any Symbol to `symbol_black.py`  for filter special symbol.

3. ## Example

    - Example1:
        ```python
        src = '美眉能污能yue。，让你yu罢不能。有性取向+V欣:fk5662'
        str=NomalTextClearResult(src)
        print(str)
        str = SpecialTextClearResult(src,True)
        print(str)
        pinyin = Chinese2Pinyin(str)
        print(pinyin)
        ```
    
        Result1:
        ```text
        美眉能污能yue让你yu罢不能有性取向v欣fk5662
        美眉能污能yue让你yu罢不能有性取向加微欣fk5662
        mei mei neng wu neng yue rang ni yu ba bu neng you xing qu xiang jia wei xin fk5662
        ```
    
    - Example2:
        ```python
        src = '微信零①③０③０③①②⑨'
        str = NomalTextClearResult(src)
        print(str)
        ```
    
        Result2:
        ```text
        微信0130303129
        ```
  
 1. ## ENV
    
    - python version
        > python 3
                       
    - how to install
        > python setup.py install
    