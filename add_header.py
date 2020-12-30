"""レースデータCSVに不足しているレース名、地面、距離の3つのヘッダーを追加するスクリプト"""
import pathlib
import sys

root_dir = sys.argv[1]
save_dir = sys.argv[2]

p = pathlib.Path(root_dir)

for path in p.glob("*.csv"):
    with open(path, "r", encoding="utf-8", newline="") as f:
        s = f.readlines()

    file_name = path.name
    save_path = save_dir + file_name

    with open(save_path, "w", encoding="utf-8", newline="") as f:
        for i, line in enumerate(s):
            # line = line.strip()
            if i == 0:
                line = "レース名,地面,距離," + line
                f.write(line)
            else:
                f.write(line)
