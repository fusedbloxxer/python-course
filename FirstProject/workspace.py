from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.cel.ro/index.php?main_page=login")


def send_text_to_input(name_of_input, text):
    name = driver.find_element_by_name(name_of_input)
    name.send_keys(text)


send_text_to_input("firstname", "Test")
send_text_to_input("lastname", "Test")
send_text_to_input("email_address", "random_email_224@yahoo.com")
send_text_to_input("telephone", "0720731327")
send_text_to_input("street_address", "Bucuresti")

county = driver.find_element_by_id("entry_suburb")
county.send_keys("Alba")

city = driver.find_element_by_id("city")
city.send_keys("Alba Iulia")

termeni = driver.find_element_by_name("termeni")
termeni.click()

termeni.submit()