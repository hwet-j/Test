# 일급 객체  : 변수나 데이터에 할당 가능, 인자로 넘기기 가능, 리턴값으로 리턴하기 가능
# 일급 함수 : 함수 안에 함수 선언 가능, 인자로 함수 사용, 반환값이 함수 가능
# 함수가 다른 일급 객체와 동일하게 다루어질때, 일급 함수라고 지칭한다.
# def, lambda, filter,재귀함수, 함수장식자
# https://wjddyd66.github.io/python/Python-Function2/

def func1(a, b):
    return a + b

func2 = func1 # 함수의 주소 치환
print(func1(2,3))
print(func2(2,3))

print()
def func3(func):    # 인자로 함수 사용
    def func4():    # 함수 안에 함수 선언 가능
        print('내부 함수')
    func4()
    return func #반환값이 함수 가능

mbc = func3(func1) # 인자로 함수 사용
print(mbc(3,4))

print('\n\nLambda : 이름이 없는 한 줄 짜리 함수 ---')
# 형식 : Lambda arg, ... : 표현식 <== return 문 없이 결과 반환
def hap(x,y):
    return x + y

print(hap(2, 4))

aa = lambda x,y:x + y
print(aa(2, 4))

kbs = lambda a, su=10:a + su
print(kbs(5))
print(kbs(5, 6))

sbs = lambda a, *tu, **di : print(a, tu, di)
sbs(1,2,3, tvn=3, ytn=24)

li = [lambda a, b:a+b, lambda a, b:a*b]
print(li[0](3,4))
print(li[1](3,4))

print('다른 함수에서 인자 값으로 람다 사용 ------')
# filter(함수, 집합형자료)
print(list(filter(lambda a:a < 5, range(10))))
print(tuple(filter(lambda a:a % 2, range(10))))  # 0,1 에서 1일때가 True

print('~~~' * 10)
# 함수장식자(Decorator) 다른 함수를 감싼 함수. meta의 기능이 있다.
# 함수 장식자 사용X
def make2(fn):
    return lambda : '안녕' + fn()

def make1(fn):
    return lambda : '반가워' + fn()

def hello():
    return '신기해'

hi = make2(make1(hello))  # 괄호안의 값들은 함수의 매개변수 fn에 넣어주는것. 
print(hi())
print()

# 함수 장식자 사용
@make2
@make1
def hello2():
    return '신기루'

print(hello2())

# 함수형태() 를 작성위치
hi2 = hello2()  
print(hi2)

hi2 = hello2
print(hi2())
# 어디에도 존재하지 않으면 주소값(?)만 출력
hi2 = hello2    
print(hi2)

'''
재귀함수(Recursive Call)
계속해서 함수 자기자신을 호출하여 반복문과 같은 효과를 낼 수 있다.
계속 반복되므로 탈출 조건을 명시하여야 한다.
'''
def countDown(n):
    if n == 0 :
        print("완료")
    else :
        print(n, end = " ")
        countDown(n-1) #자기자신을 호출
countDown(5) #5 4 3 2 1 완료
