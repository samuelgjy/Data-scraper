import os
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#store data
path_to_file = "C:/Users/itrol/OneDrive/Desktop/All_Repo/AllHotels.csv"
num_page = 2

url = "https://www.tripadvisor.com.sg/Hotel_Review-g294265-d1845693-Reviews-The_Fullerton_Bay_Hotel_Singapore-Singapore.html#REVIEWS"

#only for keying in cmd then use
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

os.environ['PATH'] += r"C:/SeleniumDrivers"
#import webdriver my method
driver = webdriver.Chrome()
driver.get(url)

#open file to save review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

for i in range(0, num_page):

    time.sleep(2)
    #remove . later and try
    #to click Read More
    driver.find_element(By.XPATH, "//span[@class='Ignyf _S Z']").click()

    container = driver.find_elements(By.XPATH, ".//div[@class='YibKl MC R2 Gi z Z BB pBbQr']")

    for j in range(len(container)):
        
        #title not working
        title = container[j].find_element(By.XPATH,".//a[@class='Qwuub']").text
        date = container[j].find_element(By.XPATH,".//span[@class='teHYY _R Me S4 H3']").text
        rating = container[j].find_element(By.XPATH,".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        review = container[j].find_element(By.XPATH,".//q[@class='QewHA H4 _a']").text.replace("\n", " ")

        csvWriter.writerow([title, date, rating, review])

    
    driver.find_element(By.XPATH,".//a[@class='ui_button nav next primary ']").click()

driver.close()
