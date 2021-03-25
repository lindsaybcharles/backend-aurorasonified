filenames = os.listdir('./Downloaded_data')
for i in range(len(filenames)):
    print(i)

if (i>0):
    for i in range(len(filenames)):
        os.remove('./Downloaded_data/'+ filenames[i])
        print("Deleted files: "+ filenames[i])
    print("Run Main Program")
else:
    print(filenames[i])
    print("Usable data found")



"""
Install geckodriver and add to path - for Firefox.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import os

def open_noaa(driver):
    """Opens the noaa url"""
    url_noaa = "https://www.swpc.noaa.gov/products/real-time-solar-wind"
    try:
        driver.get(url_noaa)
    except:
        print("Could not open url_noaa")


def press_by_id(driver, id):
    """Find and click element by id"""
    count = 0
    sleep_time = 1
    while count < 10:
        try:
            button = driver.find_element_by_id(id)
            button.click()
            return 0
        except:
            count += 1
            print(f"Could not find and click {id}. Try: {count}.")
            time.sleep(sleep_time)
    return 1

def create_driver(path_download, headless = True):
    """Create an instance of Firefox with appropriate options"""
    options = Options()
    options.headless = headless
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2) # Don't use standard download folder
    profile.set_preference("browser.download.dir", path_download) # Path to download destination
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain") # Don't prompt for download
    
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    return driver
    

def get_download_destination():
    """Just get relative path for download folder"""
    return os.path.abspath("./Downloaded_data")
    
def main():
    
    path_download = get_download_destination()
    driver = create_driver(path_download)

    id_timespan_button = "timespan-button"
    id_3days_timespan = "ui-id-9"
    id_save_button = "save_button"

    open_noaa(driver)
    press_by_id(driver, id_timespan_button)
    press_by_id(driver, id_3days_timespan)
    press_by_id(driver, id_save_button)

    # Make sure the file has time to download:
    time.sleep(20)
    driver.quit()
    print("Done")

main()

import numpy as np
import pandas as pd
import librosa
import datetime
import time
import os


filenames = os.listdir('./Downloaded_data')
for i in range(len(filenames)):
    print(i)
    

#os.rename(r'./Downloaded_data/'+ filenames[i]',r'./Downloaded_data/datafile +[i]')
#using the first 7 day downloaded txt file and converting to csv named as "for_csound"
#print(filename[i])
#a_file = open("./Data_csound/rtsw_plot_data_2021-01-27T00_00_00.txt", "r")


a_file = open('./Downloaded_data/'+ filenames[0], "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = ""
list_of_lines[1] = ""
list_of_lines[2] = ""
list_of_lines[3] = ""
list_of_lines[4] = ""
list_of_lines[5] = ""
list_of_lines[6] = ""
list_of_lines[7] = ""
list_of_lines[8] = ""
list_of_lines[9] = ""
list_of_lines[10] = ""
list_of_lines[11] = ""
list_of_lines[12] = ""
a_file = open("./Data_csound/for_csound.txt", "w")
a_file.writelines(list_of_lines)
a_file.close()

datafile = pd.read_fwf('./Data_csound/for_csound.txt')
datafile.to_csv('for_csound.csv')
datafile.rename( columns={'Unnamed: 1':'Time'}, inplace=True )
datafile['TimeStamp'] = datafile['Timestamp'] + " " + datafile['Time']
datafile['TimeStamp'] = pd.to_datetime(datafile['TimeStamp'], format='%Y-%m-%d %H:%M:%S')
datafile['Year'] = datafile['TimeStamp'].dt.year
datafile['Month'] = datafile['TimeStamp'].dt.month
datafile['Day'] = datafile['TimeStamp'].dt.day
datafile['Hour'] = datafile['TimeStamp'].dt.hour
datafile['Minute'] = datafile['TimeStamp'].dt.minute
datafile['Second'] = datafile['TimeStamp'].dt.second
datafile.pop("Timestamp")
datafile.pop('Time')
datafile.pop('Source')

for row in range(len(datafile)):
    for coloumn in range(34):
         if (datafile.iloc[row,coloumn] == -99999):
            datafile.iloc[row,coloumn] = datafile.iloc[row-1,coloumn] 
            
datafile.to_csv (r'./Data_csound/for_csound.csv', index = False, header=True)

#os.remove('./Downloaded_data/'+ filenames[i])
print("Deleted File"+filenames[i])

compare = pd.read_csv('./Data_csound/for_csound.csv')
year = compare['Year'].tail(1)
month = compare['Month'].tail(1)
day = compare['Day'].tail(1)
hour = compare['Hour'].tail(1)
minute = compare['Minute'].tail(1)
second = compare['Second'].tail(1)

split_date = pd.datetime(year,month,day,hour,minute,second)

for j in range(len(datafile)):
    if datafile.loc[j,'TimeStamp'] > split_date:
        df_newdata = datafile.loc[j:]
    else :
        df_newdata = datafile
        break 
        
frames = [compare, df_newdata]
result = pd.concat(frames)
result.to_csv (r'./Data_csound/for_csound.csv', index = False, header=True)
result
