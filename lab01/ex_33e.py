scores = [[90,85,93],
          [78,92,89]]

#지수의 국어 점수
# print(scores[0][1])
totall = []
for i in range(len(scores)):
    s = 0
    for j in range(len(scores[0])):
        # print(scores[i][j], ' ', end='')
        s+=scores[j][i]
        totall.append(s)
print(totall) 
      
    
#     score=[[90,85,93],
#        [78,92,89],
#        [85,56,99]  ]
# #score[0][0]+score[1][0]+
# total=[]
# for i in range(len(score)):
#     H=0
#     for j in range(len(score[i])):
#         H+=score[j][i]
#     total.append(H)

# print(total)

