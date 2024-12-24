import json
import datetime

# Get the current date
current_date = datetime.datetime.now()

# Define a list to hold users who haven't updated in over a year
inactive_users = []

with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Determine the timestamp for one year ago
one_year_ago = int((datetime.datetime.now() - datetime.timedelta(days=365)).timestamp())

# Identify inactive users
inactive_users = [
     user for user in data["normal_users"] if user["時間戳"] < one_year_ago
]


for i in data['users_with_novid']:
    inactive_users.append(i)



# Filter items with the tag '特别关注' in '分組'
items_with_special_attention = [item for item in inactive_users if '特别关注' in item['分組']]


# Filter items with no tags in '分組'
items_without_tags = [item for item in inactive_users if not item['分組']]

items_without_tags_uids = []

# Display the filtered items
for item in items_without_tags:
    print(item)
    items_without_tags_uids.append(item['UID'])


print(items_without_tags_uids)
print(len(items_without_tags_uids))
print(len(inactive_users))


with open('inactive_users.txt','w',encoding='utf-8') as f:
    for i in items_without_tags_uids:
        f.write(str(i)+',')


total_users = data['normal_users']
total_users.extend(data['users_with_novid'])

#print(total_users)

print(len(total_users))



# Finding the missing UIDs

'''total_users_uids = [user['UID'] for user in total_users]

with open("export_uids.json", "r", encoding="utf-8") as f:
    data = json.load(f)

mids_to_check = [d['mid'] for d in data]

# Find UIDs not in the data
missing_uids = [uid for uid in mids_to_check if uid not in total_users_uids] # Display the missing UIDs
print("Missing UIDs:", missing_uids)'''