


import jieba
import os
import re
import json


s = '我爱北京天安门'
r = jieba.cut(s)
print(list(r))

for i in r:
    print(i)

def cut_word():
    """
    分词
    :return:
    """

    filenames = os.listdir('章节')
    # print(filenames)
    data_words = {}

    for name in filenames[:]:
        with open(os.path.join('章节', name), 'r', encoding='utf8') as f:
            words = ''.join(re.findall('[\u4e00-\u9fa5]', f.read()))
            # print(words)

            for word in jieba.cut(words):
                print(word)
                if word in data_words:
                    data_words[word] += 1
                else:
                    data_words[word] = 1

    with open('分词信息结果', 'w') as f:
        json.dump(data_words, f)


def sorted_word():
    """
    统计
    :return:
    """

    with open('分词信息结果', 'r') as f:
        data_words = json.load(f)
        print(data_words)
        data_words = sorted(data_words.items(), key=lambda x:x[-1], reverse=True)
        for i in data_words:
            print(i)


if __name__ == '__main__':
    # cut_word()
    sorted_word()
    pass