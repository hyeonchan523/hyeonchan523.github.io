---
layout: single
title:  "[Python] matplotlib 테마 설정하기"
excerpt : "같은 값이면 다홍치마라고 했다."
summary: "한 줄의 명령어로 matplotlib style 바꾸기"

category : python
tags: [python, matplotlib]
toc : true
toc_sticky : true
toc_ads: true
use_math : true
---

# Matplotlib style

- matplotlib을 기본의 기본 설정을 사용하면 다소 투박한 배경에 그래프가 그려진다.
- 우연히 python에서 ggplot을 사용해 그린 그래프를 보고 아름답다고 생각을 해 다른 라이브러리를 공부해보려고 생각했다.
- 필요한 기능의 대부분을 matplotlib으로 해결을 할 수 있다보니 다른 라이브러리를 공부하는 것을 계속 미루던 참에 matplotlib의 style을 바꿀 수 있는 방법을 발견했다.

## Seaborn style 사용하기

- matplotlib 외에 처음 알게 된 라이브러리는 seaborn이다.
- seaborn은 matplotlib에 기반해 좀 더 아름답고 효과적으로 데이터 시각화를 도와주는 라이브러리이다.
- seaborn은 5가지 기본 테마를 제공한다. `sns.set_style('테마')`로 스타일을 지정할 수 있다.
- 이렇게 스타일을 지정한 후 matplotlib 라이브러리르 사용해서 그래프를 그리면 지정한 스타일이 적용된 그래프를 그릴 수 있다.

![img]({{site.url}}/assets/img/seaborn_style.png)

## Matplotlib style 사용하기

- matplotlib에서 seaborn style을 포함한 여러가지 style을 제공한다.
- 사용가능한 style의 목록은 `plt.style.available`을 통해서 확인할 수 있다.
- 스타일을 적용할 때는 `plt.use.style('테마')`로 적용해 줄 수 있다.

![img]({{site.url}}/assets/img/mpl_style.png)

# 마무리

- 큰 데이터를 다룰 때 seaborn이 matplotlib에 비해 시간이 많이 걸리는데 간단한 line plot이나 scatter plot을 그릴 때, 이 방법으로 스타일을 적용하면 좋을 것 같다.
    - 참고로 예제의 그래프를 그리는데 걸린 시간은 matplotlib이 806$\mu s$, seaborn이 19.2$ms$으로 seaborn이 약 24배의 시간이 더 소요됐다.
    - 50 point의 데이터를 사용해 느끼기 어려운 차이지만 데이터 포인트 수가 늘어나면 이 차이는 더 심해진다.
- 그럼에도 seaborn 정도는 꼭 익혀두어야 이후에 보고서나 발표 자료의 질을 높힐 수 있을 것 같다.
- 21년 하반기에 [seaborn][2]과 [plotly][3] 공부를 시작하려고 한다.

**포스팅에 사용된 코드**


[[1]] matplotlib customizeing  

<script src="https://gist.github.com/hyeonchan523/467fc2ac5d0cfa2a8d3bde6d56cef471.js"></script>


[1]:https://matplotlib.org/stable/tutorials/introductory/customizing.html
[2]:https://seaborn.pydata.org/
[3]:https://plotly.com/