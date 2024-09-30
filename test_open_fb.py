from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
def test_open():
    driver.get("http://49.249.28.218:8888/")
    sleep(2)
    driver.close()