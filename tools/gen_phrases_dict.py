# -*- coding: utf-8 -*-
import os.path
import sys


def remove_dup_items(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


def parse(in_fp):
    phrases_dict = {}
    for line in in_fp.readlines():
        line = line.strip()
        if line.startswith('#') or not line:
            continue

        # 中国: zhōng guó
        data = line.split('#')[0]
        hanzi, pinyin = data.strip().split(':')
        hanzi = hanzi.strip()
        # [[zhōng], [guó]]
        pinyin_list = [[s] for s in pinyin.split()]

        if hanzi not in phrases_dict:
            phrases_dict[hanzi] = pinyin_list
        else:
            for index, value in enumerate(phrases_dict[hanzi]):
                value.extend(pinyin_list[index])
                phrases_dict[hanzi][index] = remove_dup_items(value)

    return phrases_dict


def generate_file(hanzi_pairs, out_fp):

    out_fp.write('''# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Warning: Auto-generated file, don't edit.
phrases_dict = {
''')

    for hanzi, pinyin_list in hanzi_pairs:
        #     中国: [[zhōng], [guó]]
        new_line = "    '{hanzi}': {pinyin_list},\n".format(
            hanzi=hanzi.strip(), pinyin_list=pinyin_list
        )
        out_fp.write(new_line)
    out_fp.write('}\n')


def generate_multi_file(hanzi_pairs, out_name, num):
    base_name, ext = os.path.splitext(out_name)
    length = len(hanzi_pairs)
    file_names = []
    size = int(length / num)
    start = 0
    end = start + size
    for i in range(num + 1):
        file_name = '{}_{}{}'.format(base_name, i, ext)
        paris = hanzi_pairs[start:end]
        if not paris:
            continue

        with open(file_name, 'w') as fp:
            generate_file(paris, fp)

        file_names.append(file_name)
        start = end
        end = start + size

    with open(out_name, 'w') as fp:
        fp.write('''# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Warning: Auto-generated file, don't edit.
phrases_dict = {}

''')
        for i, name in enumerate(file_names):
            name = os.path.basename(name)
            base_name, _ = os.path.splitext(name)
            fp.write('''
from pypinyin_dict.phrase_pinyin_data import {0}
phrases_dict.update({0}.phrases_dict)
'''.format(base_name))


def main(in_name, out_name, num):
    with open(in_name) as in_fp:
        hanzi_pairs = sorted(parse(in_fp).items(), key=lambda x: x[0])

    if num < 2:
        with open(out_name, 'w') as out_fp:
            generate_file(hanzi_pairs, out_fp)
    else:
        generate_multi_file(hanzi_pairs, out_name, num)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('python gen_phrases_dict.py INPUT OUTPUT [OUTPUT_FILE_NUM]')
        sys.exit(1)

    in_f = sys.argv[1]
    out_f = sys.argv[2]
    file_num = 1
    if len(sys.argv) > 3:
        file_num = int(sys.argv[3])

    main(in_f, out_f, file_num)
