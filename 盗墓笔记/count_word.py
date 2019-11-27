
import os
import re


def count_word():
    """
    统计总字数
    :return:
    """
    dirname = '章节'

    filenames = os.listdir('章节')
    count = 0
    for name in filenames[:]:

        with open(os.path.join(dirname, name), 'r', encoding='utf8') as f:
            words = re.findall('[\u4e00-\u9fa5]', f.read())
            count += len(words)

    return count


if __name__ == '__main__':
    print(count_word())
    pass