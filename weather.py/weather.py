#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""命令行天气查询：调用 wttr.in 公开接口，无需 API Key"""

import sys
import requests


def get_weather(city):
      """查询城市天气，返回简短文字"""
      url = f"https://wttr.in/{city}?format=3&lang=zh"
      try:
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                              return resp.text.strip()
                          return f"查询失败: HTTP {resp.status_code}"
except requests.RequestException as e:
        return f"网络错误: {e}"


if __name__ == "__main__":
      city = sys.argv[1] if len(sys.argv) > 1 else "重庆"
      print(get_weather(city))
  
