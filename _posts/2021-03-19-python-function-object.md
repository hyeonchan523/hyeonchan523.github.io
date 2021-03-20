---
layout: single
title:  "[Python] python 함수를 아름답게 사용하기"
excerpt : "python의 함수도 객체임을 이해하면 파이썬스러운 코드를 작성할 수 있다."
summary: "python 함수는 객체다"

category : python
tags: [python, Python trick, python_function]
toc : true
toc_sticky : true
use_math : true
---
이 글은 [슬기로운 파이썬 트릭](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=179118176)의 내용을 정리한 글입니다.

## 3.1 파이썬 함수는 일급 객체다

- 파이썬에서 함수는 객체이기때문에 변수에 할당하고 데이터 구조에 저장하고 다른 함수에 인자로 전달하고, 함수의 값에서 반환할 수 있다.
- 이 한 문장이 이 포스팅의 요약이다. 개인적으로 문자형을 다루는 예시보다 숫자를 다루는 것이 이해가 더 잘 될 것이라고 생각해 성과금 관련 상황으로 예시를 수정했다.

### 함수는 객체(object)다

- 파이썬에서 모든 것은 객체이고 변수에 할당된다.
- 함수도 마찬가지로 변수에 할당될 수 있다.

<script src="https://gist.github.com/hyeonchan523/8d274d85be3b82e0a718a8dfa2878d53.js"></script>

- 위와 같은 경우에 level_1 뒤에 ()가 붙지 않아 호출되지 않고,  add_one은 level_1 함수를 가리키는 변수가 된다.
- one 변수로 plus_one 함수를 호출할 수 있다. 이때 del 로 level_1을 지우더라도 one은 정상적으로 작동한다

### 함수는 데이터 구조에 저장할 수 있다

- 숫자형이나 문자형 등의 자료형과 마찬가지로 함수도 객체이기 때문에 list 등의 구조에 저장할 수 있다.
- 성과금을 10%, 20%, 30%로 차등으로 지급할 때 아래처럼 각각 계산을 해볼 수 있습니다. 함수를 list에 저장해 각각 적용을 해 볼 수 있다.

<script src="https://gist.github.com/hyeonchan523/3005bc417381dc917cb6d0bee3b737a2.js"></script>

### 함수는 다른 함수로 전달할 수 있다

- 함수도 다른 함수의 인자로 전달할 수 있다. 함수를 인자로 받는 함수를 고차함수(higher-order function)이라고 한다.
- 성과금 비율을 정해주는 함수를 인자로 받아 월급에 더해주는 함수 total_income을 아래와 같이 작성할 수 있다.

<script src="https://gist.github.com/hyeonchan523/9e3554aa8f06769c56975e88e455bc8c.js"></script>

### 함수는 중첩될 수 있다

- 함수 내에 함수가 선언될 수 있다. 함수 내에 선언 된 함수는 모 함수가 호출될 때마다 선언된다.
- 함수 내에 선언된 함수는 일반적으로 접근할 수 없고 유일하게 접근할 수 있는 방법은 모 함수가 내부 함수를 반환하도록 작성될 경우다.
- 아래와 같이 성과에 따라 인센티브 레벨을 결정하는 함수를 작성할 수 있습니다.

<script src="https://gist.github.com/hyeonchan523/b0193ae71d1b8cae23e685920ea60764.js"></script>

**이후 내용은 유용하다고 판단하기 어려워 생략**

## 마무리

- 깊게 생각해보지 않으면 전혀 유용하다고 생각하지 않을 수 있는 내용이었다. 책에서 제시하는 예시가 문자열과 관련된 함수를 다루어서 내게 필요한 내용이 없다고 생각을 했다.
- 포스팅을 남기기 위해 내가 주로 사용하는 데이터 분석, 모델 학습과 관련해서 생각을 해보니 유용한 점이 많이 있었다.
- 이 내용들을 몰라도 잘 작동하는 main 함수를 작성할 수 있지만, 이 내용들을 사용한다면 기능을 더 추상화 해 더 깔끔하게 코드를 작성할 수 있을 것 같다.
    - 함수를 리스트에 저장함으로서 for 문을 이용해 여러 함수를 적용할 수 있다. main 코드에 각각 함수를 적용하는 코드를 장황하게 늘어지는 것을 방지할 수 있을 것 같다.
    - 함수를 중첩하는 경우에 위의 예에서 처럼 사용할 함수를 선택하는 과정에서 main 코드에 if 문을 너저분하게 나열하는 것이 아니라, 추상화 된 함수명으로 작성해 코드 이해를 쉽게 도와줄 수 있을 것 같다.
- 다른 유용함들도 있겠지만 이 챕터에서 나는 main 함수를 깔끔하게 작성할 수 있는 팁을 얻었다.