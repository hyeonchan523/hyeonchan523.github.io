---
layout: single
title:  "[Python] 파이썬 용어 사전"
excerpt : "다소 학술적인 용어"
summary: ""

category : python
tags: [python]
toc : true
toc_sticky : true
toc_ads: true
use_math : true
---
포스팅을 작성하며 생각나는대로 업데이트합니다.

### 바인딩
- 파이썬에서 변수를 선언 할 때 객체를 **가리킨다**고 표현을 하는데 이것을 바인딩됐다고 이야기 함.
- name = 'Python' 이라고 선언했을 때, `Python`이라는 문자열 객체와 name 변수가 바인딩 됐다고 함.

### short-circuit Evaluation
`and`나 `or`로 boolean 값을 다룰 때 연산을 최소화하기 위한 방법  
- (A `or` B)는 둘 중 하나만 참이면 `True` $\to$ A가 참이면 B 연산 안함
- (A `and` B)도 마찬가지로 A가 `False` $\to$ A가 거짓이면 B 연산 안함

