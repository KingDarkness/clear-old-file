#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime
import argparse


def clear_directory_older_than(directory, days):
    print "Xoá dữ liệu tạo trước %s ngày thư mục %s " % (days, directory)
    now = time.time()
    cutoff = now - (days * 86400)
    files = os.listdir(directory)
    for xfile in files:
        t = os.stat(os.path.join(directory, xfile))
        c = t.st_mtime
        if c < cutoff and not os.path.isdir(os.path.join(directory, xfile)):
            print "Xoá: %s | tạo lúc: %s" % (os.path.join(directory, xfile), datetime.fromtimestamp(c).strftime('%d-%m-%Y %H:%M:%S'))
            os.remove(os.path.join(directory, xfile))


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-days', metavar='N', type=int, help='Xoá file tạo trước hiện tại [days] ngày', required=True)
    argparser.add_argument('-d', '--directory', action='append', help='Danh sách thư mục cần xoá', required=True)

    args = argparser.parse_args()

    for directory in args.directory:
        clear_directory_older_than(directory, args.days)
