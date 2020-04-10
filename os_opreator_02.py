#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
输入一个路径，然后 输入dir -l 输出目录下的所有
搜索指定的内容，输出搜索结果
查找文件名或路径名包含指定字符串的文件，并打印出相对路径
"""
import os


def dir_l(path):
    lis = os.listdir(path)
    for i in lis:
        print(i)


def seach(path, s):
    dir_dict = dict()
    file_dict = dict()
    miss_list = []

    def seach_for(path, s):
        try:
            lis = os.listdir(path)
            for i in lis:
                if i[0] == '.':
                    continue
                if os.path.isdir(os.path.join(path, i)):
                    if s in i:
                        dir_dict[i] = os.path.join(path, i)
                        # print(i, '==>', os.path.join(path, i))
                    seach_for(os.path.join(path, i), s)
                if os.path.isfile(os.path.join(path, i)):
                    if s in i:
                        file_dict[i] = os.path.join(path, i)
                        # print(i, '==>', os.path.join(path, i))
        except Exception:
            miss_list.append(path)
    seach_for(path, s)
    print('搜索到的目录：')
    for key, item in dir_dict.items():
        print(key, '==>', item)
    print('搜索到的文件：')
    for key, item in file_dict.items():
        print(key, '==>', item)
    print('跳过的目录：')
    for i in miss_list:
        print(i)


def main():
    path = input('请输入一个路径：')
    while True:
        if os.path.isdir(path):
            print('输入的路径是：\n', path, sep='')
            break
        else:
            path = input('输入的路径错误，请重新输入:')
    while True:
        command = input('请输入要进行的操作命令(退出：Q，帮助：help)：')
        if command == 'Q':
            break
        if command == 'dir -l':
            dir_l(path)
        if command == 'seach':
            s = input('请输要搜索的内容：')
            seach(path, s)
        if command == 'help':
            print('''
                [command]    function
                dir -l      列出当前目录下的所有
                seach       搜索指定内容
                ''')


if __name__ == "__main__":
    main()