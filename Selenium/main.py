# main.py
# Main file to run the Selenium project

from selenium import webdriver

if __name__ == "__main__":
    # Create a new Chrome browser instance (chromedriver.exe must be in the same folder or in PATH)
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()
