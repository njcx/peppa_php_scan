# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 11:11 AM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : check.py

import os
import re
from queue import Queue
from rules.rules import datas


def walk_php_file(dir_):
    queue = Queue()
    tem_list = []
    try:
        if os.path.isdir(dir_):
            for root, dirs, files in os.walk(dir_):
                for f in files:
                    if f.endswith(".php"):
                        php_file_dir_ = os.path.join(root, f)
                        queue.put_nowait(php_file_dir_)
                        tem_list.append(php_file_dir_)
    except Exception as e:
        return queue, tem_list
    return queue, tem_list


def match_comment(text):
    try:
        return re.search(r"(?<!:)\/\/.*|\#[^\n]*|\/\*(\s|.)*?|\*(\s|.)*?|\*\/", text)
    except Exception as e:
        return None


def check_line(text_):
    tem_list = []
    for item in datas:
        pre_re_ = re.compile(item.get('re'))
        item['re'] = pre_re_
        tem_list.append(item)

    for re_pattern in tem_list:

        if re_pattern['re'].match(text_):
            return True, re_pattern['info']

    return False


def read_line(dir_):
    array2 = []
    try:
        with open(dir_) as lines:
            array = lines.readlines()
            for i in array:
                i = i.strip('\n')
                array2.append(i)
        return array2
    except Exception as e:
        return array2


def main():
    x, y = walk_php_file("/Users/njcx/project/peppa_phpcode_scanner/test")
    for file_ in y:
        # print(y)
        for line in read_line(file_):
            # print(line)
            if check_line(line):
                print(line, check_line(line))

if __name__ == '__main__':
    main()
