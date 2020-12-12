import urllib.request as req
#url="https://www.ptt.cc/bbs/movie/index.html"
url="https://www.facebook.com/"
request=req.Request(url,headers={
"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
})
with req.urlopen(request) as response:
	data=response.read().decode("utf-8")
print(data)

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
	print(title)
	if title.a != None:
		print(title.a.string)