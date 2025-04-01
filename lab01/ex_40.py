
    # x,y > 0
    # x // y, x % y
    # q = x // y
    # r = x % y
    # q = 0 
    # r = x 

    # while r >= y:
    #     r -= y 
    #     q += 1
    # return q, r
q = 0
r = 0
 
def Qr(x,y):
    global q    

    while True:
        x -=y
        if x > 0:
            q+= 1
        elif x < 0:
            r = x + y
            break
        else:
            q += 1
            break
    return(q,r)


# x = 10
# y = 3

# ret = Qr(x, y)
# print(ret[0], ret[1]) 








