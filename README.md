# bilibili-subscribes-cleaner
找出超過一年未有更新的用戶並導出他們的uid

使用以下的油猴插件來導出你所關注的用戶
<https://greasyfork.org/zh-TW/scripts/428895-bilibili-%E5%85%B3%E6%B3%A8%E7%AE%A1%E7%90%86%E5%99%A8>

將導出的文件放進目錄裏後執行getting_user_data.py便可以找出用戶的最後更新時間和其他資料然後保存為user_data.json

使用formating_output.py便可以將得到的數據格式化然後保存為output.json方便後續使用

最後使用identify_inactive_users.py便可以找到最近一年沒有更新的用戶然後導出他們的uid為inactive_users.txt

然後便可以使用油猴插件一鍵取關
