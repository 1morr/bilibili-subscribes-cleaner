import json
from functools import reduce
from hashlib import md5
import urllib.parse
import time
import requests
import datetime
import pytz
from tqdm import tqdm




headers = {
    'authority': 'api.vc.bilibili.com', 'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://message.bilibili.com', 'referer': 'https://message.bilibili.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
}

with open("export_uids.json", "r", encoding="utf-8") as f:
    data = json.load(f)




video_dict = {}

# Convert data into mids
mids = [d['mid'] for d in data]

# Create a mapping of mid to name
mid_to_name = {d['mid']: d['name'] for d in data}

user_vid_list = []

for mid in tqdm(mids, desc="Fetching videos", unit="mid"):
    user_vid = requests.get("https://api.bilibili.com/x/series/recArchivesByKeywords", headers=headers,
                            params={'mid': mid, 'keywords': '', 'orderby': 'senddate'}).json()
    print(user_vid)
    # Create a new dictionary for each entry
    entry = {
        'mid': mid,
        'user_vid': user_vid
    }

    user_vid_list.append(entry)  # Append the entry to the list

    time.sleep(1)

# Save the dictionary to a JSON file
with open("user_data.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(user_vid_list, ensure_ascii=False, indent=4))





