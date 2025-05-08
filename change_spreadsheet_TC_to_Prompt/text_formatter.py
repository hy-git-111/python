# TC 데이터를 Claude 메시지 포맷(iterable)으로 변환하는 함수
def tc_formatter(content):
    formatted_content = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": content
                }
            ]
        }
    return formatted_content