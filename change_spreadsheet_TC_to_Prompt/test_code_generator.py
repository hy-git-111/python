from anthropic import Anthropic
from initial_prompt import ui_requirement
from user_data import API_KEY

# claud API에 연동하여 프롬프트를 전송하고 결과를 반환하는 함수 
def generate_test_code(all_prompts):
    client = Anthropic()

    print("프롬프트 전송 중...")
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=64000,   # max 64000
        temperature=1,
        system=ui_requirement,
        messages=all_prompts,
        stream=True # 스트리밍 활성화
    )

    for event in response:
        if event.type == "content_block_delta": # content_block_delta : 텍스트가 생성되어 전송되었음을 알리는 이벤트 타입입
            # print(event.delta.text, end="", flush=True) # event.delta : 새로 추가된 텍스트 조각을 담고 있는 객체 / flush=True : 출력 버퍼를 비우고 내용을 즉시 화면에 표시

            yield event.delta.text  # 값 반환 및 일시중단
    print("응답 완료\n")
        
    # return response.content[0].text   # 전체 답변을 기다린 후 출력하는 비스트리밍 방식

