#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""命令行待办清单：添加、查看、完成、删除待办事项，数据存 JSON 文件"""

import json
import os
import sys

TODO_FILE = os.path.join(os.path.dirname(__file__), "todo.json")


def load():
      if os.path.exists(TODO_FILE):
                with open(TODO_FILE, encoding="utf-8") as f:
                              return json.load(f)
                      return []


def save(tasks):
      with open(TODO_FILE, "w", encoding="utf-8") as f:
                json.dump(tasks, f, ensure_ascii=False, indent=2)


def show():
      tasks = load()
      if not tasks:
                print("暂无待办事项")
                return
            for i, t in enumerate(tasks, 1):
                      status = "[x]" if t["done"] else "[ ]"
                      print(f"{i}. {status} {t['task']}")


def add(task):
      tasks = load()
    tasks.append({"task": task, "done": False})
    save(tasks)
    print(f"已添加: {task}")


def done(idx):
      tasks = load()
    if 1 <= idx <= len(tasks):
              tasks[idx - 1]["done"] = True
              save(tasks)
              print(f"已完成: {tasks[idx - 1]['task']}")
else:
        print("序号无效")


def remove(idx):
      tasks = load()
    if 1 <= idx <= len(tasks):
              removed = tasks.pop(idx - 1)
              save(tasks)
              print(f"已删除: {removed['task']}")
else:
        print("序号无效")


if __name__ == "__main__":
      args = sys.argv[1:]
    if not args:
              show()
elif args[0] == "add":
        add(" ".join(args[1:]))
elif args[0] == "done" and len(args) > 1:
        done(int(args[1]))
elif args[0] == "rm" and len(args) > 1:
        remove(int(args[1]))
else:
        print("用法: todo.py [add 内容 | done 序号 | rm 序号]")
  
