---
layout: single
title:  "[Python] jupyter module autoreload"
excerpt : "노트북 파일에 작업할 때, kernel을 restart하지 않고 수정사항을 반영할 수 있는 autoreload"
summary: "%autoreload로 모듈 수정사항 자동으로 반영하기"

category : python
tags: [python, jupyter, autoreload]
toc : true
toc_sticky : true
toc_ads: true
use_math : true
---

# jupyter notebook의 module load

- jupyter lab이나 notebook을 사용할 때 가장 불편했던 점이 어느 정도 프로젝트가 진행 된 후 자주 사용되는 함수들을 모듈화 시켜 `.py` 파일로 저장했을 때, py 파일을 수정했을 때 kernel을 재시작해야 반영이 되는 점이었다.
- 노트북에 두 줄의 코드를 입력하는 것으로 커널을 매번 재시작하지 않고 모듈의 수정사항을 반영할 수 있다.


<script src="https://gist.github.com/hyeonchan523/483e084fa0d3392ae7e58621828fc53f.js"></script>

# Reference

[[1]] ipython autoreload document
        


[1]:https://ipython.org/ipython-doc/3/config/extensions/autoreload.html
