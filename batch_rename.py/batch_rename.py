#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量重命名文件：给目录下所有文件加统一前缀"""

import os
import argparse


def batch_rename(dir_path, prefix):
      """给目录下所有文件加前缀"""
      count = 0
      for f in os.listdir(dir_path):
                old = os.path.join(dir_path, f)
                if os.path.isfile(old):
                              new = os.path.join(dir_path, prefix + f)
                              os.rename(old, new)
                              count += 1
                              print(f"已重命名: {f} -> {prefix}{f}")
                      print(f"完成，共重命名 {count} 个文件")


if __name__ == "__main__":
      parser = argparse.ArgumentParser(description="批量重命名文件")
      parser.add_argument("dir", help="目标目录")
      parser.add_argument("--prefix", default="2026_", help="要加的前缀")
      args = parser.parse_args()
      batch_rename(args.dir, args.prefix)
  
