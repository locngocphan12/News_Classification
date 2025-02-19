import pandas as pd
import random
import os
import json

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        df = json.load(json_file)
    return df

def create_json_file(file_path, df):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(df, json_file, ensure_ascii=False, indent=4)


# file_path = os.path.join('D:\pythonProject','datatestformat_4.json')
# df = load_json_file(file_path)

# train_df = {}
# dev_df = {}
# test_df = {}

file_path_train = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'train_news.json')
with open(file_path_train, 'r', encoding='utf-8') as json_file:
    train_df = json.load(json_file)

file_path_dev = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'dev_news.json')
with open(file_path_dev, 'r', encoding='utf-8') as json_file:
    dev_df = json.load(json_file)

file_path_test = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'test_news.json')
with open(file_path_test, 'r', encoding='utf-8') as json_file:
    test_df = json.load(json_file)

s1 = ['An sinh', 'Xã hội', 'Đời sống'] # 2000 450
s2 = ['Bất động sản'] # 70 12
s3 = ['Tin tức', 'Nhân ái', 'Cần biết', 'Thời sự'] # 840 190
s4 = ['Công đoàn'] # 1200 280
s5 = ['Công nghệ', 'Số hóa', 'Công nghệ - Game', 'Sức mạnh số'] # 500 100
s6 = ['Du lịch'] # 270 60
s7 = ['Giải trí', 'Thư giãn'] # 600 120
s8 = ['Giáo dục', 'Giáo dục pháp luật'] # 70 13
s9 = ['Giới trẻ'] # 80 15
s10 = ['Khoa học'] # 38 7
s11 = ['Kinh doanh', 'Kinh tế'] # 1700 400
s12 = ['Việc làm'] # 85 17
s13 = ['Pháp luật'] # 500 100
s14 = ['Sức khỏe', 'Tình yêu'] # 400 80
s15 = ['Xe', 'Xe ++'] # 250 50
s16 = ['Thế giới'] # 620 120
s17 = ['Văn hóa', 'Văn hoá - Giải trí', 'Thể thao'] # 3300 700
s18 = ['Tiêu dùng'] # 64 13
file_path = os.path.join('D:\\pythonProject\\Newspapers_Data', 's18.json')
json_data = load_json_file(file_path)
#Kích thước tập train
n = 64
selected_samples_train = random.sample(list(json_data), n)
print(len(selected_samples_train))

remaining_data = [item for item in list(json_data) if item not in selected_samples_train]
#Kích thước tập dev
n_1 = 13
# n_1 = int(round(len(remaining_data) / 2))
remaining_data_dev = random.sample(remaining_data, n_1)
# Còn lại
remaining_data4test = [item for item in remaining_data if item not in remaining_data_dev]
remaining_data_test = random.sample(remaining_data4test, n_1)
# remaining_data_test = [item for item in remaining_data if item not in remaining_data_dev]
print(len(selected_samples_train),' ',len(remaining_data_dev), ' ', len(remaining_data_test))

for i in selected_samples_train:
    train_df[i] = json_data[i]
    train_df[i]['section'] = 'Tiêu dùng'
for i in remaining_data_dev:
    dev_df[i] = json_data[i]
    dev_df[i]['section'] = 'Tiêu dùng'
for i in remaining_data_test:
    test_df[i] = json_data[i]
    test_df[i]['section'] = 'Tiêu dùng'

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'train_news.json')
create_json_file(file_path, train_df)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'dev_news.json')
create_json_file(file_path, dev_df)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'test_news.json')
create_json_file(file_path, test_df)
