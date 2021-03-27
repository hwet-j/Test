# 연산자 
v1 = 123  # 치환  
v3 = v2 = v1 
print('결과는', v1, v2, v3)  # 자동 줄바꿈
print('입니다')
print('결과는', v1, v2, v3, end='---')  # 출력 연속
print('입니다')
v4 = 1, 2, 3
print(v4, \
      type(v4))

v1, v2 = 100, 200
print(v1, v2)
v2, v1 = v1, v2  # 파이썬에서 가능한 식..(자바에서 불가능)
print(v1, v2)

print('packing - 값 할당 연산')
# v1, v2 = [1, 2, 3, 4, 5]  # 불가능 오류.
v1, *v2 = [1, 2, 3, 4, 5]
print(v1, v2)
*v1, v2 = [1, 2, 3, 4, 5]
print(v1, v2)

*v1, v2, v3 = [1, 2, 3, 4, 5]
print(v1, v2, v3)

print('\n산술, 관계 , 논리 -----------') # \n  \b  \t .... 이스케이프 문자
# 나누기에 관해서 시험출제 예정 
print(5 + 3, 5 - 3, 5 * 3, 5 / 3)
print(5 / 3, 5 // 3, 5 % 3, divmod(5, 3))  # 1.6666666666666667 1 2 (1, 2)
print(3 + 4 * 5, (3 + 4) * 5)  # () > 산술 > 관계 > 논리 > 치환

print(5 > 3,  5 == 3, 5 != 3, 5 <= 3) #관계
print(5 > 3 and 4 <= 3, 5 > 3 or 4 < 3, not(5 >= 3)) # 논리

# print('강남' + '거리' + 2021) # TypeError
# str() 괄호안의 내용을 문자열로 , int() 숫자형문자를 숫자로
print('강남' + '거리' + str(2021) + ' ' + '2000' + '21' + str(int('2000')+int('21')))
print('줘' * 10)

print('-------' * 10)
a = 5
a = a + 1
a += 1 # ++ -- 자바의 증감연산자 X
print('a :' + str(a))
print(a, a * -1, -a, --a, +a, ++a) # 부호 변경

print()
print('boolean : ', bool(False), bool(0), bool(0.0), bool(''), bool(None), bool([]), bool({}), bool(set()))
print('boolean : ', bool(True), bool(1), bool(-12), bool(1.5), bool('kbs'))

print()
print('aa\tbb')
print('aa\nbb')
print('c:\aa\nbc\kbs.txt')
print(r'c:\aa\nbc\kbs.txt') # 이스케이프 문자로 해석하지 않음 (앞에 r을 사용)

print()
print(format(1.5678, '10.3f')) 
print('나는 나이가 %d 이다.'%23) # 정수와 대응 (%d)
print('나는 나이가 %s 이다.'%'스물셋') # 문자열과 대응(%s)
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100)) # 실수와 대응(%f), 뒤에 %%를 붙여줌으로써 %하나 출력, 
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))