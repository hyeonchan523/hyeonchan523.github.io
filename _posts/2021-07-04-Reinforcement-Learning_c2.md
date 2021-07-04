---
layout: single
title:  "[강화학습] Introduction"
excerpt : "단단한 머신러닝 Chapter 2 다중 선택"
summary: "Chapter 2 Multi-armed bandit"

category : reinforcement-learning
tags: [강화학습]
toc : true
toc_sticky : true
toc_ads: true
use_math : true
---

***기호 정리***
행동 (action) : a | t 시점에서 행동은 A_t  
보상 (reward) : R_t   
가치 (value) : q_*(a) = E[R_t | A_t = a] | t 시점에서 가치의 추정치는 Q_t(a)  

이번 장에서는 다중 선택 문제를 해결하기 위해 exploration - exploitation trade-off를 다루기 위한 간단한 방법들을 설명함.  

## 다중 선택 문제 소개

- 여러 개의 선택지 중 하나를 반복적으로 선택하는 문제
- 각 선택하는 즉시 정상 **확률 분포**(stationary probability distribution)로부터 보상을 얻음
- 다중 선택 문제에서 k개의 행동에는 각각 기대할 수 있는 평균 보상 값이 **가치**
- t 시점에서 행동 A_t가 선택됐을 때 보상을 R_t라고 하면 행동 a의 가치는

$q_{*}(a) = E[R_{t} | A_{t} =a]$

- 행동의 가치를 정확히 알 수 없기 때문에 좋은 가치의 추정치 $Q_{t}(a)$를 구하는 것이 목표


## 탐험과 활용(Exploration and Exploitation)

- **활용**은 t 시점까지 추정한 가치에 기반해 가치가 가장 높은 행동을 취하는 탐욕적(greedy)인 행동을 의미
    - 활용만 한다면 더 높은 보상을 기대할 수 있는 행동을 취하지 않아 장기적인 관점에서 바람직하다고 볼 수 없음
- **탐험**은 탐욕적인 행동이 아닌 다른 행동을 취하는 것을 의미함.
- 탐험을 하는 동안 단기적으로 보상이 낮을 수 있고, 활용을 하는 동안 더 높은 보상을 줄 수 있는 행동을 하지 않기 때문에 둘 사이에 trade-off가 존재
- 이번 장을 통해 탐험과 활용을 적절히 분배하는 간단한 방법들을 소개함

## 행동 가치 방법(Action-value method)

- 행동을 선택할 때, 행동의 **가치**를 추정하고 추정값에 기반해 행동을 선택하도록 하는 방법을 통틀어 **행동 가치 방법**이라고 함
- 이때 추정된 가치를 활용하는 탐욕적 선택은 $A_{t} = \bold{argmax}_{a} Q_{t}(a)$로 결정됨


### 표본평균 방법(Sample-average)

- t 시점까지 행동 a를 선택했을 때 얻은 보상의 평균을 가치로 추정하는 방법

\[Q_{t}(a) = \dfrac{\sum^{t-1}_{i = 1} R_{i}\ I(A_{i}=a)}{\sum^{t-1}_{i = 1}I(A_i = a)}\]

- 여기서 $I$는 파라미터가 참일 때는 1을, 거짓일 때는 0인 함수
- 위 식으로 가치를 추정하는 코드를 구현하면 매 시점마다 중복되는 계산을 수행하게 됨
- 이는 t 시점에서 추정치와 보상과 t+1 시점에서 보상 사이의 점화식으로 정리됨

    **점증적 구현**

    \[Q_{n+1} = \frac{1}{n}\sum^{n}_{i=1}R_i \\
    = \dfrac{1}{n}(R_{n} + \sum^{n}_{i= 1} R_i)\\
    = \dfrac{1}{n}(R_{n} + (n-1)Q_{n})\\
    = \dfrac{1}{n}(R_{n} + nQ_{n} - Q_{n})\\
    = Q_{n} + \dfrac{1}{n}(R_{n} - Q_{n})\]

    - 새로운 추정치 = 이전의 추정치 + time step (관측값 - 이전 추정치)
    - 해석해보면 (관측값 - 이전 추정치)의 오차를 반영해 업데이트하는 방식으로 이해할 수 있다.
    - 여기에서 time step은 n이 커질수록 작은 값을 갖는다.
        - 이는 나중에 얻은 reward의 비중을 낮춰 모든 시점의 reward를 같은 정도로 반영해 추정하게 되는 것을 의미

### 기하급수적 최신 가중 평균(exponential recency-weighted average)

- 정상(stationary) 다중 문제에 대해서는 앞의 방법이 적절하지만, 보상이 시간에 따라 변하는 비정상(non-stationary)적인 경우에는 문제가 발생함
- 이런 경우 최근의 보상일수록 큰 가중치를 주는 것이 타당함
- time step을 0과 1 사이의 상수로 고정시키는 것이 한가지 방법
- $Q_{n+1} = Q_{n} + \alpha [R_{n} - Q_{n}]$으로 놓으면 앞과 비슷한 방식으로

    \[Q_{n+1} = \frac{1}{a_n}\sum^{n}_{i=1}R_i \\
    = aR_{n} + Q_{n} -aQ_{n}\\
    = aR_{n} + (1-a)Q_{n}\\
    = aR_{n} + [(1-a)aR_{n-1} + (1-a)]\\
    = aR_{n} + aR_{n} + (1-a)aR_{n-1} + (1-a)^{2}aR_{n-2} + \cdots+(1-a)^{n-1}aR_{1} + (1-a)^{n}Q_1\\
    = (1-a)^{n} Q_{1} + \sum^{n}_{i=1}a(1-a)^{n-i}R_{i}\]
- 식을 살펴보면 초기 추정치 $Q_{1}$과 각 시점의 보상들은 한 시점이 지남에 따라 (1-a)만큼 감쇄된 값으로, i 시점의 보상은 n 시점까지 남은 time step(n-i)만큼 감쇄되어 n+1 시점에 반영됨.
- $\alpha$는 감소율의 의미를 갖는다.


### 일반화

- 앞에서 고정된 $\alpha$가 아니라 time step에 따라 변화하도록 정의할 수 있는데, 추정치가 반드시 참값에 수렴하는 time step의 조건은
 \[\sum^{\infin}_{n=1}a_{n} = \infin,\ \   \sum^{\infin}_{n=1}a_{n}^2 < \infin\]
- 표본 평균 방법의 경우에는 수렴 조건을 만족하지만, 최신 가중평균은 만족하지 않음
- 위의 조건은 정상 상태의 보상 분포를 가정할 때는 맞추어주는 것이 좋지만, 대부분의 강화학습의 문제는 비정상 상태의 보상 분포를 갖기 때문에 위 조건을 만족하는 추정 방법은 잘 사용하지 않음
    - 늦은 수렴 속도
    - 튜닝의 어려움 등의 문제가 있음
- 앞서 언급한 방법들은 모두 초기 가치 평가의 영향을 받음
    - 이 점을 활용해 prior knowledge를 반영할 수 있는 점은 장점



## 10중 선택 테스트

- 정상적인 보상 분포를 갖는 10개의 행동을 선택할 수 있는 상황을 가정하고 **탐험과 활용** 사이의 선택을 조율하는 방법을 소개

![img]({{site.url}}/assets/img/multi_bandit.png)


- 위 그림에서 각각의 action의 보상은 평균(가치)이 q(a)를 갖고, 분산이 1인 정규 분포 형태를 갖는다.
- environment를 다음과 같이 class로 정의

<script src="https://gist.github.com/hyeonchan523/6baa6b01a4a50475c8a4643b1a9bd28b.js"></script>

- True value를 

<script src="https://gist.github.com/hyeonchan523/e798133134054a2d4ec5b8706dfff6a4.js"></script>

- action별 value는 다음 그림에서 보는 것과 같이 action 6이 가장 크다.

![img]({{site.url}}/assets/img/True_values.png)

### epsilon-greedy 방법

- 기본적으로 greedy한 선택을 하며 $\epsilon$의 확률로 랜덤하게 explore를 하도록 하는 방법
- 점근적 수렴성을 보장하지만 실제 효용성은 미지수이다.

<script src="https://gist.github.com/hyeonchan523/927486386a402ecc5592550e1e2b30d6.js"></script>

- 위 코드에서 epsilon 값으로 1%와 10%를 사용했을 때의 결과를 비교해보면 exploration을 더 많이 하도록 유도했을 때, 장기적으로 좋은 결과를 얻게 되는 것을 확인했다.

### 긍정적 초깃값(Optimistic initial value)

- 앞서 언급했듯, 가치 추정은 초깃값에 영향을 받음
- 실제 가치에 비해 매우 긍정적으로 초깃값을 추정하는 경우에 초반에 탐험을 유도하는 효과
- 이와 같은 방식으로 초기에 탐험을 촉진하는 기법을 긍정적 초깃값이라고 부름
- 긍정적 초깃값의 영향으로 탐험을 유도하는 효과는 일시적이기 때문에 비정상 문제에는 큰 도움이 되지 않음

<script src="https://gist.github.com/hyeonchan523/94dbefc3bf2c59e9d027ee2650c1e145.js"></script>

- 이 문제는 정상 문제이기 때문에 긍정적 초깃값이 긍정적인 영향을 주었다.
- 탐험을 유도한 효과는 초반에 끝나기 때문에 후반부에는 최적의 선택을 90% 이상 유지하는 것을 보여줌.


### 신뢰 상한 행동 선택(Upper confidence bound, UCB)

- 행동 가치 추정에는 항상 불확실성이 있기 때문에 지속적인 탐험이 필요함
- UCB는 가치의 추정치와 불확실성을 함께 고려해 행동을 결정함

\[A_{t} = argmax [\ Q_{t}(a) + c\sqrt{\dfrac{ln\  t}{N_{t}(a)}}\ ]\]

- c는 하이퍼 파라미터이고, 루트를 포함하는 항이 추정의 불확실성을 나타낸다.

불확실성을 나타내는 항을 살펴보면

- 분자의 $ln\ t$는 시간이 지남에 따라 불확실성이 증가하도록 만들지만, 그 증가량은 시간이 흐름에 따라 감쇠
- 분모의 $N_t(a)$는 행동 a가 선택된 횟수를 나타내고, 이는 불확실성을 감소시키는 역할
- t 시점에서 많이 선택된 행동의 불확실성은 작고, 적게 선택된 행동의 불확실성은 크기 때문에 자주 선택되지 않은 행동을 취할 수 있도록 유도함

<script src="https://gist.github.com/hyeonchan523/3546da1edc81fe6423a381b0c9cfc434.js"></script>


- epsilon-greedy 방법에서는 가치 추정치가 가장 높은 값이 아닌 행동 중 랜덤하게 선택을 하는 것에 비해, UCB에서는 불확실성을 고려해 행동을 선택한다는 차이점이 있다.