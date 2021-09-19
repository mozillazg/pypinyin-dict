# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import os.path

pinyin_dict_loader = '''
from pypinyin import load_single_dict


def load():
    load_single_dict(pinyin_dict)
'''

pharse_dict_loader = '''
from pypinyin import load_phrases_dict


def load():
    load_phrases_dict(phrases_dict)
'''


def gen_pinyin_dict(src_path, dst_name):
    dst_path = '../src/pypinyin_dict/pinyin_data/{}.py'.format(dst_name)
    dist_path = os.path.abspath(dst_path)
    code = subprocess.call(['python', 'python-pinyin/gen_pinyin_dict.py',
                            src_path, dist_path])
    assert code == 0
    with open(dist_path) as fp:
        content = fp.read()
    with open(dist_path, 'w') as fp:
        fp.write(content)
        fp.write('\n')
        fp.write(pinyin_dict_loader)

    print('{} -> {}'.format(src_path, dst_path))


def gen_phrase_dict(src_path, dst_name):
    dst_path = '../src/pypinyin_dict/phrase_pinyin_data/{}.py'.format(dst_name)
    dist_path = os.path.abspath(dst_path)
    code = subprocess.call(['python', 'python-pinyin/gen_phrases_dict.py',
                            src_path, dist_path])
    assert code == 0
    with open(dist_path) as fp:
        content = fp.read()
    with open(dist_path, 'w') as fp:
        fp.write(content)
        fp.write('\n')
        fp.write(pharse_dict_loader)

    print('{} -> {}'.format(src_path, dst_path))


def main():
    files = sys.argv[1:]
    for file in files:
        name = file.split('/')[-1].lower().split('.')[0]
        if 'phrase' in file:
            gen_phrase_dict(file, name)
        else:
            gen_pinyin_dict(file, name)


if __name__ == '__main__':
    main()
