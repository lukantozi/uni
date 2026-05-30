import pandas as pd
import io


"""
============================================================
Layer A
============================================================
"""
def layer_a():
    def task_1():
        df = pd.DataFrame({
            "name": ["jack", "alice", "doe"],
            "age": [23, 28, 18],
            "city": ["new york", "dallas", "paris"]
        })
        print(df)
        print(df.shape)

    def task_2():
        df = pd.DataFrame({"score": [85, 90, None, 70, None]})
        print(df.dropna(ignore_index=True))
        print(df.fillna(0))

    def task_3():
        df = pd.DataFrame({
            "a": [2, 3, 4],
            "b": [5, 1, 3],
        })
        print(df.iloc[1, 1])
        print(df.loc[1]["b"])

    def task_4():
        data = '[{"name": "Alice", "score": 90}, {"name": "Bob", "score": 75}]'
        df = pd.read_json(io.StringIO(data))
        print(df["name"])

    def task_5():
        df = pd.DataFrame({"column": [10, 25, 5, 40, 15]})
        print(df[df["column"] > 12])
