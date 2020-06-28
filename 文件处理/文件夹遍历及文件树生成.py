'''
@Author: LW
@Date: 2020-06-20 21:30:18
@LastEditTime: 2020-06-25 22:28:21
@LastEditors: Please set LastEditors
@Description: 遍历文件夹，生成路径文件树
@FilePath: \py_project\sometools\文件处理\LW_dealfile.py
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# a test for traverse directory

import os
import pprint
import os.path


class FileClass:
    def __init__(self, name):
        self.filename = name

#    ###遍历文件夹，处理每个文件
    def walkfile(self):
        """
        root [表示当前正在访问的文件夹路径],
        dirs [表示该文件夹下的子目录名list],
        files [表示该文件夹下的文件list]
        """
        file = self.filename
        for root, dirs, files in os.walk(file):
            # 遍历文件
            for f in files:
                print(os.path.join(root, f))

            # 遍历所有的文件夹
            for d in dirs:
                print(os.path.join(root, d))

    def dir_tree(self, path, sub_tree):
        if sub_tree == 0:
            print(path)  # 输出第一级目录

        path_tree = os.listdir(path)  # 获取当前目录下的文件和目录

        for item in path_tree:
            if '.git' not in item:
                print("|  " * sub_tree + "|___" + item)
                subtree = path + '\\' + item
                if os.path.isdir(subtree):  # 判断是否为目录
                    FileClass.dir_tree(self, subtree, sub_tree + 1)  # 递归深度优先遍历

def main():
    A = FileClass("./")
    A.walkfile()
    print(A.walkfile.__doc__)

    basepath = input(">>:")
    A.dir_tree(basepath, 0)

if __name__ == '__main__':
    main()
