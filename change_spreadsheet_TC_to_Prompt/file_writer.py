import os

class PromptSaver:
    def __init__(self, output_dir="prompts"):
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    # 프롬프트를 파일로 저장하는 함수
    def save(self, prompt_text, filename):
        filepath = os.path.join(self.output_dir, f"{filename}.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(prompt_text)
        print(f"[저장 완료] {filepath}")
