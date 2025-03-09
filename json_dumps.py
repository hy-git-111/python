# python의 dictionary 데이터를 json 문자열로 변환

import json

python_dict = {
    "id": 1,
    "username": "gildongGo",
    "families": {
        "ttochi": "duck",
        "dul-li": "dinosaur"
    }
}

json_string = json.dumps(python_dict)
print(json_string)