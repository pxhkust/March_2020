import math
print(dir(math))




# def word_search(documents, keyword):
#     indexes = []
#     for i, doc in enumerate(documents):
#         tokens = doc.split()
#         normalized = [token.rstrip('.,') for token in tokens]
#         # print(normalized)
#         # print(keyword)
#         # print("-"*100)
#         if keyword in normalized:
#             indexes.append(i)
#     return indexes
#
#
# def multi_word_search_dic(documents, keywords):
#     multi_word_search_dic = {}
#     for keyword in keywords:
#         multi_word_search_dic[keyword] = word_search(documents, keyword)
#     return multi_word_search_dic
#
#
# doc_list1 = ["The Learn Python Challenge casino.", "they bought a car and a casino", "casino ville"]
# keywords1 = ["casino", "they"]
# result2 = multi_word_search_dic(doc_list1, keywords1)
# print("result", result2)
#
