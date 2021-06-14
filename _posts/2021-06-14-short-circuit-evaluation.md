---
layout: single
title:  "[Python] short-circuit evaluation"
excerpt : "python에서 and, or는 효율적인 계산을 위해 short-circuit evaluation을 한다." 
summary: "최소 계산 추구"

category : python
tags: [python]
toc : true
toc_sticky : true
toc_ads: true
use_math : true
---

# short-circuit Evaluation

- `and`나 `or`로 boolean 값을 다룰 때 연산을 최소화하기 위한 방법  
## `and`
- `and`는 두 값이 모두 참일때만 `True`를 반환하고 나머지 경우에는 `False`를 반환
    - (A `and` B)에서 A가 `False` $\to$ A가 거짓이면 B 연산 안함
    - A가 `True`면 B의 참, 거짓이 (A `and` B)의 참거짓을 결정 $\to$ B를 반환

## `or`
- `or`은 두 값 모두 거짓일때만 `False`를 반환하고 나머지 경우에는 `True`를 반환
    - (A `or` B)는 둘 중 하나만 참이면 `True` $\to$ A가 참이면 B 연산 안함
    - 마찬가지로 A가 `False`이면 B의 참, 거짓이 (A `or` B)의 참거짓을 결정 $\to$ B를 반환

## Bitwise Operators
- boolean 연산의 두 operand가 function의 결과로 얻어지는 등의 경우와 같이 반드시 연산이 필요한 경우에는 *bitwise operator*를 사용
- bitwise operator는 양쪽의 operand의 연산을 먼저 수행하고 비교함
- | : bitwise `or`, & : bitwise `and`


### Example
***and vs &***
- line 2에서 `and`의 앞의 operand가 `True`이기 때문에 `15` 부분은 연산하지 않고 값을 반환
- 반면 line 3에서 `&`는 두 operand의 boolean을 연산한 후에 비교해 `True`를 반환
    - numeric에 대해서는 0을 제외한 모든 수는 True  

***or vs |***
- line 10에서 `or`의 앞의 operand가 `False`이기 때문에 `15` 부분은 연산하지 않고 값을 반환

<script src="https://gist.github.com/hyeonchan523/d703509b5b799382190ac7453e0e8189.js"></script>

