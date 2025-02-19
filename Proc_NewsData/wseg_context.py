import py_vncorenlp
import json
import os
from tqdm import tqdm
def word_segmentation(json_data):
    segment_data = json_data.copy()
    wgsegment_model = py_vncorenlp.VnCoreNLP(save_dir='D:/pythonProject/vncorenlp', annotators=["wseg"])
    for doc_id, doc_content in tqdm(segment_data.items(), desc="Processing documents"):
        context = doc_content['context']
        processed_context = []
        for text in context:
            word_segmented = wgsegment_model.word_segment(text)
            processed_text = " ".join(word_segmented)
            processed_context.append(processed_text)
        doc_content['context'] = processed_context
    return segment_data
# word_segmented = wgsegment_model.word_segment(text)
# print(word_segmented)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'cleaned_train_news.json')
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data_train = json.load(json_file)

# file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'cleaned_dev_news.json')
# with open(file_path, 'r', encoding='utf-8') as json_file:
#     json_data_dev = json.load(json_file)
#
# file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'cleaned_test_news.json')
# with open(file_path, 'r', encoding='utf-8') as json_file:
#     json_data_test = json.load(json_file)

wseg_data_train = word_segmentation(json_data_train)

# wseg_data_dev = word_segmentation(json_data_dev)

# wseg_data_test = word_segmentation(json_data_test)
#
file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'wseg_train_news.json')
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(wseg_data_train, json_file, ensure_ascii=False, indent=4)
#
# file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'wseg_dev_news.json')
# with open(file_path, 'w', encoding='utf-8') as json_file:
#     json.dump(wseg_data_dev, json_file, ensure_ascii=False, indent=4)

# file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'wseg_test_news.json')
# with open(file_path, 'w', encoding='utf-8') as json_file:
#     json.dump(wseg_data_test, json_file, ensure_ascii=False, indent=4)


