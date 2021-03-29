---
layout: single
title:  "[Python] lambda 함수"
excerpt : "lambda 함수를 사용해 list sorting을 간편하게"
summary: ""

category : python
tags: [python, Python trick, lambda]
toc : true
toc_sticky : true
use_math : true
---
이 글은 [슬기로운 파이썬 트릭](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=179118176)의 내용을 정리한 글입니다.

## 3.2 람다는 단일 표현식 함수다

- lambda 키워드는 익명 함수를 선언하는 방법이다.
- 익명 함수라는 말은 함수를 `def function_name(parameters):` 와 같은 방식으로 선언한 경우 함수 객체를 `function_name`에 바인딩해 사용하는데 그럴 필요가 없다는 말이다.  
- 아래의 `add` 함수와 `add_lambda`는 같은 역할을 한다.  

<script src="https://gist.github.com/hyeonchan523/ba3b61ce613baa7933d044ae0c3b634e.js"></script>

- 람다 함수를 사용하게 되면 코드 def로 함수를 선언하는 몇 줄을 줄일 수 있지만 과도하게 사용하면 코드의 유지보수 측면에서 악영향을 줄 수 있다.
- 사용의 간결함과 유지보수의 악영향을 주지 않는 적정선에서 사용하는 것이 좋다.

### 람다 함수를 사용하기 좋은 경우

- list를 sorting할 때 key를 정의할 때 사용하기에 편리하다.
- 다음과 같이 tuple을 element로 가지는 list를 sorting할 수 있다.

<script src="https://gist.github.com/hyeonchan523/2fba695b132b02ca481887f2618c959a.js"></script>

## 마무리

- 아주 간단한 함수를 정의할 때는 사용할 수 있지만 조금만 단계가 복잡해지면 사용할 수 없을 것 같고, 누구나 다 알 수 있는 내용이 아니라면 설명을 추가해줘야할 것 같다.
- 위에서 사용한 list를 sorting하는 경우 외에는 유용함을 찾지 못했다.