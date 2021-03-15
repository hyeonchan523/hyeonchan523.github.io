---
layout: single
title:  "[Python libs] Test-driven develope를 위한 python unittest 라이브러리"
exerpt : "TDD를 위한 파이썬 유닛 테스트 라이브러리"
summary: "unittest"

category : python
tags: [python, unittest]
toc : true
toc_sticky : true
---
Test-driven develop(TDD)는 개발이 끝난 후에 테스트를 진행하는 것이 아니라, 작은 단위의 기능을 수행하는지 여부를 테스트를 통과한 코드를 전체 코드에 리팩토링해 병합하는 방식의 개발 방법을 이야기합니다. TDD의 시작은 unittest를 작성하는 것입니다. 

# Unit test

- code를 테스트 하는 것은 bug가 없이 의도한 바를 구현하는데 중요하지만 데이터 사이언스에서 쉽게 간과됨
- 프로젝트가 커지고 복잡해짐에 따라 예상치 못한 버그가 발생할 가능성이 매우 높음
- unittest는 작성한 코드가 의도한대로 작동하는지 여부를 검증하는 과정

## unit test의 필요성

- testing을 작성하는 것은 문제가 없이 clean하고 사용성 높은 코드를 작성하는데 필수적임
- 어느 이상의 양을 가지는 복잡한 코드는 불가피하게 버그를 가지게 됨
- 의도한 결과를 만드는 코드를 작성하고 유지하는 것은 **포괄적인** 테스트를 얼마나 잘하는지에 달려있음
- 더 효율적이고 강건한 코드를 작성할 수 있음

## unit test의 원칙

- Unit test는 독립된 하나의 method에 대해서 이뤄짐
- 알고있는 고정된 input과 output에 대해서 테스트를 진행해야 함

## Assertion

- 이전 assertion에 관한 내용을 [포스팅](https://hyeonchan523.github.io/python/python-assert/)에서 확인할 수 있습니다.
- 주어진 조건의 참 거짓을 확인하고 에러를 발생시키는 assertion을 이용하는 것이 가장 기본적인 방법

    ```python
    def apply_discount(product, discount):
      	price = int(product['price'] * (1 - discount))
      	assert 0 <= price <= product['price'], 'Invalid Discount!!!' #Assertion here
      	return price
    ```

## unittest libs

- test는 각각 unit에 대해서 독립적으로 실행하고, 메모리를 효율적으로 관리할 수 있도록 해야함
- 이를 위해 python의 내장라이브러리인 unittest를 사용할 수 있음

### unittest 작성

- 테스트를 하고자하는 함수를 포함한 스크립트 `functions.py`와  테스트를 위한 스크립트 `test_functions.py`가 필요
- `test_functions.py`에 `unittest.TestCase`를 상속받는 새로운 클래스를 만들어 코드를 실행
- 만든 클래스에서 테스트할 method의 이름 앞에 test를 붙여 새로 정의해야 test가 진행됨
- method의 `output`과 예상한 기대값 `expected`를 비교해 assert을 발생시킴
- `unittest.TestCase`에 정의되어있는 여러 종류의 assert를 활용할 수 있다.<sup>[1]

### setUp() tearDown()<sup>[3]

- unittest로 작성된 테스트는 method별로 독립적으로 수행되지만 모든 테스트의 시작과 끝에서 같은 명령을 수행하고자 할 수 있음(예를 들면 입력 값을 공유하는 등)
- setUp() : 각 test 전에 수행할 명령어 / *변수 선언, data base 활성화*  등의 작업을 수행
- tearDown() : 각 test 후에 수행할 명령어 / test 이전의 상황으로 돌려놓는 모든 종류의 명령 수행

### Edge case 테스트 <sup>[4]

- 코드를 작성한 후에 최소한 두가지 케이스에 대해 테스트를 진행을 해야함
    1. 안정적으로 작동을 해야하는 케이스
    2. 입력값으로 주어질 수 있는 케이스 중 extreme한 케이스(edge case)
- 어떤 경우를 edge case로 정의할지와 같은 어려움이 있지만 다양한 edge case에 대한 테스트는 전체적인 프로그램의 신뢰성에 큰 도움이 됨

## Example

- 공부한 내용을 적용해보기 위해 python 언어 강의 과제를 활용해 unittest 연습을 해봄
- 연도를 입력받아 윤년인지 아닌지 알려주는 프로그램

---

<script src="https://gist.github.com/hyeonchan523/e15a440b4ff9c1c52bdbb03a35f0429d.js"></script>

- main 코드는 다음과 같음
    1. 입력으로 0을 받으면 프로그램을 종료
    2. 0이 아니고 양의 정수가 아닌 입력을 받으면 입력이 아니라는 메시지를 띄우고 다시 입력을 받음
    3. 양의 정수인 입력에 대해 [윤년](https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%85%84) 인지 아닌지 여부를 알려줌

---

<script src="https://gist.github.com/hyeonchan523/6b6d2e1e9aee6131c853f5d13bb688d0.js"></script>

- 각 기능을 수행하는 코드는 check_module에 함수로 만듬
    1. `validity_check`는 입력이 음수이거나 정수가 아닐 때 메시지를 print하고 False를, 양의 정수 입력은 True를 return
    2. `leak_year_check`는 입력이 윤년인 경우 True를 return

---

 <script src="https://gist.github.com/hyeonchan523/712c2f03636c09fe56ecaa8b525ddd3c.js"></script>

- 이 모듈의 함수들을 테스트하기 위한 코드를 위와 같이 작성
    1. `setUp`에서 각 테스트를 시작하기 전에 공통적으로 실행할 코드로 입력 연도를 선언
    2. `testDown`에서 각 테스트를 마친 후에 실행시킬 코드 작성
    3. `test_`로 시작하는 테스트 메소드를 정의
- 오류가 없는 경우에는 마지막에 커멘드 상에 OK만 출력됨  
    <img src = '{{site.url}}/assets/img/unittest_ok.png' align = 'center'>

- 오류가 발생한 경우에는 오류가 발생한 위치를 띄워줌  
    <img src = '{{site.url}}/assets/img/unittest_fail.png' align = 'center'>

---

# Reference
[[1]] unittest docs  
[[2]] Leveling Up Your Python Code: The Importance of Testing - medium  
[[3]] Explain the “setUp” and “tearDown” Python methods used in test cases  - stack overflow  
[[4]] Tips for How to Succeed in Coding Interviews - medium  
[[5]] Introduction to Unit Testing in Python Using unittest Framework - medium  
[[6]] Effective Unit Testing by Eliotte Rusty Harold - youtube  

[1]: https://docs.python.org/ko/3/library/unittest.html
[2]: https://link.medium.com/2PcGVA48keb
[3]: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases
[4]: https://link.medium.com/BUkpWEVvAeb
[5]: https://medium.com/swlh/introduction-to-unit-testing-in-python-using-unittest-framework-6faa06cc3ee1
[6]: https://www.youtube.com/watch?v=fr1E9aVnBxw&t=2137s 
