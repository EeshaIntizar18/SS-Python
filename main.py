import driver as driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver= webdriver.Chrome("/home/lp-035/Downloads/chromedriver")

driver.set_page_load_timeout(10)
#maximize window
driver.maximize_window()

#Open url
driver.get("https://staging.sanasafinaz.com/uk")
time.sleep(10)
#Print title
print(driver.title)

#Search
#search= driver.find_element("xpath","/html/body/div[8]/header/div/div/div[2]/div[1]/div/div[2]/form")
#search.click()
#driver.set_page_load_timeout(3)
#search1= driver.find_element("xpath","/html/body/div[8]/header/div/div/div[2]/div[1]/div/div[2]/form/div[2]/div/input")
#search1.send_keys("heels")

#Click on accessories category
cat= driver.find_element("xpath","/html/body/div[8]/header/div/div/div[3]/div/div/div/div/nav/ul/li[8]/a")
cat.click()
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

#Click on product
product= driver.find_element("xpath","/html/body/div[8]/main/div/div[1]/div[5]/ol/li[1]/div/a/span/span/img")
product.click()
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

#Change Quantity
quantity= driver.find_element("xpath","/html/body/div[8]/main/div/div/div[2]/div[6]/form/div[2]/div/div/div[1]/div/input")
quantity.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
quantity.send_keys("3")
time.sleep(2)

#Click on add to cart
addcart= driver.find_element(By.ID,"product-addtocart-button")
addcart.click()
time.sleep(2)

#Click on cart button
cart= driver.find_element("xpath","/html/body/div[8]/header/div/div/div[2]/div[3]/a")
cart.click()
time.sleep(5)

#Increase Quantity
quantity= driver.find_element("xpath","/html/body/div[8]/main/div/div/div[3]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input")
quantity.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
quantity.send_keys("5")
time.sleep(1)

#Click on checkout button
checkout= driver.find_element("xpath","/html/body/div[8]/main/div/div/div[3]/div[1]/ul/li[1]/button")
checkout.click()
time.sleep(10)
driver.execute_script("window.scroll(0, 0);")

#Enter email
email= driver.find_element(By.ID,"customer-email")
email.send_keys("esha.intizar@rltsquare.com")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 500)")

#Enter firstname
firstname= driver.find_element(By.NAME,"firstname")
firstname.send_keys("Test")
time.sleep(1)

#Enter lastname
lastname= driver.find_element(By.NAME,"lastname")
lastname.send_keys("Test")
time.sleep(1)

#Enter Address
address= driver.find_element(By.NAME,"street[0]")
address.send_keys("test address")
time.sleep(2)
driver.execute_script("window.scrollTo(0,600)")
time.sleep(2)

#Enter province
province= driver.find_element(By.NAME,"region_id")
a=Select(province)
a.select_by_visible_text("Punjab")
time.sleep(2)

#Enter city
city= driver.find_element("xpath","/html/body/div[8]/main/div/div/div/div[4]/ol/li[1]/div[2]/form[2]/div/div[7]/div/select")
b=Select(city)
b.select_by_index(2)
time.sleep(1)

#Enter postal code
code= driver.find_element(By.NAME,"postcode")
code.send_keys("12345")
time.sleep(1)

#Enter phone number
num= driver.find_element(By.NAME,"telephone")
num.send_keys("3211111111")
time.sleep(1)

#Enter shipping method
shipping= driver.find_element("xpath","/html/body/div[8]/main/div/div/div/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button")
shipping.click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(6)

#Clcik on cod
cod= driver.find_element(By.ID,"cashondelivery")
cod.click()
time.sleep(2)

#Clcik on placeorder
order= driver.find_element("xpath","/html/body/div[9]/main/div/div/div/div[4]/ol/li[3]/div/form/fieldset/div[2]/div/div/div[6]/div[2]/div[4]/div/button")
order.click()
time.sleep(1)