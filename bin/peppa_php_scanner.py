# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : peppa-scanner.py

import sys
import os
import argparse
pwd = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.dirname(pwd) + os.path.sep + "lib"))
from pyfiglet import Figlet
from peppa_utils.color_print import ColorPrint


def banner():
    banner_ = Figlet(font='smslant')
    print(banner_.renderText('Peppa-PHP-Scanner'))
    print("<---------WELCOME TO USE THIS PROGRAM--------->")
    print("<---------v1.0 - Author - nJcx86--------->")
    print("\n")


def parse_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, add_help=False)

    parser.add_argument("-h", "--help", action="help",
                        help="Show help message and exit")

    target = parser.add_argument_group('[ Targets ]')

    target.add_argument("-d", "--dir", dest="dir",
                        help="Target Dir (e.g. \"https://www.google.com/\")")

    target.add_argument("-t", "--threads", dest="process_num",
                        help="max number of process, default cpu number")

    args = parser.parse_args()

    return args.__dict__


if __name__ == "__main__":

    color_print = ColorPrint()

    banner()
    parse_options()





