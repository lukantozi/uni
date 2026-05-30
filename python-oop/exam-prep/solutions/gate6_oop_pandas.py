import pandas as pd
import io
import json


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


"""
============================================================
Layer B
============================================================
"""
def layer_b():
    def task_1():
        data = "name,grade\nAlice,75\nBob,55\nCarol,90\nDave,45\nEve,60\nFrank,30"
        df = pd.read_csv(io.StringIO(data))
        print(df[df["grade"] >= 60])

    def task_2():
        data = '[{"name":"Alice","score":80},{"name":"Bob","score":40},{"name":"Carol","score":55}]'
        df = pd.DataFrame(json.loads(data))
        df["Passed"] = df["score"] >= 50
        print(df)

    def task_3():
        df = pd.DataFrame({
            "a": [1, None, 4, 0],
            "b": [3, 4, 5, 1],
            "c": [None, 2, 3, 4]
        })
        print(df.dropna())

    def task_4():
        df = pd.DataFrame({
            "a": [2, 4, 5], "b":[4, 0, 0]},
                          index=["a", "b", "c"])

        print(df.iloc[0])
        print(df.loc["a"])
        try:
            print(df.loc[0])
        except KeyError:
            print("loc takes index pars passed in")
