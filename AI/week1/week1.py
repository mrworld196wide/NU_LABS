def strength(m):
    strength_x = 0
    strength_o = 0
    
    #diagonal 
    freq_x = 0
    freq_o = 0
    for i in range(3):
        if(m[i][i] == 'x'):
            freq_x+=1
        elif(m[i][i] == 'o'):
            freq_o+=1
    if(freq_x - freq_o > 0):
        strength_x += freq_x - freq_o
    else:
        strength_o += freq_o - freq_x

    #cross diagonal
    for i in range(3):
        freq_x = 0
        freq_o = 0
        for j in range(3):
            if(m[i][j]=='x'):
                freq_x+=1
            elif(m[i][j]=='o'):
                freq_o+=1
        if(freq_x - freq_o > 0):
            stx += freq_x - freq_o
        else:
            sto += freq_o - freq_x

    #column 
    for i in range(3):
        freq_x = 0
        freq_o = 0
        for j in range(3):
            if(m[j][i]=='x'):
                freq_x+=1
            elif(m[j][i]=='o'):
                freq_o+=1
        if(freq_x - freq_o > 0):
            stx += freq_x - freq_o
        else:
            sto += freq_o - freq_x
    
    
    
    
    freq_x = 0
    freq_o = 0
    for i in range(3):
        if(m[i][2-i] == 'x'):
            freq_x+=1
        elif(m[i][2-i] == 'o'):
            freq_o+=1
    if(freq_x - freq_o > 0):
        strength_x += freq_x - freq_o
    else:
        strength_o += freq_o - freq_x
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("X strength :",strength_x-strength_o)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("O strength:",strength_o-strength_x)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
m = []
for i in range(3):
    a = []
    for j in range(3):
        a.append(input("enter the data:"))
    m.append(a)
strength(m)