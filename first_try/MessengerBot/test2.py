from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\lucas\Desktop\chromedriver.exe")
driver.get("https://www.kubii.fr/")
print(driver.find_element_by_id("search_query_top"))