import json
import os
file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'preprocess_train_news.json')
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data_train = json.load(json_file)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'preprocess_dev_news.json')
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data_dev = json.load(json_file)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'preprocess_test_news.json')
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data_test = json.load(json_file)

def clean_empty_captions(data):
    """
    Remove images with empty captions from the images list in each document
    and remove documents with empty images lists

    Args:
        data (dict): JSON data containing documents with images lists

    Returns:
        dict: Cleaned data with empty caption images and empty image list documents removed
    """
    cleaned_data = data.copy()
    ids_to_remove = []

    for doc_id, doc_content in cleaned_data.items():
        if "images" in doc_content:
            # Filter out images with empty captions
            doc_content["images"] = [
                img for img in doc_content["images"]
                if img.get("caption") and img["caption"].strip() not in ("", ".")
            ]

            # If images list is empty after cleaning, mark this ID for removal
            if not doc_content["images"]:
                ids_to_remove.append(doc_id)

    # Remove all marked IDs
    for doc_id in ids_to_remove:
        del cleaned_data[doc_id]

    return cleaned_data


cleaned_data_train = clean_empty_captions(json_data_train)
cleaned_data_dev = clean_empty_captions(json_data_dev)
cleaned_data_test = clean_empty_captions(json_data_test)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\train', 'cleaned_train_news.json')
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(cleaned_data_train, json_file, ensure_ascii=False, indent=4)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\dev', 'cleaned_dev_news.json')
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(cleaned_data_dev, json_file, ensure_ascii=False, indent=4)

file_path = os.path.join('D:\\pythonProject\\NewsClassification_MCAN\\data\\test', 'cleaned_test_news.json')
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(cleaned_data_test, json_file, ensure_ascii=False, indent=4)


