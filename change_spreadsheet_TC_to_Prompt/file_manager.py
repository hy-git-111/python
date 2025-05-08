import os, json

class FeileManager:
    def __init__(self, prompt_dir="prompts", test_code_dir = "tests"):
        self.prompt_dir = prompt_dir
        self.test_code_dir = test_code_dir

        os.makedirs(prompt_dir, exist_ok=True)
        os.makedirs(test_code_dir, exist_ok=True)

    # 프롬프트를 .json으 저장하는 함수
    def save_prompt_json(self, prompt_data, filename):
        filepath = os.path.join(self.prompt_dir, f"{filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(prompt_data, f, indent=2, ensure_ascii=False)  # 한글도 깨지지 않도록
        print(f"[저장 완료] {filepath}")

    # 테스트코드를 .py로 저장하는 함수
    def save_test_code(self, response, sheet_name):
        filepath = os.path.join(self.test_code_dir, f"{sheet_name}.py")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"{sheet_name} 테스트 코드로 저장 완료")

    # 프롬프트 파일을 읽는 함수
    def read_prompt_json(self, sheet_name):
        filepath = os.path.join(self.prompt_dir, f"{sheet_name}.json")
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
