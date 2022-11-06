# pypinyin-dict

使用 [pinyin-data](https://github.com/mozillazg/pinyin-data) 和 [phrase-pinyin-data](https://github.com/mozillazg/phrase-pinyin-data) 中的拼音数据文件覆盖 [pypinyin](https://github.com/mozillazg/python-pinyin) 中的内置拼音数据，
实现只使用某个或某些拼音数据文件中的拼音数据的需求。

## 安装

```
$ pip install pypinyin-dict
```

## 使用示例

```python
>>> from pypinyin import pinyin
>>> pinyin('枯萎')
[['kū'], ['wēi']]

# 使用 phrase-pinyin-data 项目中 cc_cedict.txt 文件中的拼音数据优化结果
>>> from pypinyin_dict.phrase_pinyin_data import cc_cedict
>>> cc_cedict.load()

>>> pinyin('枯萎')
[['kū'], ['wěi']]


>>> pinyin('扔', heteronym=True)
[['rēng', 'rèng']]

# 使用 pinyin-data 项目中 kXHC1983.txt 文件中的拼音数据优化结果
>>> from pypinyin_dict.pinyin_data import kxhc1983
>>> kxhc1983.load()

>>> pinyin('扔', heteronym=True)
[['rēng']]
```

## 模块介绍

各个模块与数据文件关系如下（所有模块中都有一个 ``load()`` 函数用于导入对应的拼音数据，使用方法详见上方【使用示例】）：

```python
# pinyin-data/kTGHZ2013.txt
>> from pypinyin_dict.pinyin_data import ktghz2013

# pinyin-data/kHanyuPinyin.txt
>> from pypinyin_dict.pinyin_data import khanyupinyin

# pinyin-data/kXHC1983.txt
>> from pypinyin_dict.pinyin_data import kxhc1983

# pinyin-data/kHanyuPinlu.txt
>> from pypinyin_dict.pinyin_data import khanyupinlu

# pinyin-data/kMandarin_8105.txt
>> from pypinyin_dict.pinyin_data import kmandarin_8105

# pinyin-data/pinyin.txt
>> from pypinyin_dict.pinyin_data import pinyin

# pinyin-data/zdic.txt
>> from pypinyin_dict.pinyin_data import zdic

# pinyin-data/cc_cedict.txt
>> from pypinyin_dict.pinyin_data import cc_cedict


# phrase-pinyin-data/pinyin.txt
>> from pypinyin_dict.phrase_pinyin_data import pinyin

# phrase-pinyin-data/zdic_cibs.txt
>> from pypinyin_dict.phrase_pinyin_data import zdic_cibs

# phrase-pinyin-data/zdic_cybs.txt
>> from pypinyin_dict.phrase_pinyin_data import zdic_cybs

# phrase-pinyin-data/cc_cedict.txt
>> from pypinyin_dict.phrase_pinyin_data import cc_cedict

# phrase-pinyin-data/di.txt
>> from pypinyin_dict.phrase_pinyin_data import di

# phrase-pinyin-data/large_pinyin.txt
>> from pypinyin_dict.phrase_pinyin_data import large_pinyin

```

## 生成文件

依赖 Python 3 环境。

clone 子模块：

```
git submodule init
git submodule update
```

生成 py 文件：

```
make generate
```

编辑数据文件然后生成 py 文件（可选）：

1. 进入 tools 目录
2. 编辑 pinyin-data 或 phrase-pinyin-data 里的 txt 文件（tools 目录中 Makefile 里涉及的 txt 文件）
3. 执行 `make generate` 生成最新的 py 文件
4. 可以通过 `git diff` 查看变更内容

