# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Warning: Auto-generated file, don't edit.
phrases_dict = {}


from pypinyin_dict.phrase_pinyin_data import large_pinyin_0
phrases_dict.update(large_pinyin_0.phrases_dict)

from pypinyin_dict.phrase_pinyin_data import large_pinyin_1
phrases_dict.update(large_pinyin_1.phrases_dict)

from pypinyin_dict.phrase_pinyin_data import large_pinyin_2
phrases_dict.update(large_pinyin_2.phrases_dict)


from pypinyin import load_phrases_dict


def load():
    load_phrases_dict(phrases_dict)
