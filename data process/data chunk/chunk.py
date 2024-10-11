import json
from langchain.text_splitter import NLTKTextSplitter
def chunk3(text):
    # 重新组合句子，实现重叠效果
    new_sentences = []
    for i in range(len(text) - 2):  # 确保至少有三句话
        new_sentence = " ".join(text[i:i+3])
        new_sentences.append(new_sentence)
    print('new_sentences  ',len(new_sentences))
    return new_sentences
def chunk(text):
    allchunk=[]
    allchunkdoc3=[]
    text_splitter = NLTKTextSplitter()
    # 使用 NLTKTextSplitter 对象分割文本
    docs = text_splitter.split_text(text)
    # 将分割后的文档列表转换为句子列表
    chunk1 = [sentence.strip() for doc in docs for sentence in doc.split('\n') if sentence.strip()]
    if len(chunk1) > 3:
        allchunkdoc3=chunk3(chunk1)
    print('chunk1  ',len(chunk1))
    print('allchunkdoc3  ',len(allchunkdoc3))
    allchunk=chunk1+allchunkdoc3
    print('allchunk  ',len(allchunk))
    return allchunk

with open("ADE/suoyou.json", 'r', encoding='utf-8') as file:
    # 使用json模块的load函数解析JSON数据
    data = json.load(file)




zuizhong=[]
num=0
for i in data:
    print(num)
    num+=1
    id=i['id']
    token=i['token']
    chunkdoc=chunk(token)
    for j in chunkdoc:
        iiii={'id':id,'token':j}
        zuizhong.append(iiii)
print(zuizhong)
zuizhong=zuizhong+data

with open('ADE/allabschunk.json', 'w', encoding='utf-8') as file:
    # 使用json.dump()将数据写入文件，indent参数用于美化输出，使其更易读
    json.dump(zuizhong, file, indent=4, ensure_ascii=False)


from operator import itemgetter
sorted_data = sorted_data = sorted(zuizhong, key=lambda x: int(x['id']))

# 打印排序后的JSON数据
print(json.dumps(sorted_data, indent=4, ensure_ascii=False))

with open('ADE/allabschunkrank.json', 'w', encoding='utf-8') as file:
    # 使用json.dump()将数据写入文件，indent参数用于美化输出，使其更易读
    json.dump(sorted_data, file, indent=4, ensure_ascii=False)

def paixu(data1):
    last_id = None
    i = 0
    # 遍历文档列表并更新id
    for doc in data1:

        #base_id = doc['id'].split('.')[0]
        base_id = doc['id']
        # 如果是第一个id或者当前id与上一个id不同，更新编号
        if last_id is None or base_id != last_id:
            last_id = base_id
            i = 0
            next_id = f"{base_id}.{i}"
        else:
            # 否则递增编号
            i += 1
            next_id = f"{base_id}.{i}"

        # 更新id
        doc['id'] = next_id

    # 打印更新后的JSON数据
    #print(json.dumps(data1, indent=4, ensure_ascii=False))
    return data1
dataaaa=paixu(sorted_data)
with open('ADE/allabschunkok.json', 'w', encoding='utf-8') as file:
    # 使用json.dump()将数据写入文件，indent参数用于美化输出，使其更易读
    json.dump(dataaaa, file, indent=4, ensure_ascii=False)