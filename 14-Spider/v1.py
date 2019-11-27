from urllib import request

'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''


if __name__ == '__main__':

    url = "https://e-hentai.org"
    url = "https://www.bilibili.com"
    # 打开相应url并把相应页面作为返回
    response = request.urlopen(url, headers={'User-Agent': 'Mozilla/5.0'})

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = response.read()
    print(type(html))

    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode("utf-8")

    print(html)
