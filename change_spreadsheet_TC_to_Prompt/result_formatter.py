import re

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

# api 응답에서 python 태그를 제거하는 함수
def remove_python_tags(content):
    if content.startswith("```python"):
        content = content[len("```python"):].strip()
    if content.endswith("```"):
        content = content[:-len("```")].strip()
    return content

# api 응답에서 파일명과 내용 추출하는 함수
def extract_filenames_and_contents(full_text):
    pattern = r"#\s*([\w]+)\.[\w]+(.*?)#\s*[\w]+\.[\w]+|$"
    matches = re.findall(pattern, full_text, re.DOTALL)
    return [(filename.strip(), content.strip()) for filename, content in matches]