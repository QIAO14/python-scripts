# Python 实用脚本合集

日常开发常用的 Python 小工具脚本，覆盖文件处理、数据处理与自动化任务。

## 仓库结构

| 文件 | 功能 |
|---|---|
| batch_rename.py | 批量重命名文件 |
| excel_merge.py | 合并多个 Excel 文件 |
| weather.py | 命令行天气查询 |
| todo.py | 命令行待办清单 |

## 环境要求

- Python 3.8+
- 部分脚本需要第三方库：pandas、openpyxl、requests

```bash
pip install pandas openpyxl requests
```

## 脚本说明

### 1. batch_rename.py 批量重命名

```python
import os

def batch_rename(dir_path, prefix):
    """给目录下所有文件加前缀"""
        for f in os.listdir(dir_path):
                old = os.path.join(dir_path, f)
                        if os.path.isfile(old):
                                    new = os.path.join(dir_path, prefix + f)
                                                os.rename(old, new)
                                                            print(f"已重命名: {f} -> {prefix}{f}")

                                                            if __name__ == "__main__":
                                                                batch_rename("./files", "2026_")
                                                                ```

                                                                ### 2. excel_merge.py 合并 Excel

                                                                ```python
                                                                import pandas as pd
                                                                import glob

                                                                def merge_excel(pattern, output):
                                                                    """合并同目录下多个 Excel 文件"""
                                                                        files = glob.glob(pattern)
                                                                            df_list = [pd.read_excel(f) for f in files]
                                                                                result = pd.concat(df_list, ignore_index=True)
                                                                                    result.to_excel(output, index=False)
                                                                                        print(f"合并完成: {len(files)} 个文件 -> {output}")

                                                                                        if __name__ == "__main__":
                                                                                            merge_excel("./data/*.xlsx", "./merged.xlsx")
                                                                                            ```

                                                                                            ### 3. weather.py 天气查询

                                                                                            ```python
                                                                                            import requests

                                                                                            def get_weather(city):
                                                                                                """调用公开天气 API 查询城市天气"""
                                                                                                    url = f"https://wttr.in/{city}?format=3"
                                                                                                        resp = requests.get(url, timeout=10)
                                                                                                            print(resp.text)
                                                                                                            
                                                                                                            if __name__ == "__main__":
                                                                                                                get_weather("重庆")
                                                                                                                ```
                                                                                                                
                                                                                                                ### 4. todo.py 待办清单
                                                                                                                
                                                                                                                ```python
                                                                                                                import json, os
                                                                                                                
                                                                                                                TODO_FILE = "todo.json"
                                                                                                                
                                                                                                                def add_task(task):
                                                                                                                    tasks = load()
                                                                                                                        tasks.append({"task": task, "done": False})
                                                                                                                            save(tasks)
                                                                                                                                print(f"已添加: {task}")
                                                                                                                                
                                                                                                                                def show():
                                                                                                                                    for i, t in enumerate(load(), 1):
                                                                                                                                            status = "✓" if t["done"] else " "
                                                                                                                                                    print(f"{i}. [{status}] {t['task']}")
                                                                                                                                                    
                                                                                                                                                    def load():
                                                                                                                                                        if os.path.exists(TODO_FILE):
                                                                                                                                                                with open(TODO_FILE) as f:
                                                                                                                                                                            return json.load(f)
                                                                                                                                                                                return []
                                                                                                                                                                                
                                                                                                                                                                                def save(tasks):
                                                                                                                                                                                    with open(TODO_FILE, "w") as f:
                                                                                                                                                                                            json.dump(tasks, f, ensure_ascii=False)
                                                                                                                                                                                            
                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                show()
                                                                                                                                                                                                ```
                                                                                                                                                                                                
                                                                                                                                                                                                ## 后续计划
                                                                                                                                                                                                - 日志分析脚本
                                                                                                                                                                                                - 数据库备份脚本
                                                                                                                                                                                                - 网页爬虫示例
                                                                                                                                                                                                - 数据清洗工具
