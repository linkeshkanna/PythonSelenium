from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:/LEARNINGS/001.GITHUB.REPOSITORIES/PythonSelenium/Drivers/chromedriver.exe')
# driver = webdriver.Firefox(executable_path='D:/LEARNINGS/001.GITHUB.REPOSITORIES/PythonSelenium/Drivers/geckodriver.exe')
# driver = webdriver.Edge(executable_path='D:/LEARNINGS/001.GITHUB.REPOSITORIES/PythonSelenium/Drivers/msedgedriver.exe')
driver.get("http://demo.guru99.com/test/newtours/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
