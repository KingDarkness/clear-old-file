#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import argparse


def clear_directory_older_than(directory, days):
    now = time.time()
    cutoff = now - (days * 86400)
    files = os.listdir(directory)
    for xfile in files:
        t = os.stat(os.path.join(directory, xfile))
        c = t.st_ctime
        if c < cutoff:
            os.remove(os.path.join(directory, xfile))


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-days', metavar='N', type=int, help='Xoá file tạo trước hiện tại [days] ngày', required=True)
    argparser.add_argument('-d', '--directory', action='append', help='Danh sách thư mục cần xoá', required=True)

    args = argparser.parse_args()

    for directory in args.directory:
        clear_directory_older_than(directory, args.days)
