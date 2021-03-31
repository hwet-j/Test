# MariaDB의 sangpum table 자료를 웹으로 출력 
import MySQLdb
import ast

with open('cgi-bin/mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
    
print('Content-Type:text/html;charset=utf-8\n')
print('<html><body><h2>상품자료(Python 서버이용)</h2>')
print("""
<table border='1'>
<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>
""")
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    
    for a,b,c,d in datas:
        print("""
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        </tr>
        """.format(str(a), b, c, d))
    
except Exception as e:
    print('처리 오류', e)
finally:
    cursor.close()
    conn.close()
print('</table></body></html>')