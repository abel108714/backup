print('hi')
s = '東森未入績效 mm/dd止 #,###'
pos_title = s.find('東森未入績效')
pos_date_m = s.find('/')
pos_date_d = s.find('止')
pos_amount = s.find('#,###')
if pos_title >= 0:
	print('有找到: 在'+ str(pos_title))

else:
    print('找不到')



if pos_date_m >= 0: 
    print('有找到: 在'+ str(pos_date_m))
else:
    print('找不到')


if pos_date_d >= 0: 
    print('有找到: 在'+ str(pos_date_d))
else:
    print('找不到')

if pos_amount >= 0: 
    print('有找到: 在'+ str(pos_amount))
else:
    print('找不到')

import re

#@昱慧 @立修 東森未入績效 10/21止3,069,200  請更新
#email4 = re.compile(r'\W*[@]?\w*\W*[@]?\w*\W*[東][森][未][入][績][效]\W*\d*[/]\d*[止]\d*[,]?\d*[,]?\d*\D*')
#match = email4.match('@昱慧 @立修 東森未入績效 10/21止3,069,200  請更新').group(0)
#print(match)
#match = next(re.finditer(r'[0-9]+[,]?[0-9]+[,]?[0-9]+[,]?[0-9]+', email4)).group(0)
#print(match)


regex = r"\W*[@]?\w*\W*[@]?\w*\W*[東][森][未][入][績][效]\W*\d*[/]\d*[止]\d*[,]?\d*[,]?\d*\D*"
expected_perf_str = ("@昱慧 @立修 東森未入績效 9/21止3069200\n\n")
matches = re.search(regex, expected_perf_str)
if matches:#訊息
    match = matches.group()
    print(match)
    title_regex = r"\w*[東][森]\W*"
    title_matches = re.search(title_regex, expected_perf_str)
    if title_matches:#標題
        title_match = title_matches.group()
        print(title_match)
    date_regex = r"\d*[/]\d*\W*"
    date_matches = re.search(date_regex, expected_perf_str)
    if date_matches:#日期
        date_match = date_matches.group()
        print(date_match)
    amount_regex = r"[0-9]+[,]?[0-9]+[,]?[0-9]+[,]?[0-9]+"
    amount_matches = re.search(amount_regex, expected_perf_str)
    if amount_matches:#金額
        amount_match = amount_matches.group()
        print(amount_match)

    keymsg_regex = r"\W*[未][入][績][效]\s?"
    keymsg_str = ("@昱慧 @立修 東森未入績效 9/21止3069200\n")
    keymsg_matches = re.search(keymsg_regex, keymsg_str)
    if keymsg_matches:
        keymsg_match = keymsg_matches.group()
        print(keymsg_match.strip()+'123')



