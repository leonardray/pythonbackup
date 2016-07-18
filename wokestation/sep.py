#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.seec.local")

driver.find_element_by_name("username").send_keys("18910161612")
driver.find_element_by_name("password").send_keys("6941200lzr")
driver.find_element_by_name("password").send_keys("6941200lzr")
