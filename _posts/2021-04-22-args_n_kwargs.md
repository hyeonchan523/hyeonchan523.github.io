---
layout: single
title:  "[Python] *args와 **kwargs 활용하기"
excerpt : "lambda 함수를 사용해 list sorting을 간편하게"
summary: ""

category : python
tags: [python, Python trick, args, kwargs]
toc : true
toc_sticky : true
use_math : true
---
- open source 라이브러리를 사용하며 문서를 찾다보면 `*args`와 `**kwargs`가 사용되는 것을 볼 수 있다.
- 두 키워드는 해당 함수에 여분의 argument를 전달해 줄 수 있는 방법이다.
- `*`는 필요한 parameter 이외에 추가로 전달되는 argument를 **tuple**로 전달하고, `**`는 **dictionary** 형태로 전달한다.

<script src="https://gist.github.com/hyeonchan523/f6c186eceeb2f12d3a59e7589ccb9cc1.js"></script>
- 여기에서 중요한 부분은 `*`와 `**`로, `*`나 `**`뒤에는 args, kwargs 대신 어떤 단어를 사용해도 좋다.

---

- `*`와 `**`를 활용해 함수를 정의하는 것 뿐만 아니라 argument를 tuple이나 dictionary 형태로 함수에 전달 할 수 있다.

<script src="https://gist.github.com/hyeonchan523/093c883f1402b9ee0594c60136f25db2.js"></script>
- dictionary 형태로 argument를 전달하는 방식은 머신러닝 모델을 정의할 때 많이 사용하게 된다.