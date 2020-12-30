import pathlib
import sys

root_dir = sys.argv[1]
save_dir = sys.argv[2]

p = pathlib.Path(root_dir)

with open(save_dir + "master.csv", "w", encoding="utf-8", newline="") as master:
    for i, path in enumerate(p.glob("*.csv")):
        with open(path, "r", encoding="utf-8", newline="") as f:
            header = f.readline()
            s = f.readlines()
        if i == 0:
            master.write(header)

        for line in s:
            master.write(line)
