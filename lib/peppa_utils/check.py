# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 11:11 AM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : check.py

import os
import re
from queue import Queue


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


def main():
    x, y = walk_php_file("/Users/njcx/project/peppa_phpcode_scanner/test")
    print(x, y)
    if match_comment(r"require 'front-office/public/index.html';"):
        print("ok")


if __name__ == '__main__':
    main()
