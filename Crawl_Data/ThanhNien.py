from bs4 import BeautifulSoup
import requests
import os
import json
data_frame = {}
#file_path = os.path.join('D:\pythonProject\ThanhNien','thoi-sup.json')
#with open(file_path, 'r', encoding='utf-8') as json_file:
    #data_frame = json.load(json_file)
def Get_Content_Img_Cap(link, page_content, page_img, page_cap):
    link_text = requests.get(link).text
    link_soup = BeautifulSoup(link_text, "html.parser")
    tieu_de = link_soup.find('h2', class_='detail-sapo')
    if (tieu_de!=None):
        content = tieu_de.text.strip()
        page_content.append(content)
    main_content = link_soup.find('div', class_='detail-cmain')
    if main_content!=None:
        list_para = main_content.find('div', class_ = 'detail-content afcbc-body')
        if list_para != None:
            paragraphs = list_para.find_all(['p','h2'], recursive=False)
            img_caps = list_para.find_all('figure')
            print(img_caps)
            if paragraphs !=None:
                for p in paragraphs:
                    content = p.text.strip()
                    page_content.append(content)
            if (img_caps!=None):
                for img_cap in img_caps:
                    img = img_cap.find('img', attrs = {'src':True})
                    cap = img_cap.find('figcaption')
                    if (img != None and cap != None):
                        page_img.append(img['src'])
                        page_cap.append(cap.text.strip())

def Create_Data_frame(link, page_content, page_img, page_cap, muc, linh_vuc, ten_json_file):
    url = link
    data_frame[url] = {}
    data_frame[url]["context"] = page_content
    data_frame[url]["images"] = []
    cnt = 0
    for img in page_img:
        data_frame[url]["images"].append({"url_img": img, "caption": page_cap[cnt]})
        cnt += 1
    data_frame[url]["section"] = muc
    data_frame[url]["subsection"] = linh_vuc
    file_path = os.path.join('D:\pythonProject\ThanhNien', f'{ten_json_file}p.json')
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_frame, json_file, ensure_ascii=False, indent=4)
def Create_Data(link, ten_json_file, muc, linh_vuc):
    page_content = []
    page_img = []
    page_cap = []
    # =====================================================================
    Get_Content_Img_Cap(link, page_content, page_img, page_cap)
    # =====================================================================
    if (page_img != []):
        Create_Data_frame(link, page_content, page_img, page_cap, muc,
                          linh_vuc, ten_json_file)

file_path = os.path.join('D:\pythonProject\ThanhNien','kinh-te.json')
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
#20000

for i in range(0,len(json_data)):

    print(i, ' ',json_data[i]['Field1_links'])
    if json_data[i]['Field1_links'] == '':
        continue
    checklv = json_data[i]['Field2']
    if ('kinh-te-xanh' in checklv):
        linh_vuc = 'Kinh tế xanh'
    elif ('chinh-sach-phat-trien' in checklv):
        linh_vuc = 'Chính sách - Phát triển'
    elif ('ngan-hang' in checklv):
        linh_vuc = 'Ngân hàng'
    elif ('chung-khoan' in checklv):
        linh_vuc = 'Chứng khoán'
    elif ('doanh-nghiep' in checklv):
        linh_vuc = 'Doanh nghiệp'
    elif ('khat-vong-viet-nam' in checklv):
        linh_vuc = 'Khát vọng Việt Nam'
    elif ('lam-giau' in checklv):
        linh_vuc = 'Làm giàu'
    elif ('dia-oc' in checklv):
        linh_vuc = 'Địa ốc'
    #elif ('thoi-luan' in checklv):
        #linh_vuc = 'Thời luận'
    print(linh_vuc)

    Create_Data(json_data[i]['Field1_links'],'kinh-te','Kinh tế',linh_vuc)