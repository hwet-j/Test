# class : OOP 기법 구사
# 클래스는 새로운 이름 공간을 지원하는 단위다. 멤버는 변수, 메소드, 생성자로 구성, 접든지정지X, method overloading X
# 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고(틀), 객체(object)란 클래스로 만든 피조물을 뜻한다.

# 클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 가진다는 것이다. 
# 동일한 클래스에서 만들어진 객체들은 서로 영향을 주지 않는다. 
#  조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

# [객체와 인스턴스의 차이]
# 클래스로 만든 객체를 인스턴스라고도 한다. 
# 그렇다면 객체와 인스턴스의 차이는 무엇일까? 
# 이렇게 생각해 보자. a = Cookie() 이렇게 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다. 
# 즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다. 
# "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 "a는 Cookie의 객체"보다는 
# "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.


print('이런 저런 작업을 하다가 클래스 등장..')

def func():
    print('함수')

class TestClass : # 원형 클래스 - prototype
    abc = 1 #맴버 변수는 전역
    
    def __init__(self):
        print('생성자')
        
    def __del__(self):
        print('소멸자')
        
    def printMsg(self): # method
        name = '홍길동'    # 지역 변수
        print(name)
        print(self.abc)
        self.show()
        
    def show(self):
        print('show')
        
print(TestClass.abc)    # 원형 클래스의 멤버 변수 직접 호출
# TestClass.printMsg(self)    # # 이렇게 주면 아규먼트를 주지 않아서 ERR -> NameError : name 'self' is not defined

test = TestClass()  # 생성자 호출된 후 객체 생성(instance)
print(test.abc)
test.printMsg()     # 1. Bound method call
print('--------')

TestClass.printMsg(test)    # 2. UnBound method call
print()
print('클래스 타입 확인 :', type(1))
print('클래스 타입 확인 :', type(test))
print(id(test))
print(id(TestClass))

