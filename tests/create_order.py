from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.appiumby import AppiumBy


app_path = r"C:\Users\user\Employify\build\app\outputs\flutter-apk\app-debug.apk"

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.app = app_path
options.automation_name = "UiAutomator2"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 20)

print("✅App launched")


utils.login(driver, wait, phone="911863162", password="1863162_sh")
utils.select_one_time_pickup(driver, wait)
utils.add_order_button(driver, wait)
utils.current_location_button(driver, wait)
utils.location_permission(driver, wait)
utils.address_details(driver, wait)

try:
    driver.hide_keyboard()
except:
    driver.back()
time.sleep(2)

utils.select_trash_type(driver, wait, trash_type="commercial")
utils.scroll_one_screen_size(driver, wait)
utils.open_date_picker(driver, wait)
utils.get_tomorrow_date_label()
utils.select_tomorrow(driver, wait)

time.sleep(2)
driver.back()
time.sleep(2)

utils.scroll_one_screen_size(driver, wait)
utils.open_time_picker(driver, wait)
utils.select_time(driver, wait, time="17:00 - 19:00")

finish = driver.find_element(
    AppiumBy.XPATH, 
    "//android.view.View[@content-desc='Tashish Buyurtmasi Yaratish' and @clickable='true']"
)
finish.click()
print("Order creation finished")

time.sleep(20)
driver.quit()

print("Test finished successfully")
