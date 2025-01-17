from src.core.get_data import get_race_urls, get_race_data
from src.core.get_data import write_data_to_csv
from time import sleep


def download_race_data(date: str, wait_time=1, save_dir=""):
    race_info = get_race_urls(date)
    places = [place for place in race_info.keys()]
    for place in places:
        for races in race_info[place]:
            for r in races.keys():
                file_name = save_dir + date + place + r + ".csv"
                race_data = get_race_data(races[r])
                write_data_to_csv(file_name, race_data)

            sleep(wait_time)
