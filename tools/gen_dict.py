# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import os.path


def gen_pinyin_dict(src_path, dst_name):
    dst_path = '../src/pypinyin_dict/pinyin_data/{}.py'.format(dst_name)
    dist_path = os.path.abspath(dst_path)
    code = subprocess.call(['python', 'gen_pinyin_dict.py',
                            src_path, dist_path])
    assert code == 0

    print('{} -> {}'.format(src_path, dst_path))


def gen_phrase_dict(src_path, dst_name, num):
    dst_path = '../src/pypinyin_dict/phrase_pinyin_data/{}.py'.format(dst_name)
    dist_path = os.path.abspath(dst_path)
    code = subprocess.call(['python', 'gen_phrases_dict.py',
                            src_path, dist_path, str(num)])
    assert code == 0

    print('{} -> {}'.format(src_path, dst_path))


def main():
    file = sys.argv[1]
    num = 1
    if len(sys.argv) > 2:
        num = sys.argv[2]

    name = file.split('/')[-1].lower().split('.')[0]
    if 'phrase' in file:
        gen_phrase_dict(file, name, num)
    else:
        gen_pinyin_dict(file, name)


if __name__ == '__main__':
    main()
