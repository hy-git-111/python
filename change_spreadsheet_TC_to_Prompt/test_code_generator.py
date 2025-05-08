import anthropic
from initial_prompt import ui_requirement

# claud API에 연동하여 프롬프트를 전송하고 결과를 반환하는 함수 
def generate_test_code(all_prompts):
    client = anthropic.Anthropic()

    print("프롬프트 전송 중...")
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        temperature=1,
        system=ui_requirement,
        messages=all_prompts
    )

    print("응답 완료\n")
    return response

