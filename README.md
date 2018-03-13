# BaiDuBaiKeSpider（Python2.7）
百度百科页面爬虫
## 使用方法
#### 1.命令行
```
cd baike_spider
python spider_main.py
```
#### 2.PyCharm
```
Open baike_spider
Run  'spider_main'
```
## 我遇到的问题
####1.地址问题
之前的地址[https://baike.baidu.com/view/10812319.htm](https://baike.baidu.com/view/10812319.htm)
现在的地址[https://baike.baidu.com/item/python/407313](https://baike.baidu.com/item/python/407313)

修改html_parser.py中的 
```
links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
```
改为
```
links = soup.find_all('a', href=re.compile(r"/item/*"))
```
  
#### 2.https问题
在spider_main中加上import ssl

#### 3.卡住不走，爬取几条就不动了
修改html_downloader.py,不明白的可以看我的代码
```
 try:
            response = urllib2.urlopen(url, timeout=10)
            if response.getcode() != 200:
                print 'false'
                return None
            print 'success'
        except:
            print 'timeout'
        return response.read()
```
#### 4. output.html一片空白
可以尝试删掉output.html文件重新运行（前提是程序可以正常运行），可以把1000改少一点查看效果
## 其他问题（继续补充 ）

## 架构
调度器->URL管理器->网页下载器->网页解析器->数据
## 用到的知识点
- set(),可选方案（MySQL, redis）
- urllib2
- BeautifulSoup，可选方案（正则表达式，html.parser,lxml)

## 联系我
QQ群：455285463
QQ：1185907688
微信：chaochao625121
