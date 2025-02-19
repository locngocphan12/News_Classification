import os
import shutil
import json

source_fol = 'D:/IMG_Categorical'

# destination_fol = 'D:/pythonProject/NewsClassification_MCAN/data/train/images'

# destination_fol = 'D:/pythonProject/NewsClassification_MCAN/data/dev/images'

destination_fol = 'D:/pythonProject/NewsClassification_MCAN/data/test/images'

os.makedirs(destination_fol, exist_ok=True)

# train_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'wseg_train_news.json')
# with open(train_path, 'r', encoding='utf-8') as f:
#   json_data_train = json.load(f)

# dev_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'wseg_dev_news.json')
# with open(dev_path, 'r', encoding='utf-8') as f:
#   json_data_dev = json.load(f)

test_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'wseg_test_news.json')
with open(test_path, 'r', encoding='utf-8') as f:
  json_data_test = json.load(f)


# images_list_train = []
# for doc_id, doc_content in json_data_train.items():
#     for img_path in doc_content['images']:
#         images_list_train.append(img_path['path'])
#
# for root, dirs, files in os.walk(source_fol):
#     for file in files:
#         if file in images_list_train:
#             source_path = os.path.join(root, file)
#             destination_path = os.path.join(destination_fol, file)
#             shutil.copy(source_path, destination_path)
#             print(f"Copied: {file} -> {destination_path}")
#
# print("Hoàn thành sao chép ảnh!")

# images_list_dev = []
# for doc_id, doc_content in json_data_dev.items():
#     for img_path in doc_content['images']:
#         images_list_dev.append(img_path['path'])
#
# for root, dirs, files in os.walk(source_fol):
#     for file in files:
#         if file in images_list_dev:
#             source_path = os.path.join(root, file)
#             destination_path = os.path.join(destination_fol, file)
#             shutil.copy(source_path, destination_path)
#             print(f"Copied: {file} -> {destination_path}")
#
# print("Hoàn thành sao chép ảnh!")

images_list_test = []
for doc_id, doc_content in json_data_test.items():
    for img_path in doc_content['images']:
        images_list_test.append(img_path['path'])

for root, dirs, files in os.walk(source_fol):
    for file in files:
        if file in images_list_test:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_fol, file)
            shutil.copy(source_path, destination_path)
            print(f"Copied: {file} -> {destination_path}")

print("Hoàn thành sao chép ảnh!")