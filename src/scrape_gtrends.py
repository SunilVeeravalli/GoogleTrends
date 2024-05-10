import shutil
from time import sleep

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scrape_gtrends(keywords: list,
                   start_date: str,
                   end_date: str,
                   geo: str,
                   csv_directory_location: str) -> None:

    csv_fnames = (["kwds_score_relative_each_other"] +
                  [f"scores_for_kwd_{kwd}" for kwd in keywords])

    url = (f"https://trends.google.co.uk/trends/explore?date={start_date}%20"
           f"{end_date}&geo={geo}&q={','.join(keywords)}&hl=en-GB")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": csv_directory_location,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    })
    # options.add_argument('--headless')

    driver = webdriver.Chrome(
        service = ChromeService(ChromeDriverManager().install()),
        options = options)

    driver.set_window_size(width = 1374, height = 1000)

    driver.get(url)
    sleep(1)
    driver.refresh()

    sleep(2)

    try:
        driver.find_element(by = By.CSS_SELECTOR,
                            value = 'a[role="button"]').click()
    except Exception as _:
        pass

    geo_buttons = driver.find_elements(
        by = By.CLASS_NAME,
        value = "resolution-selector-container"
    )

    widget_maps = driver.find_elements(
        by = By.CSS_SELECTOR,
        value = "trends-widget[widget-name^=GEO_MAP]"
    )

    scrollings = np.cumsum([650, 600, 575, 550, 525, 500])

    for idx, geo_button in enumerate(geo_buttons):
        driver.execute_script(f"window.scrollTo(0, {scrollings[idx]})")

        dropdown = geo_button.find_element(
            by = By.CLASS_NAME,
            value = "_md-select-value"
        )

        dropdown.click()
        sleep(1)

        city = driver.find_element(
            by = By.CLASS_NAME,
            value = "_md-select-menu-container.geo-resolution._md-active._md"
                    "-clickable"
        ).find_element(by = By.CSS_SELECTOR,
                       value = "md-option[value='city']")

        city.click()
        sleep(5)

        low_search_vol_checkboxes = driver.find_elements(
            by = By.CSS_SELECTOR,
            value = 'md-checkbox[aria-label="Include low search volume '
                    'regions"]')

        try:
            low_search_vol_checkboxes[-1].click()
        except Exception as _:
            pass

        sleep(5)

        download_csv = widget_maps[idx].find_element(
            by = By.CSS_SELECTOR,
            value = 'button[title="CSV"]'
        )
        download_csv.click()
        sleep(2)
        shutil.move("Data_Output/geoMap.csv",
                    f"Data_Output/{csv_fnames[idx]}.csv")

    driver.quit()
