# Liber

劇本語言Liber使用的解析器。

它主要被用在[Librian - 簡明強大的Galgame引擎](https://github.com/RimoChan/Librian)。


## 文檔

<https://doc.librian.net/site/用戶指南/劇本寫法.html>。


## 使用方法

需要Python3.6以上，然後:

```sh
pip install liber
```

接口只有1個，就是`加載`，函數名也可以用英文寫作`load`，輸入1個字符串或者文件，將它解析爲劇本。

```python
def 加載(x: Union[str, TextIO]) -> List[Dict[str, Any]]:
    ...
```

舉個例子:

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
