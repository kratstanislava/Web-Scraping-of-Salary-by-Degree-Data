from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint
import pandas as pd
import numpy as np


chrome_driver_path = "C:/Users/Вселенная/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

major, early_career_pay, mid_career_pay, high_meaning = [], [], [], []

driver.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
for k in range(1, 25):
    major_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[2]/span[2]').text
    early_pay_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[4]/span[2]').text
    mid_pay_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[5]/span[2]').text
    high_meaning_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[6]/span[2]').text
    major.append(major_data)
    try:
        early_career_pay.append(float(early_pay_data[1:].replace(',', '.')))
    except:
        early_career_pay.append(np.nan)
        
    try:
        mid_career_pay.append(float(mid_pay_data[1:].replace(',', '.')))
    except:
        mid_career_pay.append(np.nan)
    
    try:
        high_meaning.append(int(high_meaning_data[:-1]))
    except:
        high_meaning.append(np.nan)
    
for i in range(1, 35):
    
    if i == 1:
        driver.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
    else:
        driver.get(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}")    
    
    if i != 34:
        for k in range(1, 25):
            major_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[2]/span[2]').text
            early_pay_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[4]/span[2]').text
            mid_pay_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[5]/span[2]').text
            high_meaning_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[6]/span[2]').text
            major.append(major_data)
            try:
                early_career_pay.append(float(early_pay_data[1:].replace(',', '.')))
            except:
                early_career_pay.append(np.nan)
                
            try:
                mid_career_pay.append(float(mid_pay_data[1:].replace(',', '.')))
            except:
                mid_career_pay.append(np.nan)
            
            try:
                high_meaning.append(int(high_meaning_data[:-1]))
            except:
                high_meaning.append(np.nan)
    else:
        for k in range(1, 3):
            major_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[2]/span[2]').text
            early_pay_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[4]/span[2]').text
            mid_pay_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[5]/span[2]').text
            high_meaning_data = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody/tr[{k}]/td[6]/span[2]').text
            major.append(major_data)
            try:
                early_career_pay.append(float(early_pay_data[1:].replace(',', '.')))
            except:
                early_career_pay.append(np.nan)
                
            try:
                mid_career_pay.append(float(mid_pay_data[1:].replace(',', '.')))
            except:
                mid_career_pay.append(np.nan)
            
            try:
                high_meaning.append(int(high_meaning_data[:-1]))
            except:
                high_meaning.append(np.nan)

data = {
    "Major": major,
    "Early Career Pay": early_career_pay,
    "Mid-Career Pay": mid_career_pay,
    "% High Meaning": high_meaning
}


df = pd.DataFrame(data)
clean_df = df.dropna()
cleanest_df = clean_df.drop_duplicates(keep='first')
cleanest_df.to_csv('new_salaries_data.csv')