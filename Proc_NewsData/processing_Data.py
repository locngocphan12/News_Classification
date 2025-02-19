# Xoá \": \"Quỷ đỏ\"
# Xoá (Ảnh: .... ), Ảnh: .: Ảnh: Reuters.
# Xoá (......) - : ví dụ: (Dân Trí)

import re
import json
import os
def preprocess_text(text):
    # Remove source attributions like "Nguồn: ..." and "(Nguồn: ...)"
    patterns = [
        r'\(Nguồn\s*:\s*[^)]*\)\s*',      # (Nguồn: ...) with optional trailing space
        r'Nguồn\s*:\s*[^.\n]*',

        # Image attribution patterns
        r'\(Ảnh\s*minh\s*[hoạ|họa]+\s*:\s*[^)]+\)',  # (Ảnh minh hoạ: ...)
        r'Ảnh\s*minh\s*[hoạ|họa]+\s*:\s*[^.\n]*',  # Ảnh minh hoạ: ...
        r'\(Ảnh\s*:\s*[^)]+\)',  # (Ảnh: ...)
        r'Ảnh\s*:\s*[^.\n]*',  # Ảnh: ...
        r'ảnh\s*:\s*[^.\n]*'  # ảnh: ...
    ]

    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    # Strip leading and trailing whitespace
    text = text.strip()

    return text

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'test_news.json')
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

for i in json_data:
    for k in range(len(json_data[i]['images'])):
        json_data[i]['images'][k]['caption'] = re.sub(r"\(Dân trí\)\s*-?\s*", "", json_data[i]['images'][k]['caption'])
        json_data[i]['images'][k]['caption'] = json_data[i]['images'][k]['caption'].replace('\\', '')
        json_data[i]['images'][k]['caption'] = json_data[i]['images'][k]['caption'].replace('\"', '')
        json_data[i]['images'][k]['caption'] = preprocess_text(json_data[i]['images'][k]['caption'])
        # json_data[i]['images'][k]['caption'] = re.sub(r'\(?Ảnh: [^\)]+\)?\.?', '', json_data[i]['images'][k]['caption']).strip()
        # json_data[i]['images'][k]['caption'] = re.sub(r'\s+', ' ', json_data[i]['images'][k]['caption'])
        # json_data[i]['images'][k]['caption'] = re.sub(r'\(Ảnh minh [họa|hoạ]+: [^\)]+\)', '', json_data[i]['images'][k]['caption']).strip()
        # json_data[i]['images'][k]['caption'] = re.sub(r'\s+', ' ', json_data[i]['images'][k]['caption'])

    for j in range(len(json_data[i]['context'])):
        json_data[i]['context'][j] = re.sub(r"\(Dân trí\)\s*-?\s*", "", json_data[i]['context'][j])
        json_data[i]['context'][j] = json_data[i]['context'][j].replace('\\', '')
        json_data[i]['context'][j] = json_data[i]['context'][j].replace('\"', '')
        json_data[i]['context'][j] = preprocess_text(json_data[i]['context'][j])
        # json_data[i]['context'][j] = re.sub(r'\(?Ảnh: [^\)]+\)?\.?', '', json_data[i]['context'][j]).strip()
        # json_data[i]['context'][j] = re.sub(r'\s+', ' ', json_data[i]['context'][j])
        # json_data[i]['context'][j] = re.sub(r'\(Ảnh minh [họa|hoạ]+: [^\)]+\)', '', json_data[i]['context'][j]).strip()
        # json_data[i]['context'][j] = re.sub(r'\s+', ' ', json_data[i]['context'][j])

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'preprocess_test_news.json')
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

# import re
#
#
# def preprocess_text(text):
#     # Remove source attributions like "Nguồn: ..." and "(Nguồn: ...)"
#     patterns = [
#         r'\(Nguồn\s*:\s*[^)]*\)\s*',      # (Nguồn: ...) with optional trailing space
#         r'Nguồn\s*:\s*[^.\n]*',
#
#         # Image attribution patterns
#         r'\(Ảnh\s*minh\s*[hoạ|họa]+\s*:\s*[^)]+\)',  # (Ảnh minh hoạ: ...)
#         r'Ảnh\s*minh\s*[hoạ|họa]+\s*:\s*[^.\n]*',  # Ảnh minh hoạ: ...
#         r'\(Ảnh\s*:\s*[^)]+\)',  # (Ảnh: ...)
#         r'Ảnh\s*:\s*[^.\n]*',  # Ảnh: ...
#         r'ảnh\s*:\s*[^.\n]*'  # ảnh: ...
#     ]
#
#     for pattern in patterns:
#         text = re.sub(pattern, '', text, flags=re.IGNORECASE)
#
#     # Normalize whitespace
#     text = re.sub(r'\s+', ' ', text)
#
#     # Strip leading and trailing whitespace
#     text = text.strip()
#
#     return text
#
#
# # Test the function
# texts = [
#     "Bảng khảo sát giá vàng tuần tới của Kitco News. Nguồn: Kitco",
#     "Giá vàng thế giới chao đảo, tăng giảm liên tục trong bối cảnh sự bất định gia tăng trong cuộc đàm phán Mỹ-Trung. Tuy nhiên, nhìn chung sức cầu đối với vàng vẫn lớn. Ảnh minh họa: ST",
#     "Các khách hàng trúng giải tại Siêu thị Điện máy - Nội thất Chợ Lớn (Ảnh: Panasonic Việt Nam). ahfhds",
#     "Cảnh sát Giao thông Điện Biên ra quân cao điểm thực hiện kiểm tra, xử lý vi phạm về trật tự an toàn giao thông. Ảnh: Quang Anh",
#     "(Nguồn: VTV). Tin tức mới nhất về diễn biến kinh tế. (Nguồn: )",
#     "Báo cáo kinh tế (Nguồn: Bộ Tài chính) với nhiều thông tin quan trọng",
#     "Nguồn: Quang VInh"
# ]
#
# for text in texts:
#     print("Original:", text)
#     print("Processed:", preprocess_text(text))
#     print()