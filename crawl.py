url = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-duong-pham-kiet-phuong-khue-my-prj-the-sang-residence/-cham-den-dinh-cao-ve-su-tinh-te-trong-so-huu-vinh-vien-view-bien-khe-dung-bo-qua-pr30762362'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

import requests

rs = requests.get(url, headers=headers)

print(rs)