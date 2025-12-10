import datetime
import os
import re
import ffmpeg
import cv2
import m3u8
import requests
from bs4 import BeautifulSoup
import pyshark
from selenium import webdriver
import signal
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
import numpy as np


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


def get_request(url):
    option = webdriver.ChromeOptions()
    option.add_argument('--auto-open-devtools-for-tabs')
    # 填入chromedriver路径
    driver = webdriver.Chrome(options=option,service=webdriver.chrome.service.Service(executable_path='D:/SomeThingsForProgrammer/chromedriver-win64/chromedriver.exe'))
    driver.get(url)
    time.sleep(5)
    scriptToExec="var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntriesByType('resource') || {}; return network;"
    netData = driver.execute_script(scriptToExec)
    driver.maximize_window()
    for item in netData:
        # print(item['name'])
        if re.match(r'^.*m3u8', item['name']):
            # print("found"+item['name'])
            m3u8_url = item['name']
            break
    print(m3u8_url)
    return m3u8_url

def temp_download_by_ffmpeg(m3u8_url):
    date = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    # cmd_command = "ffmpeg -i "+"\"" + m3u8_url +"\""+" -vcodec libx265" + " -c copy Video/"+date+".mp4"
    cmd_command = "ffmpeg -hwaccel cuda -i "+"\"" + m3u8_url +"\""+" -c:v libx265 -s 1920x1080" + " D:/Video/lubo/"+date+".mp4"
    print(cmd_command)
    os.system(cmd_command)
    # process = subprocess.Popen(cmd_command,shell=True)
    # command = input()
    # if(command == "stop"):
    #     process.send_signal(signal.SIGINT)
    #     print("wait")


def m3u8_video_decode(m3u8_url):
    # ts_url = m3u8_url
    # date = datetime.date.today().strftime("%Y-%m-%d")
    # ts_path = "Video/"+ date + ".ts"
    response = requests.get(m3u8_url)
    m3u8_obj = m3u8.loads(response.text)
    print(m3u8_obj)
    for line in response.text.split():
        print(line)
    temp_download_by_ffmpeg(m3u8_url)

    # for ts_file in ts_files:
    #     ts_response = requests.get(ts_file)
    #     if ts_response.status_code == 200:
    #         ts_data = np.frombuffer(ts_response.content, dtype=np.uint8)
    #         cap = cv2.VideoCapture(ts_file)
    #         if not cap.isOpened():
    #             print("Error opening video stream or file")
    #             continue
    #         while True:
    #             ret, frame = cap.read()
    #             if not ret:
    #                 break
    #             cv2.imshow('stream',frame)
    #             if cv2.waitKey(1) & 0xFF == ord('q'):
    #                 break
    #         cap.release()
    #         cv2.destroyAllWindows()
    #     else:
    #         print("无法下载ts文件"+ts_file)


# def change_encrypt():
# 录制完毕后转码可能会损坏部分画面(现版本已经在录播时指定编码)
# ffmpeg -i infile.mp4 -an -vcodec libx264 -crf 23 outfile.h264ffmpeg -i infile.mp4 -an -vcodec libx264 -crf 23 outfile.h264ffmpeg -i infile.mp4 -an -vcodec libx264 -crf 23 outfile.h264
if __name__ == '__main__':
    # 填入b站直播间url
    m3u8_video_decode(get_request('https://live.bilibili.com/1883942385?live_from=85001'))
    # 关注sonicandshadow谢谢喵修改为需要录播的直播间url

