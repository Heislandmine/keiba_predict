from src.lib.webdriver import Driver

base_list_page_url: str = (
    "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date="
)
base_race_url: str = "https://race.netkeiba.com/race/result.html?race_id="

table_header = (
    "着順",
    "枠",
    "馬順",
    "馬名",
    "年齢",
    "斤量",
    "騎手",
    "タイム",
    "着差",
    "人気",
    "単勝オッズ",
    "後3F",
    "コーナー通過順",
    "厩舎",
    "馬体重(増減)",
)

driver: Driver = Driver()


def get_race_urls(data: str) -> list:
    html = driver.get_html(base_list_page_url + data)
    list_a = html.select("li.RaceList_DataItem a.LinkIconRaceMovie")

    list_race_ids: list = [a.get("id").replace("movie_", "") for a in list_a]
    list_race_urls: list = [base_race_url + race_id for race_id in list_race_ids]
    return list_race_urls


def get_race_data(url: str) -> list:
    html = driver.get_html(url)
    race_data = []
    # レースデータの取得
    race_title = html.select("div.RaceName")[0].text.strip()
    # トラック情報の取得(地面,距離)
    track_info = html.select("div.RaceData01 span", limit=1)[0].text.strip()
    track = track_info[0:1]
    distance = track_info[1:]
    # レースデータの各行を取得
    rows = html.select("table#All_Result_Table tbody tr")
    for row in rows:
        tds = row.find_all("td")
        td_dict = {header: td for header, td in zip(table_header, tds)}
        rank = _get_value_from_div(td_dict["着順"])
        waku = _get_value_from_div(td_dict["枠"])
        num_txt_c = _get_value_from_div(td_dict["馬順"])
        horse_name = _get_value_from_a(td_dict["馬名"])
        horse_info_txt_c = _get_value_from_div_span(td_dict["年齢"])
        jockey_weight = _get_value_from_div_span(td_dict["斤量"])
        jockey = _get_value_from_a(td_dict["騎手"])
        time = _get_value_from_span(td_dict["タイム"])
        race_time = _get_value_from_span(td_dict["着差"])
        odds_txt_c = _get_value_from_span(td_dict["人気"])
        odds_txt_r = _get_value_from_span(td_dict["単勝オッズ"])
        time_bg_yellow = _get_value_from_td(td_dict["後3F"])
        passage_rate = _get_value_from_td(td_dict["コーナー通過順"])
        trainer = _get_value_from_a(td_dict["厩舎"])
        weight, weight_gain_and_loss = _get_weight(td_dict["馬体重(増減)"])

        race_data.append(
            [
                race_title,
                track,
                distance,
                rank,
                waku,
                num_txt_c,
                horse_name,
                horse_info_txt_c,
                jockey_weight,
                jockey,
                time,
                race_time,
                odds_txt_c,
                odds_txt_r,
                time_bg_yellow,
                passage_rate,
                trainer,
                weight,
                weight_gain_and_loss,
            ]
        )
    return race_data


def _get_weight(html):
    data = _get_value_from_td(html)
    weight = data[:3]
    gain_and_loss = data[3:].replace("(", "").replace(")", "")

    return weight, gain_and_loss


def _get_value_from_div_span(html):
    return html.find("div").find("span").text.strip()


def _get_value_from_div(html) -> str:
    return html.find("div").text.strip()


def _get_value_from_a(html) -> str:
    return html.find("a").text.strip()


def _get_value_from_span(html) -> str:
    return html.find("span").text.strip()


def _get_value_from_td(html) -> str:
    return html.text.strip()
