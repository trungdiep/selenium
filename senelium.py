from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_location = "/usr/bin/chromedriver"

binary_location = "/usr/bin/google-chrome"

option = webdriver.ChromeOptions()
option.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=option)

driver.get("https://batdongsan.com.vn/ban-can-ho-chung-cu-duong-pham-kiet-phuong-khue-my-prj-the-sang-residence/-cham-den-dinh-cao-ve-su-tinh-te-trong-so-huu-vinh-vien-view-bien-khe-dung-bo-qua-pr30762362")

html = driver.find_element_by_tag_name('html')

# print(html.text)
with open('crawl.html', 'w+') as f:
    f.write(driver.page_source)