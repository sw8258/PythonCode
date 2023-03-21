import requests
import re
from pyquery import PyQuery as pq 


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}



proxies = {"http":"http://222.95.241.44:3000",
           "https":"http://222.95.241.44:3000"}   

for i in range(0,62):
#目标网站复制下来
#https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92
	college_url = "https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=1&bsst=1&rsv_dl=news_b_pn&tn=news&word=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92&x_bfe_rqs=03E80&x_bfe_tjscore=0.500606&tngroupname=organic_news&newVideo=12&pn="+str(i*10)+"" #替换目标网址
	data = requests.get(college_url, headers=headers, proxies=proxies)
	#print(data.encode('gbk','ignore').decode('gbk')) 

	data.encoding = "utf-8"
	resove_college_url = data.text
	#print(resove_college_url.encode('gbk','ignore').decode('gbk'))


	# # #正则表达
	pat1 = '<h3 class="c-title">(.*?)<span class="c-info">'   
	rst1 = re.compile(pat1,re.S).findall(resove_college_url)
 	# print(len(rst1))

	for i in rst1:
		string1 = i
	
		text = pq(string1).text() 
        print(text.encode('gbk','ignore').decode('gbk')) 
		# # # # print (text)