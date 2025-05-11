from result_formatter import tc_formatter

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

        content = f"""
테스트 ID: {test_id}
시나리오: {title}

사전 조건:
{precondition}

재현 절차:
{steps}
기대 결과:
{expected}
"""
        return tc_formatter(content)
