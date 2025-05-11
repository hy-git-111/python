from anthropic import Anthropic
from anthropic import RateLimitError
import time

class TestCodeGenerator:
    def __init__(self, model_name, temperature, system_prompt, max_tokens_per_request):
        self.client = Anthropic()
        self.model_name = model_name
        self.temperature = temperature
        self.system_prompt = system_prompt
        self.max_tokens_per_request = max_tokens_per_request
        self.generated_text = ""  # 생성된 텍스트 누적
        print("API 클라이언트 초기화 완료")

    # API 응답을 생성하는 내부 헬퍼 함수
    def _create_response(self, messages, max_tokens, stream=False):
        try:
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=max_tokens,
                temperature=self.temperature,
                system=self.system_prompt,
                messages=messages,
                stream=stream
            )
            return response
        except Exception as e:
            print(f"API 응답 생성 오류: {e}")
            raise  # 오류를 상위 함수로 전파

        except RateLimitError as e:
            print(f"Rate limit exceeded. Waiting before retry: {e.response.headers['retry-after']} seconds")
            time.sleep(float(e.response.headers['retry-after']))

    # Claude API에 프롬프트를 전송하고 스트리밍 방식으로 응답을 반환하는 함수
    def generate_test_code(self, all_prompts, response=None, previous_response=""):
        messages = []

        # 이전 응답이 있으면 messages에 추가
        if previous_response:
            messages.append({"role": "assistant", "content": previous_response})

        for prompt in all_prompts:
            messages.append(prompt)

        print("프롬프트 전송 중...")
        try:
            current_text = ""
            for event in response:
                if event.type == "content_block_delta": # content_block_delta : 텍스트가 생성되어 전송되었음을 알리는 이벤트 타입
                    text_delta = event.delta.text
                    current_text += text_delta
                    self.generated_text += text_delta  # 생성된 텍스트 누적
                    yield event.delta.text  # 값 반환 및 일시중단
            print("응답 완료\n")

            return current_text
            
        except Exception as e:
            print(f"Claude API 오류: {e}")
            yield f"오류 발생: {e}"
            return ""

    # 토큰 수 계산하는 함수
    def tocken_count(self, messages, response=None):
        result = {"input_tokens": 0, "output_tokens": 0}

        try:
            # 입력 토큰 계산
            count_response = self.client.beta.messages.count_tokens(
                betas=["token-counting-2024-11-01"],    # 토큰 계산 버전의 베타기능 사용
                model=self.model_name,
                system=self.system_prompt,
                messages=messages
            )
            result["input_tokens"] = count_response.input_tokens
            
            # 응답 객체가 있는 경우에만 출력 토큰수 계산
            if response and hasattr(response, 'usage') and hasattr(response.usage, 'output_tokens'):
                result["output_tokens"] = response.usage.output_tokens
                
            return result
        
        # Beta API가 실패할 경우 일반 api 응답 객체에서 토큰 수 추출
        except Exception as e:
            print(f"토큰 계산 오류: {e}")
            if response and hasattr(response, 'usage'):
                if hasattr(response.usage, 'input_tokens'):
                    result["input_tokens"] = response.usage.input_tokens
                if hasattr(response.usage, 'output_tokens'):
                    result["output_tokens"] = response.usage.output_tokens
            
            return result
        
    # 토큰 수를 체크하면서 코드 생성
    def generate_code_with_token_check(self, all_prompts, max_total_tokens):
        all_text = ""
        total_tokens = 0
        request_count = 0
        threshold = self.max_tokens_per_request * 0.8  # 최대 토큰의 80%를 임계값으로 설정
        
        # 프롬프트를 메시지 형식으로 변환
        messages = []
        for prompt in all_prompts:
            messages.append(prompt)
        
        # 첫 번째 응답 생성
        print(f"\n--- 요청 {request_count + 1} 시작 ---")

        time.sleep(1)  # Rate limit을 피하기 위해 잠시 대기
        response = self._create_response(
            messages, 
            self.max_tokens_per_request, 
            stream=False
        )
        
        request_count += 1
        all_text += response.content[0].text
        
        # 출력 토큰 수 확인
        used_tokens = response.usage.output_tokens
        total_tokens += used_tokens
        
        print(f"\n이번 요청 토큰 수: {used_tokens}, 총 토큰 수: {total_tokens}")
        
        # 토큰 임계값을 초과했는지 확인하고 필요시 추가 요청
        while used_tokens >= threshold and total_tokens < max_total_tokens:
            print(f"\n최대 토큰의 80% 이상 사용됨({used_tokens}/{self.max_tokens_per_request}). 추가 요청 진행")
            
            # 새로운 프롬프트 생성
            continuation_prompt = [
                {"role": "user", "content": f"이어서 답변해주세요. 지금까지 생성된 내용은 다음과 같습니다:\n{all_text}"}
            ]
            
            # 추가 응답 생성
            print(f"\n--- 요청 {request_count + 1} 시작 ---")
            remaining_tokens = min(self.max_tokens_per_request, max_total_tokens - total_tokens)
            
            time.sleep(1)  # Rate limit을 피하기 위해 잠시 대기
            response = self._create_response(
                continuation_prompt, 
                remaining_tokens, 
                stream=False
            )
            
            request_count += 1
            additional_text = response.content[0].text
            all_text += additional_text
            
            # 출력 토큰 수 업데이트
            used_tokens = response.usage.output_tokens
            total_tokens += used_tokens
            
            print(f"\n이번 요청 토큰 수: {used_tokens}, 총 토큰 수: {total_tokens}")
            
            # 더 이상 출력이 없으면 중단
            if not additional_text.strip():
                print("\n더 이상 응답이 없습니다.")
                break
                
            # 최대 토큰에 도달하면 중단
            if total_tokens >= max_total_tokens:
                print(f"\n최대 토큰 수({max_total_tokens})에 도달했습니다. 코드 생성을 중단합니다.")
                break
        
        return all_text