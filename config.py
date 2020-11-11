#!/usr/bin/env python
# encoding: utf-8
"""
@author: liuxiangfeng
@file: config.py
@time: 2020/11/11 18:44
@desc:
"""
import time


def print_name(file_path):
    with open(file_path, "r") as f_open:
        time.sleep(10)
        return f_open.read()


def update(name):
    print(name)


if __name__ == '__main__':
    print_name()
