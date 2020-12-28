from src.data_downloader import download_race_data
import sys

save_dir = "race_data/"  # todo:オプション引数としてとれるように直す
if __name__ == "__main__":
    date = sys.argv[1]

    download_race_data(date, save_dir=save_dir)