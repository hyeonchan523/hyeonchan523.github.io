---
layout: single
title:  "[Python] 유연한 matplotlib subplot 사용하기"
excerpt : "subplot 배치는 자유롭게 할 수 있다."
summary: "도시하려는 그래프마다 subplot을 새로 정의함으로써 유연한 figure를 만들 수 있다."

category : python
tags: [python, matplotlib]
toc : true
toc_sticky : true
toc_ads: true
use_math : true
---

# figure canvas를 분할하는 subplot

- 하나의 이미지에 다단으로 이미지를 삽입하고자 할 때 subplot으로 canvas를 분할하고 위치를 지정할 수 있다.

- `plt.subplot(행, 열, 인덱스)` 행과 열에서 형태를 지정하고 인덱스로 그래프를 넣을 위치를 지정하게 된다. canvas를 행과 열에 맞게 분할하고 인덱스로 figure를 삽입할 위치를 지정한다.
- 아래는 `plt.subplot(3,2,idx)`로 canvas를 분할한 예시이다.

![img]({{site.url}}/assets/img/matplotlib_subplot_frame.png)


## 고정된 분할
- 예를 들어 canvas를 4개의 행으로 분리해 4개의 figure를 그리고 싶을 때는 `plt.subplot(4,1,인덱스)`를 고정으로 사용하면 된다.

<script src="https://gist.github.com/hyeonchan523/daefe97e77e8dd8faeb49d38dc50583d.js"></script>

![img]({{site.url}}/assets/img/matplotlib_subplot_basic.png)

## 유연한 분할
- 만약 1행에는 1개의 figure를 그리고, 2행에는 3개의 figure를 그린다면 다음과 같이 하면 된다.
- 1행에 1개의 figure를 그리기 위해서는 `plt.subplot(2,1,2)`로 2개의 행으로 나누어 1번째 인덱스를 지정한다
- 2행에 삽입할 figure들은 3개의 열로 나누어야하기 때문에 `plt.subplot(2,3,idx)`로 위치를 지정해주면 된다. 
    - 그런데 여기에서 idx는 전체 canvas를 2행 3열로 나누었다고 생각하고 지정해주어야 한다.
    - 2행의 idx의 시작은 4부터 시작하기 때문에 `plt.subplot(2,3,4)`위치에 figure를 그려주면 원하는 결과를 얻을 수 있다.  

<script src="https://gist.github.com/hyeonchan523/3523920afa6ecb3b85ac5dc1f522e032.js"></script>

![img]({{site.url}}/assets/img/matplotlib_subplot_advanced.png)

# 마무리
- subplot는 시계열 데이터의 같은 시점을 비교하거나, 다수의 figure를 비교해야하는 경우에 빈번하게 사용되는 방법이다.
- 알고리즘 학습 결과를 시각화 할 때, 다른 크기의 figure를 삽입할 필요가 있었는데 이 방법으로 구현했었다.