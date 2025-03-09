# json 문자열을 python dictionary 타입으로 변환
# '''{}''' 은 json 문자열을 뜻함.
# json 문자열은 데이터 전송을 위한 문자열 타입의 데이터

import json

json_string = '''{
    "id": 1,
    "username": "gildongGo",
    "families": {
        "ttochi": "duck",
        "dul-li": "dinosaur"
    }
}'''

python_object = json.loads(json_string)
print(json_object)

assert json_object["id"] == 1
assert json_object["username"] == "gildongGo"
assert json_object["families"]["dul-li"] == "dinosaur"