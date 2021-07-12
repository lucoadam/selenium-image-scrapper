from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C://Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe',chrome_options=options)

driver.get('http://localhost:8080')
driver.save_screenshot("screenshots/shot1.png")
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[2]/div/div[3]/a[1]").click()
driver.save_screenshot("screenshots/shot2.png")
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[1]/div/div[1]/div/input").send_keys("super@user.com")
driver.save_screenshot("screenshots/shot3.png")
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[2]/div/div/div/input").send_keys("Super.admin")
driver.save_screenshot("screenshots/shot4.png")
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/form/button").click()
driver.save_screenshot("screenshots/shot5.png")
# driver.find_element_by_xpath("/html/body/div/div/div/div/nav/div[1]/div[2]/a[3]").click()
import time
time.sleep(2)
driver.execute_script("window.location.href='/admin/properties';")

time.sleep(2)
driver.save_screenshot("screenshots/shot6.png")
driver.execute_script("window.location.href='/admin/properties/create'")
time.sleep(2)
driver.save_screenshot("screenshots/shot7.png")
# driver.close()