#获取图片链接地址
#读取HTML文件内容，返回一个列表
def getHTMLlines(htmlpath):
    ls = open(htmlpath,"r",encoding="utf-8")
    lines = ls.readlines()
    ls.close()
    return lines

#用于解析文件并提取图像的URL
def extractImageUrls(htmllist):
    url = []
    for line in htmllist:
        if "img" in line:
            http = line.split("src=")[-1].split('"')[1]
            if 'http' in http:
                url.append(http)
    return url

#将获取的链接输出到屏幕上
def showResults(urls):
    count = 1
    for url in urls:
        print("第{:2}个URL:{}".format(count,url))
        count += 1

# 主程序：1 读取文件；2 解析并提取其中的图片链接；3 输出提取结果到屏幕
def main():
    f = getHTMLlines("./files/ngchina.html")
    urls = extractImageUrls(f)
    showResults(urls)

main()
