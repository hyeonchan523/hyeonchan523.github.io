```python
def apply_discount(product, discount):
	price = int(product['price'] * (1 - discount))
	assert 0 <= price <= product['price'], 'Invalid Discount!!!'
	return price
```


```python
product = {'name' : 'shoes', 'price' : 50000}
discount = 0.2
apply_discount(product, discount)

```




    40000




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



```python
if (1==2, 'asdf'):
    print('이게 참이라고?')
```

    이게 참이라고?
    


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


