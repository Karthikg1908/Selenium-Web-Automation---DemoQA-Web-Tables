from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

def slow_down(seconds=2):
    time.sleep(seconds)

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.execute_script("""
    let iframe = document.querySelector("iframe[id^='google_ads_iframe']");
    if (iframe) { iframe.style.display = 'none'; }
""")
slow_down()

print("Adding a new record...")
add_btn = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
add_btn.click()
slow_down()

wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
driver.find_element(By.ID, "firstName").send_keys("Karthik")
driver.find_element(By.ID, "lastName").send_keys("G")
driver.find_element(By.ID, "userEmail").send_keys("karthikgr1908@gmail.com")
driver.find_element(By.ID, "age").send_keys("21")
driver.find_element(By.ID, "salary").send_keys("50000")
driver.find_element(By.ID, "department").send_keys("CSE")
slow_down()
driver.find_element(By.ID, "submit").click()
slow_down()

wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "rt-tbody"), "Karthik"))
rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
found = any("Karthik" in row.text and "G" in row.text for row in rows)
assert found, "Record not added"
print("Record added: Karthik G")
slow_down()

print("Editing the record...")
for row in driver.find_elements(By.CLASS_NAME, "rt-tr-group"):
    if "Karthik" in row.text and "G" in row.text:
        edit_btn = row.find_element(By.CSS_SELECTOR, "span[title='Edit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", edit_btn)
        edit_btn.click()
        break

wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
slow_down()
first_name_input = driver.find_element(By.ID, "firstName")
first_name_input.clear()
first_name_input.send_keys("Karthii")
slow_down()
driver.find_element(By.ID, "submit").click()
slow_down()

wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "rt-tbody"), "Karthii"))
rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
updated = any("Karthii" in row.text and "G" in row.text for row in rows)
assert updated, "Record not updated"
print("Record updated: Karthii G")
slow_down()

print("Deleting the record...")
rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
rows_before = len(rows)
deleted = False

for row in rows:
    try:
        if "Karthii" in row.text and "G" in row.text:
            delete_btn = row.find_element(By.CSS_SELECTOR, "span[title='Delete']")
            driver.execute_script("arguments[0].scrollIntoView(true);", delete_btn)
            delete_btn.click()
            deleted = True
            break
    except StaleElementReferenceException:
        continue

assert deleted, "Could not find the row to delete"
slow_down()
wait.until(lambda d: not any("Karthii" in row.text for row in d.find_elements(By.CLASS_NAME, "rt-tr-group")))

print("Record deleted successfully")
print("All CRUD operations completed successfully.")
driver.quit()
