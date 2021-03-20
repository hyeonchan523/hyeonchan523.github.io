---
layout: single
title:  "[Python] assert문으로 디버깅"
excerpt : "assert문으로 예상치 못한 버그를 방지하기"
summary: "assert문을 활용하면 디버깅을 효과적으로 할 수 있다."

category : python
tags: [python, Python trick, assert, debugging]
toc : true
toc_sticky : true
use_math : true
---
이 글은 [슬기로운 파이썬 트릭](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=179118176)의 내용을 정리한 글입니다.

## 2.1 assert(단언)문으로 방어하기

- 단언문은 어떤 조건을 테스트하는 디버깅 도구로 유용하다.
- 프로그램을 작성할 때 예상 범위 외로 벗어날 때 에러를 발생시킨다.
- `assert` 조건에서 벗어난 경우에 에러를 발생시킨다.

```python
## assert
assert expression1, 'expression2'
```

- `assert` 프로그램에서 만족할 것으로 생각하는 조건이고, expression2는 expression1이 False일 때 에러와 함께 출력할 표현이다.

### **예외처리를 하지 않는 이유 (try... except ...)**

- 에러를 발생시켜 다시 시도할 수 있는 버그가 아니라 프로그램은 실행되지만 존재하는 버그를 찾는데 활용할 수 있다.
- 따라서 디버깅을 할 때, 프로그램을 중단시키지는 않지만 예상치 못한 결과를 만드는 버그를 찾기 위해 사용한다.
- 다음과 같이 할인된 가격을 적용할 때, 가격은 음수이고, 원래 가격보다 클 수 없다.

    ```python
    def apply_discount(product, discount):
    	price = int(product['price'] * (1 - discount))
    	assert 0 <= price <= product['price'], 'Invalid Discount!!!'
    	return price
    ```

**Example**
```python
product = {'name' : 'shoes', 'price' : 50000}
discount = 0.2
apply_discount(product, discount)

```




    40000

정상적인 할인율이 적용된 경우에는 제대로 작동합니다.
```python
product = {'name' : 'shoes', 'price' : 50000}
discount = 2
apply_discount(product, discount)
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-4-7f0c68663e13> in <module>
          1 product = {'name' : 'shoes', 'price' : 50000}
          2 discount = 2
    ----> 3 apply_discount(product, discount)
    

    <ipython-input-1-e56f6faa1e5b> in apply_discount(product, discount)
          1 def apply_discount(product, discount):
          2         price = int(product['price'] * (1 - discount))
    ----> 3         assert 0 <= price <= product['price'], 'Invalid Discount!!!'
          4         return price
    

    AssertionError: Invalid Discount!!!
200%의 할인률이 적용된 경우에 에러를 발생시켜 알려줍니다.


### 단언문의 일반적인 함정

**보안과 관련된 함수에서는 단언문을 활용하지 말 것**
- 아이디와 패스워드 같은 자격을 인증하는 부분에서는 assert문을 자제하라는 내용입니다.(이해를 잘 못함)

**쓸모없는 단언문을 작성하지 말 것**

- 항상 참이되는 경우를 단언문에 넣는 경우
- python에서 비어있지 않은 tuple은 항상 참으로 간주한다.

    ```python
    if (1==2, 'asdf'):
        print('이게 참이라고?')
    ```

        이게 참이라고?

- 다음과 같은 단언문은 제 역할을 하지 못합니다.

    ```python
    assert (1==2,
        'your program have bug')
    ```

**Example**
```python
def apply_discount(product, discount):
	price = int(product['price'] * (1 - discount))
	assert (0 <= price <= product['price'],
            'Invalid Discount!!!'
            )
	return price
```

    <>:3: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    <>:3: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    <>:3: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    <ipython-input-20-9fd86cc4aa6d>:3: SyntaxWarning: assertion is always true, perhaps remove parentheses?
      assert (0 <= price <= product['price'],
    

python 3 버전에서는 이런 경우에 항상 참이라고 error를 띄워줍니다.


```python
product = {'name' : 'shoes', 'price' : 50000}
discount = 2
apply_discount(product, discount)
```




    -50000

## 마무리
- 데이터 분석을 하다보면 데이터를 몇 단계에 걸쳐 계산하고, 변환하는 일이 많은데 그 과정에서 발생하는 버그가 많다.
- 이미 정리가 끝난 코드에서 버그가 발견되어 시간을 많이 잡아먹는데 처음에 코드를 테스트할 때 이를 활용하면 좋을 것 같다.