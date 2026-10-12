#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并多个 Excel 文件：把同目录下所有 .xlsx 合并成一个文件"""

import glob
import pandas as pd


def merge_excel(pattern, output):
      """合并同目录下多个 Excel 文件"""
      files = glob.glob(pattern)
      if not files:
                print("没有找到匹配的文件")
                return

      df_list = []
      for f in files:
                df = pd.read_excel(f)
                df["source"] = f  # 标记来源文件
        df_list.append(df)
        print(f"已读取: {f} ({len(df)} 行)")

    result = pd.concat(df_list, ignore_index=True)
    result.to_excel(output, index=False)
    print(f"合并完成: {len(files)} 个文件 -> {output}，共 {len(result)} 行")


if __name__ == "__main__":
      merge_excel("./data/*.xlsx", "./merged.xlsx")
