---
layout: single
title:  "[Python] numpy array를 사용할 때 for문을 피해야하는 이유"
excerpt : "numpy array를 활용할 때 for문을 대체할 방법을 고려해야합니다."
summary: "Avoid for loops with numpy array"

category : python
tags: [python, Python trick, numpy, ufunc]
toc : true
toc_sticky : true
use_math : true
toc_ads: true
---

# Avoid for loops with numpy array

- numpy는 배열을 효율적으로 다룰 수 있도록 만들어진 라이브러리입니다.
- 같은 배열을 저장하고 있더라도 list에 비해 효과적으로 메모리를 사용하고, tensor간 연산을 지원해 계산 속도에서도 큰 이점을 가집니다.<sup>[1]</sup>
- 요소별로 연산을 필요로 할 때, for 문을 활용해 계산을 하면 numpy의 장점을 활용하지 못합니다.
- numpy는 범용 함수(ufunc)을 지원하기 때문에 for문을 사용할 때와 비교가 안될 만큼 효율적인 요소별 계산을 할 수 있습니다.
- 아래 예를 보게 된다면 numpy 배열에 요소별 연산을 할 때 for 문이 얼마나 비효율적인지 알게 됩니다.
<script src="https://gist.github.com/hyeonchan523/553fef8fd54b3b38374cd852e97b9c23.js"></script>
- 속도 뿐만 아니라 코드를 작성할 때도 for 문을 사용하지 않아도 되기 때문에 간결하게 코드를 작성할 수 있습니다.

### Example

- 서울대학교 김성우 교수님의 "머신러닝을 위한 기초 수학 및 프로그래밍 실습" 강의의 과제로 작성했던 코드를 예로 들어보겠습니다.
- 코페르니쿠스가 화성의 위치를 계산하기위해 유도했던 식을 프로그램화 해보는 과제입니다. 두 시점에서 지구의 태양 중심의 경도($\theta_1,\theta_2$)와 화성의 지구 중심 경도($\phi_1,\phi_2$)로 아래와 같은 식으로 화성의 좌표를 계산할 수 있습니다.  

\[
x_{Mars} = \frac{(\sin{\theta_2} - \sin{\theta_1}) + (\tan{\phi_1}\cos{\theta_1} - \tan{\phi_2} \cos{\theta_2})}{\tan{\phi_1}-\tan{\phi_2}}\]
\[
y_{Mars} = \tan{\phi_1}x_{Mars} +\sin{\theta_1} - \tan{\phi_1}\cos{\theta_1}
\]

- `to_degree`함수는 각도의 단위를 변환해주는 함수이고, `calculate_coordinate`는 화성의 좌표를 계산해주는 함수입니다.
- `to_degree`에서 단위를 변환해 주는 과정 중에 array간의 element-wise 계산을 수행합니다.
- `calculate_coordinate`에서는 line3 에서 데이터를 $\theta_1, \phi_1,\theta_2,\phi_2$ **벡터**로 분리했고, line4와 line5에서 화성의 좌표를 계산합니다.


<script src="https://gist.github.com/hyeonchan523/212fe5fea366ebb8d190abbe3d57a92f.js"></script>


- 만약에 numpy 배열을 list처럼 생각하고 for 문을 사용한다면 다음과 같이 비효율적인 방식으로 장황하게 코드를 작성해야합니다.


<script src="https://gist.github.com/hyeonchan523/72e232447af7576164ed880bc512f658.js"></script>

- 실행 시간을 측정해보면 비효율 적인 방식이 3배의 시간이 걸리는 것을 볼 수 있습니다. 데이터가 많아지면 이 차이는 더 커집니다.

<script src="https://gist.github.com/hyeonchan523/de3f410bd513b967ce5884dc25f4a970.js"></script>

## np.vectorize로 ufunc 정의하기

- 라이브러리에서 제공하는 ufunc으로 대부분의 작업이 가능하지만 스칼라 연산에 대해 정의 된 함수를 ufunc으로 바꿀 수 있는 방법이 있습니다.
- 궂이 vectorize방법이 필요한 상황을 생각해보았지만 지금은 떠오르지 않지만 억지로 예시를 만들자면 다음과 같은 예시가 있을 수 있습니다.
- python 내장 라이브러리인 math의 sin함수는 numpy array 연산을 지원하지 않지만 vecotrize 함수를 사용해 다음과 같이 범용함수로 만들 수 있습니다.
  
<script src="https://gist.github.com/hyeonchan523/6bcf27aae7ce516f7d862862f6cdccc4.js"></script>

# 마무리
- numpy array를 사용할 때 범용함수(universial function)의 유용함을 확인했습니다.
- numpy 연산의 특징을 잘 활용할 때, for 문을 사용해 코드가 길어질 때 발생할 수 있는 잠재적인 오류의 원인을 막을 수 있고 빠른 연산 속도를 보장할 수 있습니다. 

# Reference
[[1]] numpy ufunc docs  
[[2]] Python Lists vs. Numpy Arrays - What is the difference? - UCF open course  
[[3]] 코페르니쿠스 혁명 - wiki  


[1]: https://numpy.org/doc/stable/reference/ufuncs.html  
[2]: https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference  
[3]: https://ko.wikipedia.org/wiki/코페르니쿠스_혁명

