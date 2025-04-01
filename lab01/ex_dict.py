d = {
    'foo' : 'foo@naver.com',
    'bar' : 'bar@gmail.com',
    'egg' : 'egg@kakao.com'
   
 }

#인덱스값으로 조회 불가 d[0]
print(d['foo'])
#삭제
del d['foo']
print(d)
#추가
d['foo'] = 'foo@naver.com'
print(d)
#기존값 업데이트
d['foo'] = 'foo@kdt.com.kr'
print(d)

d['list'] = [1,2,3,4,5]
print(d)

print(d.keys())

for key in d.keys():
    print(d[key])

for key in d:
    print(d[key])

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)


# for key, value in d.item():
#     print(key, value)

# print(d.item())


#키 없음을 방지하는 방법
print(d.get('bar','없어요'))
if d.get('bar','없어요') == '없어요':
    print("조회하신 키가 없습니다.")
else:
    #키를 이용한 작업...
    pass

from collections import defaultdict

dd = defaultdict(int)
print(dd)
print(dd['a'])

dd = defaultdict(list)
print(dd)
print(dd['a'])

dd['a'].append('a')
print(dd)