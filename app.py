# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

def create_csv(filename, headers):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

def add_row(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

# Define the filename for the CSV file
filename = 'data.csv'

# Define headers for the CSV file
headers = ['Company Name', 'Position', 'Location', 'Link']
# Create the CSV file with headers
create_csv(filename, headers)

myId = "email id"
myPassword = "pass"
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED')


def checkLoginState():   # Check if user is logged in
    try:
        isPresentt = driver.find_element(By.XPATH,"//button[@aria-label='Sign in']")
        print("isPresentt", isPresentt)
        isPresent = True;
    except:
        isPresent = False;
    return isPresent;
checkLoginState()
# time.sleep(3)
def Login():                # Login to sleepdata.org
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(myId)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(myPassword)
    driver.find_element(By.XPATH,"//button[@aria-label='Sign in']").click()
# Login()
# time.sleep(1000)
print(checkLoginState())
def goToNextPage():
    driver.find_element(By.XPATH,"//button[@aria-label='Next']").click()

def getData():
    print('📊📊📊📊📊')
    allPositions = driver.find_elements(By.XPATH, "//div[@class='mb1']/div[1]/div/span/span/a")
    allCompany = driver.find_elements(By.XPATH, "//div[@class='mb1']/div[2]")
    allLocations = driver.find_elements(By.XPATH, "//div[@class='mb1']/div[3]")
    # /div/div/span/span/a
    print('length', len(allPositions))
    data = []
    for i in range(10):
        # position = i.find_element(By.XPATH, "//div[1]")
        company = allCompany[i].text
        location = allLocations[i].text
        position = allPositions[i].text
        link = allPositions[i].get_attribute('href')
        add_row(filename, [company, position, location, link])
        print('📊📊📊📊📊', company, location, position, link)
#calling Login function if user is not logged in to sleepdata.org
if(checkLoginState()==False):
    print("Already logged in")
else:
    try:
        Login()
        print("Page is ready!")
        time.sleep(2)
        getData()
        for j in range(21):
            try: 
                goToNextPage()
                time.sleep(5)
                getData()
            except: 
                print("Error in going to next page")

    except TimeoutException:
        print ("Loading took too much time!")
    print("Logged in")








time.sleep(1000)
