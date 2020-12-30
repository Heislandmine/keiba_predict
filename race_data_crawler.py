from src.data_downloader import download_race_data

start_y = 2011
end_y = 2020
save_dir = "race_data/"

current_y = start_y
while current_y <= end_y:
    for m in range(1, 13):
        for d in range(1, 32):
            date = str(current_y) + f"{m:02}{d:02}"
            print(date)
            try:
                download_race_data(date, save_dir=save_dir)
            except Exception:
                print("err:{}".format(date))
    current_y += 1
