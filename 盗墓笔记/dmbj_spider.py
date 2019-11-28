


import requests
import re
import os


html_dirname = 'html'
article_dirname = '章节'

if not os.path.exists(html_dirname):
    os.mkdir(html_dirname)
if not os.path.exists(article_dirname):
    os.mkdir(article_dirname)


def html_download():
    """
    下载章节页面
    :return:
    """

    for i in range(1, 9):

        r = requests.get('http://www.daomubiji.com/dao-mu-bi-ji-%s'%(i))
        html = r.content.decode()
        with open(html_dirname + '/盗墓笔记-%s.html'%(str(i).zfill(2)), 'w', encoding='utf8') as f:
            f.write(html)


def title_get(page):
    """
    提取章节信息
    :return:
    """

    with open(html_dirname + '/盗墓笔记-%s.html'%(str(page).zfill(2)), 'r', encoding='utf8') as f:
        text = f.read()
        complile = re.compile('<article .*?</article>', re.S)
        data = complile.findall(text)
        for line in data:
            print(line)
            title = re.findall('[\u4e00-\u9fa5]+', line)
            url = re.findall('href="(.*)">', line)
            with open('章节目录.txt', 'a', encoding='utf8') as f:
                f.write(' '.join(title) + '\t'+ url[0] + '\n')


def content_get(url, title):
    """
    获取正文内容
    :return:
    """

    r = requests.get(url)
    html = r.content.decode()
    article = re.findall('<article class="article-content">(.*)</article>', html, re.S)

    p_list = re.split('<p>|</p>', article[0])
    with open(article_dirname + '/%s.txt'%(title), 'w', encoding='utf8') as f:
        for line in p_list:
            line = line.strip()
            if line:
                print(line)
                f.write(line + '\n\n')


def main():
    """
    主函数
    :return:
    """

    with open('章节目录.txt', 'r', encoding='utf8') as f:
        for index, line in enumerate(f):
            print(line)
            if index >= 10:
                # break

                w_list = line.strip().split()
                url = w_list[-1]
                name = str(index).zfill(3) + '-'.join(w_list[:-1])
                content_get(url, name)


if __name__ == '__main__':
    # for i in range(1, 9):
    #     title_get(i)

    # content_get('http://www.daomubiji.com/qi-xing-lu-wang-01.html', '血尸')
    # main()
    pass
