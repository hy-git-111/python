import os, json, re
from result_formatter import remove_python_tags, extract_filenames_and_contents

class FileManager:
    def __init__(self, prompt_dir="prompts", test_code_dir = "qa-realworld-automation"):
        # 디렉토리 매핑 설정
        self.directory_mapping = {
            "prompt": prompt_dir,
            "data": os.path.join(test_code_dir, "data"),
            "tests": os.path.join(test_code_dir, "tests"),
            "conftest": os.path.join(test_code_dir, "tests"),
            "fixtures": os.path.join(test_code_dir, "fixtures"),
            "utils": os.path.join(test_code_dir, "utils"),
            "default": test_code_dir,
        }

        # 디렉토리 생성
        for dir_path in self.directory_mapping.values():
            os.makedirs(dir_path, exist_ok=True)

    # 프롬프트를 .json으로 저장하는 함수
    def save_prompt_json(self, prompt_data, filename):
        filepath = os.path.join(self.directory_mapping["prompt"], f"{filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(prompt_data, f, indent=2, ensure_ascii=False)  # 한글도 깨지지 않도록
        print(f"[저장 완료] {filepath}")

    # 테스트코드를 .py로 저장하는 함수
    # def save_test_code(self, response, sheet_name):
    #     filepath = os.path.join(self.test_code_dir, f"{sheet_name}.py")
        
    #     # response가 청크 리스트인 경우 처리
    #     full_text = ""
    #     if isinstance(response, list):
    #         for chunk in response:
    #             full_text += chunk or ""  # "" : None 방지
    #     else:
    #         full_text = response  # 이미 문자열인 경우
        
    #     with open(filepath, "w", encoding="utf-8") as f:
    #         f.write(full_text)

    #     print(f"{sheet_name} 테스트 코드 단일파일로 저장 완료")

    # 주석에서 파일명을 인식하여 여러 파일로 분리 저장하는 함수
    def save_test_code_as_multiple_files(self, response, sheet_name, base_dir=None):
        # 기본 디렉터리 설정
        if base_dir is None:
            base_dir = self.directory_mapping["tests"]

        # response가 청크 리스트인 경우 처리
        full_text = ""
        if isinstance(response, list):
            for chunk in response:
                full_text += chunk or ""  # None 방지
        else:
            full_text = response  # 이미 문자열인 경우
        
        # 파일명 추출 (확장자 제외)
        matches = extract_filenames_and_contents(full_text)
        if not matches:
            print("파일명 주석을 찾을 수 없습니다.")
            return []
        
        # 찾은 파일명과 내용으로 파일 생성
        created_files = []
        for filename, file_content in matches:
            filename = filename.strip()
            file_content = remove_python_tags(file_content)     

            # "test" 또는 "locator"로 시작하는 경우 파일명에 sheet_name 추가
            if filename == "test_data" or filename.startswith("locator"):
                target_filename = f"{filename}.py"
            elif filename.startswith("test"):
                target_filename = f"{filename}_{sheet_name}.py"
            else:
                target_filename = f"{filename}.py"
            # 파일명에 따라 저장 경로 결정 및 생성성
            target_dir = self._get_target_directory(filename)
            os.makedirs(target_dir, exist_ok=True)
            filepath = os.path.join(target_dir, target_filename)
            
            # 파일 저장
            with open(filepath, 'w', encoding="utf-8") as f:
                f.write(file_content.strip())
            
            print(f"파일 '{filepath}' 생성 완료")
            created_files.append(filepath)
        
        if not matches:
            print("파일명 주석을 찾을 수 없습니다.")
            return []
            
        return created_files
    
    # 파일명에 따라 저장할 디렉토리를 결정하는 함수
    def _get_target_directory(self, filename):
        # data로 끝나는 파일은 data 폴더에 저장
        if filename.endswith("data.py"):
            return self.directory_mapping["data"]

        # test_ 로 시작하는 파일은 tests 폴더에 저장
        if filename.startswith("test_"):
            return self.directory_mapping["tests"]

        # conftest.py는 tests 폴더에 저장
        elif filename == "conftest.py":
            return self.directory_mapping["tests"]

        # fixture 가 포함된 파일은 fixtures 폴더에 저장
        # elif "fixture" in filename:
        #     return self.directory_mapping["fixtures"]

        # helper, util 등의 유틸리티 파일은 utils 폴더에 저장
        elif any(keyword in filename for keyword in ["helper", "util", "common"]):
            return self.directory_mapping["utils"]

        # 기본값은 default 디렉토리 사용
        return self.directory_mapping["default"]

    # 프롬프트 파일을 읽는 함수
    # def read_prompt_json(self, sheet_name):
    #     filepath = os.path.join(self.prompt_dir, f"{sheet_name}.json")
    #     with open(filepath, "r", encoding="utf-8") as f:
    #         return f.read()
