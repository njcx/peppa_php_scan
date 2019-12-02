# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 11:11 AM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : check.py

import os

def walk_php_file(dir_):
    for root, dirs, files in os.walk(dir_):
        for f in files:
            if f.endswith(".php"):
                print(os.path.join(root, f))

def main():
    walk_php_file("/Users/njcx/project/peppa_phpcode_scanner/test")


if __name__ == '__main__':
    main()