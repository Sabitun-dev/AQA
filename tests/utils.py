from datetime import datetime, timedelta
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





def login(driver, wait, phone="911863162", password="1863162_sh"):
    inputs = wait.until(
        EC.presence_of_all_elements_located(
            (AppiumBy.CLASS_NAME, "android.widget.EditText")
        )
    )
    
    print(f"✅ Found {len(inputs)} input fields")
    
    # Enter credentials
    inputs[0].click()
    inputs[0].send_keys(phone)
    inputs[1].click()
    inputs[1].send_keys(password)
    
    # Click login button
    login_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "submit_auth_button")
        )
    )
    
    login_button.click()
    wait.until(
    EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("one_time_pickup")')
    )
)
    print("✅ Login is successful")




def select_one_time_pickup(driver, wait, menu_item="one_time_pickup"):
    menu_button = wait.until(
    EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{menu_item}")')
    )
)
    print(f"✅ {menu_item} menu item loaded")

    menu_button.click()
    print(f"🚀 {menu_item} menu item clicked")









def select_subscriptions(driver, wait, menu_item="subscriptions"):
    menu_button = wait.until(
    EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{menu_item}")')
    )
)
    print(f"✅ {menu_item} menu item loaded")

    menu_button.click()
    print(f"🚀 {menu_item} menu item clicked")







def select_settings(driver, wait, menu_item="settings"):
    menu_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{menu_item}")')
        )
    )
    print(f"✅ {menu_item} menu item loaded")

    menu_button.click()
    print(f"🚀 {menu_item} menu item clicked")



def add_order_button(driver, wait):
    add_order = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("add_order")')
        )
    )
    add_order.click()
    print("🚀 Add order button clicked")



def current_location_button(driver, wait):
    current_location = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("current_location")')
        )
    )
    current_location.click()
    print("🚀 Current location clicked")



def location_permission(driver, wait):
    # Handle "Turn on location" dialog (if appears)
    try:
        turn_on = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Turn on")')
            )
        )
        turn_on.click()
        print("✅ Location turned on")
    except:
        print("ℹ️ Location was already on")

    # Handle permission dialog
    try:
        allow_location = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            )
        )
        allow_location.click()
        print("✅ Location permission granted")
    except:
        print("ℹ️ Permission already granted")





def address_details(driver, wait):
    # Barcha EditText elementlarini kutib olish
    manzillar = wait.until(
        lambda d: d.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    )

    kvartira = manzillar[0]
    qavat = manzillar[1]
    kirish = manzillar[2]

    kvartira.click()
    kvartira.send_keys("12")

    qavat.click()
    qavat.send_keys("3")

    kirish.click()
    kirish.send_keys("A")

    print("✅ Address details entered")





    



def select_trash_type(driver, wait, trash_type="household"):
    # Find trash type buttons using semantic labels (language-independent)
    if trash_type == "household":
        button = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("household_waste")')
            )
        )
    elif trash_type == "commercial":
        button = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("non_residential_waste")')
            )
        )
    elif trash_type == "construction":
        button = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("construction_debris")')
            )
        )
    else:
        raise ValueError(f"Invalid trash_type: {trash_type}")
    
    button.click()
    print(f"🚀 {trash_type} trash type selected")


def scroll_one_screen_size(driver, wait):
    size = driver.get_window_size()
    start_x = size["width"] // 2
    start_y = int(size["height"] * 0.8)
    end_x = size["width"] // 2
    end_y = int(size["height"] * 0.2)
    driver.swipe(start_x, start_y, end_x, end_y, 700)





def open_date_picker(driver, wait):  
    date_picker = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("pickup_date")')
        )
    )
    date_picker.click()
    print("✅ Date field clicked")




def open_time_picker(driver, wait):
    time_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().descriptionContains("pickup_time"))')
    time_field.click()
    print("✅ Time field clicked")


def select_time(driver, wait, time):
    time_option = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    f'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().descriptionContains("{time}"))')
    time_option.click()
    print("✅ Time option selected")

#############################################################################################################################
############### SELECT DATE FUNCTIONS ###########################################
##############################################################################################################################################################################################################################################################################################
def get_tomorrow_date_label():
    """Get tomorrow's date in app's accessibility label format"""
    tomorrow = datetime.now() + timedelta(days=1)
    day = tomorrow.day
    weekday = tomorrow.strftime("%A")
    month = tomorrow.strftime("%B")
    year = tomorrow.year
    return f"{day}, {weekday}, {month} {day}, {year}"

def get_today_date_label():
    """Get today's date in app's accessibility label format"""
    today = datetime.now()
    day = today.day
    weekday = today.strftime("%A")
    month = today.strftime("%B")
    year = today.year
    return f"{day}, {weekday}, {month} {day}, {year}"

def get_yesterday_date_label():
    """Get yesterday's date in app's accessibility label format"""
    yesterday = datetime.now() - timedelta(days=1)
    day = yesterday.day
    weekday = yesterday.strftime("%A")
    month = yesterday.strftime("%B")
    year = yesterday.year
    return f"{day}, {weekday}, {month} {day}, {year}"

def select_tomorrow(driver, wait):
    """Select tomorrow's date and click OK"""
    target_date_label = get_tomorrow_date_label()
    print(f"🎯 Selecting tomorrow: {target_date_label}")
    
    # Select tomorrow (date picker should already be open)
    day_field = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, target_date_label)
        )
    )
    day_field.click()
    print("✅ Tomorrow selected")
    
    # Click OK
    ok_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "OK")
        )
    )
    ok_button.click()
    print("✅ OK button clicked")

def select_today(driver, wait):
    """Select today's date and click OK"""
    target_date_label = get_today_date_label()
    print(f"🎯 Selecting today: {target_date_label}")
    
    # Click date field
    date_field = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "01/11/2026")
        )
    )
    date_field.click()
    print("✅ Date field clicked")
    
    # Select today
    day_field = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, target_date_label)
        )
    )
    day_field.click()
    print("✅ Today selected")
    
    # Click OK
    ok_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "OK")
        )
    )
    ok_button.click()
    print("✅ OK button clicked")

def select_yesterday(driver, wait):
    """Select yesterday's date and click OK"""
    target_date_label = get_yesterday_date_label()
    print(f"🎯 Selecting yesterday: {target_date_label}")
    
    # Click date field
    date_field = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "01/11/2026")
        )
    )
    date_field.click()
    print("✅ Date field clicked")
    
    # Select yesterday
    day_field = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, target_date_label)
        )
    )
    day_field.click()
    print("✅ Yesterday selected")
    
    # Click OK
    ok_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "OK")
        )
    )
    ok_button.click()
    print("✅ OK button clicked")
