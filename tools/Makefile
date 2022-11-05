

gen: gen_pinyin_dict gen_phrase_pinyin_dict

gen_pinyin_dict:
	python gen_dict.py pinyin-data/kTGHZ2013.txt
	python gen_dict.py pinyin-data/kHanyuPinyin.txt
	python gen_dict.py pinyin-data/kXHC1983.txt
	python gen_dict.py pinyin-data/kHanyuPinlu.txt
	python gen_dict.py pinyin-data/kMandarin_8105.txt
	python gen_dict.py pinyin-data/pinyin.txt
	python gen_dict.py pinyin-data/zdic.txt
	python gen_dict.py pinyin-data/cc_cedict.txt

gen_phrase_pinyin_dict:
	python gen_dict.py phrase-pinyin-data/pinyin.txt
	python gen_dict.py phrase-pinyin-data/zdic_cibs.txt
	python gen_dict.py phrase-pinyin-data/zdic_cybs.txt
	python gen_dict.py phrase-pinyin-data/cc_cedict.txt
	python gen_dict.py phrase-pinyin-data/di.txt
	python gen_dict.py phrase-pinyin-data/large_pinyin.txt 3
