import json
import datetime
import pytz


with open("export_uids.json", 'r',encoding='utf-8') as f:
    uid_data = json.load(f)

with open('user_data.json', 'r', encoding='utf-8') as f:
    user_vid_list = json.load(f)

video_dict = {}

user_with_no_vid_or_others_dict = {}

error_mids = []

# Create a mapping of mid to name
mid_to_name = {d['mid']: d['name'] for d in uid_data}

mid_to_tag = {d['mid']: d['tag'] for d in uid_data}

for i in user_vid_list:
    print(i)
    '''if i['user_vid']['data']['archives'] and i['user_vid']['data']['archives'][0] == True:
        newest_videoname = i['user_vid']['data']['archives'][0]['title']
        latest_pubtime_unix = i['user_vid']['data']['archives'][0]['pubdate']
        bvid = i['user_vid']['data']['archives'][0]['bvid']
        # Convert UNIX timestamp to a datetime object
        dt = datetime.datetime.utcfromtimestamp(latest_pubtime_unix)
        # Define the target timezone
        target_timezone = pytz.timezone('Asia/Shanghai')
        # Convert the datetime object to the target timezone
        latest_pubtime_localized = dt.replace(tzinfo=pytz.utc).astimezone(target_timezone)

        video_dict[i['mid']] = {
            'newest_videoname': newest_videoname,
            'latest_pubtime_unix': latest_pubtime_unix,
            'latest_pubtime_localized': latest_pubtime_localized,
            'bvid': bvid,
            'user_name': mid_to_name[i['mid']],
            'tag': mid_to_tag[i['mid']]
        }

    else:
        user_with_no_vid_or_others_dict[i['mid']] = {
            'user_name': mid_to_name[i['mid']],
            'tag': mid_to_tag[i['mid']]
        }'''


    try:
        newest_videoname = i['user_vid']['data']['archives'][0]['title']
        latest_pubtime_unix = i['user_vid']['data']['archives'][0]['pubdate']
        bvid = i['user_vid']['data']['archives'][0]['bvid']
        # Convert UNIX timestamp to a datetime object
        dt = datetime.datetime.utcfromtimestamp(latest_pubtime_unix)
        # Define the target timezone
        target_timezone = pytz.timezone('Asia/Shanghai')
        # Convert the datetime object to the target timezone
        latest_pubtime_localized = dt.replace(tzinfo=pytz.utc).astimezone(target_timezone)

        video_dict[i['mid']] = {
            'newest_videoname': newest_videoname,
            'latest_pubtime_unix': latest_pubtime_unix,
            'latest_pubtime_localized': latest_pubtime_localized,
            'bvid': bvid,
            'user_name': mid_to_name[i['mid']],
            'tag': mid_to_tag[i['mid']]
        }
    except IndexError:
        error_mids.append(i['mid'])
        print(f"Error occurred for mid: {error_mids}")

        try:
            user_with_no_vid_or_others_dict[i['mid']] = {
                'user_name': mid_to_name[i['mid']],
                'tag': mid_to_tag[i['mid']]
            }
        except KeyError:
            pass
    except KeyError:
        pass

print(video_dict)

print(f'error_mids = {error_mids}')

print(f'user_with_no_vid = {user_with_no_vid_or_others_dict}')

# Extract data and sort by 'latest_pubtime_unix'
sorted_videos = sorted(video_dict.items(), key=lambda x: x[1]['latest_pubtime_unix'])



total_users = []

users_with_novid = []

# Populate user lists
for mid, details in sorted_videos:
    user_info = {
        'UID': mid,
        '用户名': mid_to_name[mid],
        '最近更新': details['newest_videoname'],
        '視頻鏈接': f"https://www.bilibili.com/video/{details['bvid']}/",
        '日期': details['latest_pubtime_localized'].isoformat(),
        '時間戳': details['latest_pubtime_unix'],
        '分組': details['tag']

    }
    total_users.append(user_info)  # Add to total users list

for mid, details in user_with_no_vid_or_others_dict.items():
    user_info = {
        'UID': mid,
        '用户名': details['user_name'],
        '分組': details['tag']
    }
    users_with_novid.append(user_info)


filename='output.json'
results = {
    'normal_users': total_users,  # Include total users in the output
    'users_with_novid' : users_with_novid
}

print(json.dumps(results, ensure_ascii=False, indent=4))

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
