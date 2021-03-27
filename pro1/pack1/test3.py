# 집합형 자료
# 문자열 자료형 - 순서O, 수정 불가
s = 'sequence' # s = "sequence" s= """seqence"""
print(s)
print(len(s), s.count('e')) # e가 몇개 있는지
print(s.find('e'), s.find('e', 3), s.rfind('e'))
# 문자열 관련함수 다수...

ss = 'kbs'
print(ss, id(ss))
ss = 'sbs'  # 값의 일부를 변경해서 기억하는 것이 아니라 새로운 객체에 주소를 참조
print(ss, id(ss))

print('슬라이싱(집합형 자료의 일부 요소만 참조)-----')
print(s, s[0], s[2:4], s[3:])
print(s[-1], s[-4:-1], s[1:6:2])  # [1:6:2] 1부터 6까지 2번째 마다.
# s[0] = 'k' # TypeError: 'str' object does not support item assignment

ss2 = 'kbs mbc'
ss3 = ss2.split(sep=' ')
print(ss3) # ['kbs', 'mbc']

print(":".join(ss3))

a = 'life is too short'
b = a.replace("life", 'Java')
print(b)
#.................

print('\nList type : 순서O,. 여러종류의 값을 기억, 변경O [요소,.....]')
family = ['엄마', '아빠', '나', 123, 12.345]
print(family, type(family))
family.append(['삼촌', '고모'])
family.append('이모')
family.insert(0, '할머니')
family += ['아저씨']
family.remove('이모')
print(family, len(family), family.index('아빠'))
print(family[0], family[1:4])
print(family[6], family[6][1])
family[0] = '할아버지'
print(family)

print('\nTuple type : 리스트와 유사. 순서O, 변경X, 읽기 전용 (요소,...)')
# t = ('a', 'b', 'c', 'd', 'a')
t = 'a', 'b', 'c', 'd','a' # 굳이 괄호를 안써줘도되지만 가독성을 위해 괄호를 작성해준다.
print(t, type(t), len(t), t.count('a'))
print(t[1], t[2:5])
# t[1] = 'k'  # TypeError: 'tuple' object does not support item assignment
imsi = list(t) # 형 변환 후 값 변경 가능
print(imsi, type(imsi))
imsi[1] = 'kbs'
t = tuple(imsi)
print(t, type(t))
t1 = (10,)
t1 = (10, 20)
a, b = t1
b, a = a, b
t2 = a, b
print(t2)

print('\nSet type : 순서X, 변경X, 중복X, {요소,...}')
a = {1, 2, 3, 1}
print(a,type(a), len(a))
# print(a[0])  # TypeError: 'set' object is not subscriptable
b = {3, 4}
print(a.union(b), a.intersection(b))
print(a | b, a - b, a & b)  # 합, 차, 교집합
b.update({6, 7})
print(b)
b.update([8, 9])
b.update((10, 11))
print(b)
b.discard(4)
b.discard(4)  # 있으면 삭제 없으면 없는데로 스킵
print(b)
b.remove(7)
# b.remove(7)  # 있으면 삭제 없으면 에러 
print(b)
b.clear()
print(b) # set()이라는 결과가 나옴 - 비어있다는 의미

li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2]
print(li)
# 중복제거
im = set(li) 
li = list(im)
print(li)

print('\nDict type : 순서X, {key:value,...}')
mydic = dict(ki=1, k2='kbs', k3=1.23)
print(mydic, type(mydic))

dic = {'파이썬':'뱀','자바':'커피','스프링':'봄'}
print(dic, type(dic))
print(dic['자바']) # 키로 값을 참조
# print(



