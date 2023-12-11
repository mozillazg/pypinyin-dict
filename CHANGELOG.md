# ChangeLog

## [0.7.0] (2023-12-11)

* 基于 phrase-pinyin-data v0.16.0 和 pinyin-data v0.14.0 生成最新的数据


## [0.6.0] (2023-05-14)

* 基于 phrase-pinyin-data v0.15.0 生成最新的数据


## [0.5.0] (2023-01-15)

* 基于 phrase-pinyin-data v0.14.0 生成最新的数据


## [0.4.0] (2022-11-06)

* 将 `phrase_pinyin_data` 中的多个数据文件切分为数量不等的 py 文件
  解决 python 10 下可能会出现 `OverflowError: line number table is too long`
  错误的问题。 (fixed [#3] [#5] )


## [0.3.0] (2022-07-31)

* 基于 phrase-pinyin-data v0.13.0 以及 pinyin-data v0.13.0 生成最新的数据
* 新增使用数据文件 phrase-pinyin-data/di.txt 的模块（纠正部分短语中`地`的拼音）:

```
from pypinyin_dict.phrase_pinyin_data import di
```

## [0.2.0] (2021-11-14)

* 基于 phrase-pinyin-data v0.12.0 以及 pinyin-data v0.12.0 生成最新的数据


## 0.1.0 (2021-09-20)

* Initial Release

[#3]: https://github.com/mozillazg/pypinyin-dict/issues/3
[#5]: https://github.com/mozillazg/pypinyin-dict/issues/5

[0.2.0]: https://github.com/mozillazg/pypinyin-dict/compare/v0.1.0...v0.2.0
[0.3.0]: https://github.com/mozillazg/pypinyin-dict/compare/v0.2.0...v0.3.0
[0.4.0]: https://github.com/mozillazg/pypinyin-dict/compare/v0.3.0...v0.4.0
[0.5.0]: https://github.com/mozillazg/pypinyin-dict/compare/v0.4.0...v0.5.0
[0.6.0]: https://github.com/mozillazg/pypinyin-dict/compare/v0.5.0...v0.6.0
[0.7.0]: https://github.com/mozillazg/pypinyin-dict/compare/v0.6.0...v0.7.0
