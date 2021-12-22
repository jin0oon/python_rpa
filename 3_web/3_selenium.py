from selenium import webdriver
import time
# driver = webdriver.Chrome("./chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

# 이미지 아이콘 클릭
driver.find_element_by_xpath('//*[@id="sbtc"]/div[2]/div[3]/div[2]').click()

# '이미지 업로드 중' 클릭
driver.find_element_by_xpath('//*[@id="dRSWfb"]/div/a').click()

# 파일 선택 클릭
driver.find_element_by_xpath('//*[@id="awyMjb"]').click()
time.sleep(1)

# 내 컴퓨터 파일구조에 어떻게 접근?

# list_raw = driver.find_element_by_
