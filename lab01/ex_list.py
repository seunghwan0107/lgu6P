# # # shoplist = ['apple', 'mango','carrot', 'banana']
# # # print(shoplist)
# # # print(type(shoplist))

# # # print(list(range(5)))

# # # #for i in range(5):
# # # for i in list(range(5)):
# # #     print(i)

# # # ########################################################
# # # #자주쓰는 기능
# # # #######################################################

# # # shoplist[0] = 'melonn'
# # # print(shoplist)

# # # #값 바꾸는거 가능

# # # shoplist.append('lego')
# # # print(shoplist)

# # # #append는 list에 추가하는기능

# # # #리스트나 시퀀스 추가
# # # shoplist.extend(['소고기','닭고기'])
# # # print(shoplist)
# # # #리스트가 추가된거라 소고기 닭고기가 두개씩나옴

# # # print(shoplist + ['소고기','닭고기'])
# # # print(shoplist)
# # # #더하기 기능이라 대입을 하지 않아서 원래값은 안바뀜

# # # #제거 remove(value)
# # # shoplist.remove('소고기')
# # # print(shoplist)

# # # #제거 del index
# # # del shoplist[0]
# # # print(shoplist)

# # # #index
# # # i = shoplist.index('banana')
# # # print(i)

# # # #len 리스트의 길이
# # # print(len(shoplist))

# # # #빈 리스트
# # # # L = []

# # #정렬
# # L =[3,5,2,1,0,4]
# # L.sort()
# # print(L)

# # # L.sort(reverse=True) 역순

# # L =[3,5,2,1,0,4]
# # L_sorted = sorted(L)
# # print(L)
# # print(L_sorted)

# # # L_sorted = sorted(L,reverse=True) 역순

# # #########################################################
# #인덱싱과 슬라이싱
# #    0 1 2 3 4 5 6 7 정방향index
# L = [1,2,3,4,5,6,7,8]
# #   -8-7-6-5-4-3-2-1 역방향index
# print(L[3])

# #indexError
# # print(L[8])

# print(L[-1])

# i = -1
# print(L[i])

# #슬라이싱
# #L[start:end:stride] end는 마지막수 포함x

# print(L[1:7:1])

# #셋다 생략
# print(L[::])

# #start,stride 생략
# print(L[:3])

# #end,stride 생략
# print(L[3:])

# #start,end 생략
# print(L[::2])

# #음수인덱스를 사용한 슬라이싱
# print(L[-3:])

# print(L[-7:-4:1])

# print(L[-2:-6:-1])

###############################################
# # 다른 자료형을 담고있는 리스트
L = [1, 'foo', True, 3.14,(1,2)]
print(L)
t = L[4]
print(t[1])
print(L[4][0])

L = [[1,2,3],[4,5,6]]

print(L[1][0])
print(L[0][2])