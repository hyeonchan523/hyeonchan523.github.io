def level_1(value):
    return value*0.1

add_one = level_1
print(add_one(1)) # == 0.1


def level_1(value):
    return value*0.1

def level_2(value):
    return value*0.2

def level_3(value):
    return value*0.3

functions = [level_1, level_2, level_3]
incentive = []
salary = 100
# 각각 함수를 for 문을 활용해서 적용해 볼 수 있음
for func in functions:
    incentive.append(func(salary))

print(incentive)



def calculate_income(func, salary):
    return func(salary) + salary

functions = [level_1, level_2, level_3]
income = []
salary = 100
# 각각 함수를 for 문을 활용해서 적용해 볼 수 있음
for func in functions:
    income.append(calculate_income(func,salary))

print(income)


def determine_level(performance):
        # 내부함수 선언
    def level_1(value):
            return value*0.1
    
    def level_2(value):
            return value*0.2
    
    def level_3(value):
            return value*0.3


    if performance > 100 :
            return level_3
    elif performance >50 :
            return level_2
    else :
            return level_1

performance = [130, 60, 20]
income = []
salary = 100
# 각각 함수를 for 문을 활용해서 적용해 볼 수 있음
for perform in performance:
    func = determine_level(perform)
    income.append(calculate_income(func,salary))

print(income)


#%%
