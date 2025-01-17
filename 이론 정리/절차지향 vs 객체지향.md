[마크다운 가이드] https://www.markdownguide.org/cheat-sheet/  

# 절차 지향 vs 객체 지향
: 프로그램의 규모와 목적에 따라 코드 작성 방식 선택

## 절차 지향 프로그래밍 (Procedural Programming)  
 : 소규모, 유틸리티 성향의 코딩 시 사용

## 객체 지향 프로그래밍 (OOP, Object-Oriented Programming)  
: 대규모, 클래스 기반(데이터 기반) 코딩

* 코드 재사용 용이
* 코드 중복 방지
* 유지보수 용이

## 사용 예시
* 일반적인 구조

    ```
    object1 = "o1"
    attribute1 = [
        {"attr1" : "a1"},
        {"attr2" : "a2"}
    ]

    object2 = "o2"
    attribute2 = [
        {"attr1" : "a1"},
        {"attr2" : "a2"}
    ]
    ```

* List 구조
    * 중복 코드 발생 > 데이터 수정/삭제 불편함
    * index 번호를 관리하는 함수가 별도로 필요함
    * index 접근 시 실수 가능성 있음

    ```
    object_list = ["o1", "o2"]
    attribute_list =[
        {"attr1" : "a1", "attr2" : "a2"},    #딕셔너리가 리스트 형식으로 저장
        {"attr1" : "a1", "attr2" : "a2"}
    ]
    ```

* Dictionary 구조
    * 중복 코드 발생 > 데이터 수정/삭제 불편함
    * 키 중첩 오류 발생 가능
    * 데이터 정렬 필요

    ```
    object_dict = [
        {"object" : "o1", "attribute" : {"attr1" : "a1", "attr2" : "a2"} } # nest dictionary(중첩 딕셔너리)
        {"object" : "o2", "attribute" : {"attr1" : "a1", "attr2" : "a2"} }
    ]
    ```

* Class 구조
    * 재사용성 증가(코드 반복 최소화)
    * 메소드 활용 가능

    ```
    class object_class():
        def __init__(self, object, attribute):
            self._object = object
            self._attribute = attribute

    attr1 = object_class("o1", {"attr1" : "a1", "attr2" : "a2"})
    attr2 = object_class("o2", {"attr1" : "a1", "attr2" : "a2"})
    ```


[학습 참고 영상] https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90