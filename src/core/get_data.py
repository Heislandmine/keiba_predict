from src.lib.webdriver import Driver

base_list_page_url: str = (
    "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date="
)
base_race_url: str = "https://race.netkeiba.com/race/shutuba.html?race_id="

driver: Driver = Driver()


def get_race_urls(data: str) -> list:
    html = driver.get_html(base_list_page_url + data)
    list_a = html.select("li.RaceList_DataItem a.LinkIconRaceMovie")

    list_race_ids: list = [a.get("id").replace("movie_", "") for a in list_a]
    list_race_urls: list = [base_race_url + race_id for race_id in list_race_ids]
    return list_race_urls


def get_race_data(url: str) -> list:
    # レースデータの取得
    html = driver.get_html(url)
    race_title = html.select("div.RaceName")[0].text.strip()
    # トラック情報の取得(地面,距離)
    track_info = html.select("div.RaceData01 span", limit=1)[0].text.strip()
    track = track_info[0:1]
    distance = track_info[1:]
