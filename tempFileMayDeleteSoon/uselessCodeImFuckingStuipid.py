#没用
# def element_test():
    # option = webdriver.ChromeOptions()
    # option.add_argument('--auto-open-devtools-for-tabs')
    # driver = webdriver.Chrome(options=option,service=webdriver.chrome.service.Service(executable_path='D:/SomeThingsForProgrammer/chromedriver-win64/chromedriver.exe'))
    # driver.get("https://live.bilibili.com/12723707?live_from=85001&spm_id_from=444.41.live_users.item.click")
    # time.sleep(3)
    # flag = driver.find_element(By.XPATH,"//li[text()=\"默认\"]")
    # script = "arguments[0].class="+flag.get_attribute("class")+""
    # path = driver.find_element(By.XPATH,"//li[text()=\"HEVC\"]")
    # driver.execute_script(script,path)
    # time.sleep(10)
    # print(flag.get_attribute("class"))