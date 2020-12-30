"""レースデータCSVに不足しているレース名、地面、距離の3つのヘッダーを追加するスクリプト"""
import pathlib

p = pathlib.Path("./")

for path in p.glob("*.csv"):
    with open(path, "r", encoding="utf-8", newline="") as f:
        s = f.readlines()
    with open("tst.csv", "w", encoding="utf-8", newline="") as f:
        for i, line in enumerate(s):
            # line = line.strip()
            if i == 0:
                line = "race_name,ground,distance," + line
                f.write(line)
            else:
                f.write(line)
