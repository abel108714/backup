
#import excel2json

#excel2json.convert_from_file('123.xlsx')
import json
import pandas
# Read excel document
#excel_data_df = pandas.read_excel('123.xlsm', sheet_name='Sheet1')
excel_data_df=pandas.read_excel('123.xlsm', sheet_name='Sheet1', engine='openpyxl')

# Convert excel to string (define orientation of document in this case from up to down)
thisisjson = excel_data_df.to_json(orient='records')
# Print out the result
print('Excel Sheet to JSON:\n', thisisjson)
# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)
# Define file to write to and 'w' for write option -> json.dump() defining the list to write from and file to write to
# with open('data.json', 'w') as json_file:
#     json.dump(thisisjson_dict, ensure_ascii=False).decode('utf8').encode('gb2312')

import codecs
fp = codecs.open('data.json', 'w', 'utf-8')
fp.write(json.dumps(thisisjson_dict,ensure_ascii=False))
fp.close()
