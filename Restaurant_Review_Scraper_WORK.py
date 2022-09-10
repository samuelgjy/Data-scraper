import os
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#store data
path_to_file = "C:/Users/itrol/OneDrive/Desktop/All_Repo/Python_test/HotelReviews.csv"
num_page = 10

url = "https://www.tripadvisor.com/Restaurant_Review-g60763-d802686-Reviews-Hard_Rock_Cafe-New_York_City_New_York.html"

if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

os.environ['PATH'] += r"C:/SeleniumDrivers"
#import webdriver use their one first else use my method
driver = webdriver.Chrome()
driver.get(url)

#open file to save review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

for i in range(0, num_page):

    time.sleep(2)
    #remove . later and try
    driver.find_element(By.XPATH, "//span[@class='taLnk ulBlueLinks']").click()

    container = driver.find_elements(By.XPATH, ".//div[@class='review-container']")

    for j in range(len(container)):

        title = container[j].find_element(By.XPATH,".//span[@class='noQuotes']").text
        date = container[j].find_element(By.XPATH,".//span[@class='ratingDate']").get_attribute("title")
        rating = container[j].find_element(By.XPATH,".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        review = container[j].find_element(By.XPATH,".//p[@class='partial_entry']").text.replace("\n", " ")

        csvWriter.writerow([date, rating, review])

    driver.find_element(By.XPATH,".//a[@class='nav next ui_button primary']").click()

driver.close()




