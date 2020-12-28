from src.core.get_data import get_race_urls, get_race_data

# race_urls = get_race_urls("20201226")

res = get_race_data("https://race.netkeiba.com/race/shutuba.html?race_id=202006050704")
print(res)
