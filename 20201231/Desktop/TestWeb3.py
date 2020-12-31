# import urllib.request as req
# #url="https://www.ptt.cc/bbs/movie/index.html"
# url="https://www.facebook.com/"
# request=req.Request(url,headers={
# "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# })
# with req.urlopen(request) as response:
# 	data=response.read().decode("utf-8")
# print(data)

# import bs4
# root=bs4.BeautifulSoup(data, "html.parser")
# titles=root.find_all("div",class_="title")
# for title in titles:
# 	print(title)
# 	if title.a != None:
# 		print(title.a.string)
import re

regex = r"\d*\S[/][箱]"

test_str = ("8包/袋\n")

matches = re.search(regex, test_str)

if matches:
	print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
	
	for groupNum in range(0, len(matches.groups())):
		groupNum = groupNum + 1
		
		print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))