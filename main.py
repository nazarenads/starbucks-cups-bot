import os
import requests as requests
import schedule as schedule
import time


from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from constants import MESSAGE_TITLE, STORES, XPATH_PRODUCTS_CONTAINER, \
    TELEGRAM_BOT_API_SEND_MESSAGE_URL


def get_text_from_cups(browser):
    wait = ui.WebDriverWait(browser, 10)
    text_to_send = ''
    for store in STORES:
        browser.get(store.get("url"))
        wait.until(lambda driver: driver.find_element(
            By.XPATH, XPATH_PRODUCTS_CONTAINER
        ))
        time.sleep(5)
        cups_list = browser.find_elements(By.CLASS_NAME, 'business-product')
        text_list = [cup.text for cup in cups_list]
        text_title = f"{MESSAGE_TITLE}".format(
            store_name=store.get("name")
        )
        cups_text = text_title + ' '.join(text_list) + '\n'
        text_to_send = text_to_send + cups_text
    return text_to_send


def cups_available():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(
        "chromedriver",
        options=chrome_options,
        service_args=[
            '--verbose',
            '--log-path=/tmp/chromedriver.log'
        ]
    )
    text_to_send = get_text_from_cups(browser)

    # send the message
    api_url = f"{TELEGRAM_BOT_API_SEND_MESSAGE_URL}".format(
        api_token=os.environ.get("TELEGRAM_BOT_API_TOKEN"),
        chat_id=os.environ.get("BOT_CHAT_ID"),
        text=text_to_send
    )
    requests.get(api_url)


if __name__ == '__main__':

    schedule.every().hour.do(cups_available)

    while True:
        schedule.run_pending()
