

import requests as rq
import urllib

tdy_date_str = "20220614"
salesman = "李永齊"



urls = []
i = 1
j = 0
count = 0
while i > 0:
    print(i)
    rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/'+str(tdy_date_str)+urllib.parse.quote(str(salesman)+'銷貨明細_')+ str(i) +'.jpg')
    if rqt.status_code == 200:
        print('https://raw.githubusercontent.com/abel108714/test/master/'+str(tdy_date_str)+urllib.parse.quote(str(salesman)+'銷貨明細_')+ str(i) +'.jpg') 
        urls.append('https://raw.githubusercontent.com/abel108714/test/master/'+str(tdy_date_str)+urllib.parse.quote(str(salesman)+'銷貨明細_')+ str(i) +'.jpg')
        columns.append(


        )
        i += 1
    else:
        count = i
        i = 0



for x in urls:
    print("----")
    print(x)
    print("----")


print("count = " + str(count))



message = TemplateSendMessage(
    alt_text=str(tdy_date_str),
    template=ImageCarouselTemplate(
        columns=[            
            ImageCarouselColumn(
                image_url=str(urls[i]),
                action=URITemplateAction(
                    label="報表",
                    uri = urls[i]
                )
            ) for i in range(1, count+1)]
    )
)



# message = TemplateSendMessage(
#     alt_text=str(tdy_date_str),
#     template=ImageCarouselTemplate(
#         columns=[

#             for urlindex in urls

            # ImageCarouselColumn(
            #     image_url=str(urls[0]),
            #     action=URITemplateAction(
            #         label="報表1",
            #         uri = urls[0]
            #     )
            # )
#         ]
#     )
# )