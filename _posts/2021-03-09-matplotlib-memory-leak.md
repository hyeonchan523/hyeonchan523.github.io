---
layout: single
title:  "[Python libs] matplotlib 사용시 메모리 누수"
excerpt : "matploilib로 인한 메모리 누수 방지하기"
summary: "matplotlib 라이브러리를 사용시 발생할 수 있는 메모리 누수는 plt.clf(), plt.close('all')로 방지할 수 있다."

category : python
tags: [python]
toc : true
toc_sticky : true
---
# Memory Leakage

- 프로그램이 불필요한 메모리를 점유하고 있는 것을 메모리 누수(memory leakage)<sup>[[1]]
- 메모리 누수를 발생시키는 요인 중 matplotlib 라이브러리를 사용할 때 메모리 누수가 발생하기 쉬움
- 각 iteration마다 이미지를 그리는데 필요한 메모리를 할당하고 이미지를 저장하는데 다음 iteration으로 넘어가도 해당 메모리를 점유하기 때문에 다음과 같은 경우에 메모리 누수가 발생
- 메모리 사용량 추적을 위해 다음 블로그의 코드를 사용했습니다.<sup>[[2]]

    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    memory_ = np.zeros(100)
    dummy_data = np.random.rand(100,100,100,3)
    for i in range(100):
        plt.imshow(dummy_data[i,:])
        memory_use = _check_usage_of_cpu_and_memory()
        memory_[i] = memory_use
    ```
    <img src = '{{site.url}}/assets/img/memory_leak_y.png' align = 'center'>

- 메모리 사용량이 iteration이 진행됨에 따라 꾸준히 증가하는 것을 볼 수 있음

## plt.clf()<sup>[[3]]

- figure 창 내의 plot을 지우는 방법
- 이미지를 저장한 후 plt.clf()를 붙여줌

## plt.close('all')<sup>[[3]]

- figure 창 자체를 지우는 방법
- 이미지를 저장한 후 plt.close('all')을 붙여줌

- 둘 다 memory에서 figure를 해제하는 방법이지만 특정 상황에서 memory 해제가 안되는 문제가 있음<sup>[[4]]</sup>
- 마음 편하게 둘 다 붙여주면 matplotlib 사용으로 인한 메모리 누수 문제는 해결됨
    ```python
    memory_2 = np.zeros(100)
    plt.close('all')
    plt.clf()
    dummy_data = np.random.rand(100,100,100,3)
    for i in range(100):
        plt.imshow(dummy_data[i,:])
        memory_use = _check_usage_of_cpu_and_memory()
        memory_2[i] = memory_use
    ```
    <img src = '{{site.url}}/assets/img/memory_leak_n.png' align = 'center'>
- 메모리 사용량이 증가하지 않음

# Reference

[[1]] wikipedia

[[2]]python에서 프로세스의 cpu 사용량과 memory 사용량 체크하기

[[3]]Matplotlib의 cla(), clf() 및 close() 메서드의 차이점

[[4]]Stack Overflow

[1]: https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EB%A6%AC_%EB%88%84%EC%88%98
[2]: https://helloyjam.github.io/python/check-cpu-and-memory/
[3]: https://www.delftstack.com/ko/howto/matplotlib/differences-between-cla-clf-and-close-method-in-matplotlib/
[4]: https://stackoverflow.com/questions/7101404/how-can-i-release-memory-after-creating-matplotlib-figures