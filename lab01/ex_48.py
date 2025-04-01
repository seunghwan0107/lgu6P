# with open("file_w.txt","w",encoding="utf-8") as f:
#     f.write("hello python\n")
#     f.write("안녕 파이썬")

# with open("file_w.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines,type(lines))
#     for line in lines:
#         print(line,end ='')
        # 줄바꿈 지가해서 막아줘야함
import ex_45
import os

input_files = os.listdir('./data')

with open('ex_48.txt','w') as fw:

    for file in input_files:
        # print(file, type(file),file[-3:])
        if file[-3:] == 'txt':
            print(file)
            scores=[]
            name = file[:-4]
            with open(f"./data/{file}",'r',encoding='utf-8') as f:
                lines = (f.readlines())
                # readlines가 str문자임으로 int로 바꿔야함
                # 그게 아래작업
                for line in lines:
                    scores.append(int(line))
            print(scores)
            # print(ex_45.mean(scores),ex_45.std(scores))
            m = ex_45.mean(scores)
            sigma = ex_45.std(scores)
            fw.write(f"{name:>10}: {m}, {sigma}\n")
            




    
    



    