# Liber

劇本語言Liber使用的解析器。

它主要被用在[Librian - 簡明強大的Galgame引擎](https://github.com/RimoChan/Librian)。

## 文檔

拿Librian的中文文檔[https://doc.librian.net](https://doc.librian.net/site/主頁.html)湊合一下吧！

## 使用方法

需要Python3.6以上。

```sh
pip install liber
```

```python
import liber
s = '''
> BG 中庭
潘大爺 「你好啊！」
'''
print(liber.load(s))
```

輸出: 

```python
[
    {'縮進數': 0, '原文': 'BG 中庭', '函數': 'BG', '參數表': [{'a': '中庭'}], '類型': '函數調用'}, 
    {'縮進數': 0, '名': '潘大爺', '代': None, '特效': None, '顏': None, '語': '你好啊！', '類型': '人物對話'}
]
```
