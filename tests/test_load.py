# -*- coding: utf-8 -*-

from pypinyin_dict.pinyin_data import (
    cc_cedict as single_cc_cedict,
    khanyupinlu,
    khanyupinyin,
    kmandarin_8105,
    ktghz2013,
    kxhc1983,
    pinyin as single_pinyin,
    zdic
)
from pypinyin_dict.phrase_pinyin_data import (
    cc_cedict as phrase_cc_cedict,
    large_pinyin,
    pinyin as phrase_pinyin,
    zdic_cibs,
    zdic_cybs,
    di
)
from pypinyin import lazy_pinyin


def test_load_pinyin_data():
    single_cc_cedict.load()
    khanyupinyin.load()
    khanyupinlu.load()
    kmandarin_8105.load()
    ktghz2013.load()
    kxhc1983.load()
    single_pinyin.load()
    zdic.load()


def test_load_pharse_pinyin_data():
    phrase_cc_cedict.load()
    large_pinyin.load()
    phrase_pinyin.load()
    zdic_cibs.load()
    zdic_cybs.load()
    di.load()


def test_pypinyin():
    lazy_pinyin('测试')
