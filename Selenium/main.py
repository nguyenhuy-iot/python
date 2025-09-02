import time
import tkinter as tk
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = None  # Global variable to manage the browser
# URL = "https://www.google.com/?hl=vi"
URL = "https://tradestation.fireant.vn/charts"

def open_browser():
    global driver
    if driver is None:  # Only open if not already opened
        driver = webdriver.Chrome()
        driver.get(URL)
        label.config(text="Browser opened")
        driver.save_screenshot("screenshot.png")
         # Wait a bit for page to load
        # time.sleep(3)

        # driver.save_screenshot("screenshot.png")

        try:
            # Wait until the button with text "Để sau" is clickable
            wait = WebDriverWait(driver, 10)
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Để sau']]"))
            )
            btn.click()
            print("Clicked 'Để sau' button!")
            time.sleep(2)

            driver.save_screenshot("screenshot1.png")

            # # Take screenshot after click
            # filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
            # driver.save_screenshot(filename)
            # print(f"Screenshot saved: {filename}")

        except Exception as e:
            print("Button 'Để sau' not found:", e)

         # Log page source
        # print("=== Page Source ===")
        # print(driver.page_source) 
        # print("===================")
    else:
        label.config(text="Browser is already opened!")


def close_browser():
    global driver
    if driver:
        driver.quit()
        driver = None
        label.config(text="Browser closed")
    else:
        label.config(text="No browser to close")


def keep_on_top():
    """Force Tkinter window to stay on top"""
    window.attributes("-topmost", True)
    window.lift()
    window.focus_force()


# Create Tkinter window
window = tk.Tk()
window.title("Selenium + Tkinter Demo")
window.geometry("300x200")

# Always on top
keep_on_top()

label = tk.Label(window, text="No browser opened yet", font=("Arial", 14))
label.pack(pady=20)

open_button = tk.Button(window, text="Open Browser",
                        command=lambda: threading.Thread(target=open_browser, daemon=True).start())
open_button.pack(pady=5)

close_button = tk.Button(window, text="Close Browser", command=close_browser)
close_button.pack(pady=5)

window.mainloop()
