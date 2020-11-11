#!/usr/bin/env python
# encoding: utf-8
"""
@author: liuxiangfeng
@file: main.py
@time: 2020/11/11 18:44
@desc:
"""
import config
import time
import threading
import os
import gc

base_dir = os.path.abspath(os.path.dirname(__file__))
model_dir = os.path.join(base_dir, "model")

model_version = None
name = ""


def func1():
    global name
    name = "123"
    while True:
        start_time = time.time()
        config.update(name)
        time.sleep(1)
        print(time.time() - start_time)


def func2():
    while True:
        flag = 0
        global model_version
        global name
        for file in os.listdir(model_dir):
            if model_version is None:
                model_version = file
            else:
                if file > model_version:
                    model_version = file
                    flag = 1
        if flag:
            print("reload config {}".format(model_version))
            new_name = config.print_name(os.path.join(model_dir, model_version))
            name = new_name
            del new_name
            gc.collect()


if __name__ == '__main__':
    t1 = threading.Thread(target=func1, )
    t2 = threading.Thread(target=func2, )
    t1.start()
    t2.start()
    t1.join()
    t2.join()

