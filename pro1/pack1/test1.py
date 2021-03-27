'''
여러줄 주석
여러줄 주석 
여러줄 주석 
여러줄 주석 
'''
from future.builtins.misc import isinstance

"""
여러줄 주석 
여러줄 주석 
여러줄 주석 
여러줄 주석 
"""

# 한줄 주석
print('파이썬 세상에 오신걸 환영합니다.')
var1 = '안녕 파이썬!'
var1 = 10
print(var1)

a = 1
b = 1.2
c = b
print(a,b,c)
print(id(a), id(1), id(b), id(c)) #주소 확인함수 id()
# 파이썬은 기본형이 존재하지 않음. 참초형은 존재함.
print(a is b, a == b)  #is 주소비교, == 값 비교
print(b is c, b == c)

A = 1
a = 2
# 변수는 대소문자를 구분한다.
print(A, a, A ==a)
# for = 5 # 변수명으로 키워드 (예약어) 불가
import keyword #외부모듈 읽기 - 설치된 모듈 로딩
print(keyword.kwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async'......

print(10, oct(10), hex(10), bin(10)) # 10 0o12 0xa 0b1010  // oct - 8진수, hex - 16진수, bin - 2진수 (앞에 2자는 몇진수인지 알려줌)
print(10, 0o12, 0xa, 0b1010)

print('type 확인')
print(3, type(3))  # 3 <class 'int'>
print(3.4, type(3.4))  # 3.4 <class 'float'>
print(3 + 4j, type(3 + 4j))  # (3+4j) <class 'complex'>
print(True, type(True))  #  True <class 'bool'>
print('aa', type('aa'))  #  aa <class 'str'>
print("abc", type("abc"))  #  abc <class 'str'>

print(isinstance(1, int))  # isinstance() 객체 type 확인 함수 
print(isinstance(1.2, int))

print('-----집합형 자료형 ------')  # 알아둬아함 ! 
print((1), type((1)))  # int 집합형 자료형 아님 - 다른것과 비교하기위해 작성해놓음
print((1,), type((1,)))  # tuple
print([1], type([1]))  # list
print({1}, type({1}))  # set
print({'k':1}, type({'k':1}))  # dict

