import json

with open('json_old.json', encoding="utf-8") as json_file_1:
    json1_dict = json.load(json_file_1)

with open('json_new.json', encoding="utf-8") as json_file_2:
    json2_dict = json.load(json_file_2)

diff_list = ["services", "staff", "datetime"]

result = {}
for key in diff_list:
    if json1_dict['data'][key] != json2_dict['data'][key]:
        result[key] = json2_dict['data'][key]

print(result)

with open('result.json', 'w', encoding="utf-8") as result_file:
    json.dump(result, result_file)
