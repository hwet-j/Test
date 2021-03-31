# 움직이는 기계에 사용할 부품 클래스로 핸들
# 사용자 정의 모듈

class PohamHandle:
    quantity = 0 # 회전량
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    
    