class PromptGenerator:
    # 테스트케이스 한 줄을 받아 저장하는 함수
    def __init__(self, row):
        self.row = row

    # 프롬프트를 생성하는 함수
    def generate(self):
        test_id = self.row.get("No.", "unnamed")
        title = self.row.get("Title", "")
        precondition = self.row.get("Precondition", "")
        steps = self.row.get("Steps", "")
        expected = self.row.get("Expected Result", "")

        step_lines = [s.strip() for s in str(steps).split("\n") if s.strip()]
        expected_lines = [e.strip() for e in str(expected).split("\n") if e.strip()]

        prompt = f"""
테스트 ID: {test_id}
시나리오: {title}

사전 조건:
{precondition}

재현 절차:
"""
        for i, step in enumerate(step_lines, 1):
            prompt += f"{i}. {step}\n"

        prompt += "\n기대 결과:\n"
        for i, expect in enumerate(expected_lines, 1):
            prompt += f"{i}. {expect}\n"

        return prompt
