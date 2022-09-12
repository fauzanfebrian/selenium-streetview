from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver.exe')
first = True

try:
    while(True):
        latlong = input("Enter lat long: ")
        uristreet =f"http://maps.google.com/maps?q=&layer=c&cbll={latlong}"
        urimap = f"http://maps.google.com/maps?q={latlong}"
        
        if first:
            first = False
        else:
            driver.close()
            driver.switch_to.window(base_window)
        
        driver.get(urimap)
        base_window = driver.current_window_handle
        driver.execute_script("window.open('about:blank', 'secondtab');")
        driver.switch_to.window("secondtab")
        driver.get(uristreet)
except KeyboardInterrupt:
    print("SANGAT MEMBANTU BUKAN")

