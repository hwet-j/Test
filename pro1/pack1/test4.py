# 정규 표현식
# 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어. 
import re
from re import IGNORECASE

ss = '1234 abc가나다ABC_555_6_789_555kbs가나 다라 가나 정규 표현식 특정한 규칙'
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r'가나', ss))
print(re.findall(r'[0,1,3]', ss))
print(re.findall(r'[0,1,5]', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]?', ss))
print(re.findall(r'[a-z,A-Z]+', ss))
print(re.findall(r'[가-힣]+', ss))
print(re.findall(r'[가-힣]{2}', ss))
print(re.findall(r'[가-힣]{2,3}', ss))

print(re.findall(r'[^0-9]+', ss))
print(re.findall(r'^1', ss))
print(re.findall(r'^2', ss))
print(re.findall(r'칙$', ss))

print(re.findall(r'\d', ss))
print(re.findall(r'\d{2}', ss))
print(re.findall(r'\d{2,3}', ss))
# 개인적인 연습 필요