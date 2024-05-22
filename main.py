from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://maps.app.goo.gl/JagPjjA2QKbkvZ278"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:\\Users\\bkurt\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(options=options)

driver.get(URL)
time.sleep(3)

# title of the list
the_title = driver.find_element(By.CSS_SELECTOR, value=".L1xEbb .fontTitleLarge").text

# number of places
places_count = int(driver.find_element(By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/h2').text.split(" ")[2])

# titles = driver.find_elements(By.CSS_SELECTOR, value=".fontHeadlineSmall")

options_button = driver.find_element(By.CSS_SELECTOR, value=".e7e4sc")
options_button.click()
time.sleep(5)
edit_list_button = driver.find_element(By.CSS_SELECTOR, value=".fxNQSd")
edit_list_button.click()
time.sleep(7)

list_div = driver.find_element(By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
list_div.click()

# getting the number of places
time.sleep(4)
print(f"Num of places: {places_count}")

if places_count > 20 and places_count % 20 != 0:
    times_to_scroll = int(places_count / 20) + 1
elif places_count > 20 and places_count % 20 == 0:
    times_to_scroll = int(places_count / 20)

for it in range(0, times_to_scroll):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list_div)
    time.sleep(5)

everything = driver.find_elements(By.CSS_SELECTOR, value=".nvZPbe")
placeholders = driver.find_elements(By.CSS_SELECTOR, value=".BmGZWb")

# for item in everything:
#     print(f"{item.text}\n")

for item in everything:
    text = item.text
    print(f"{text}\n")
    # num = everything.index(item)
    # print(f"{num}. {text}\n")



