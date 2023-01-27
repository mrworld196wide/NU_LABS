# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next1 = None
#         self.next2 = None
#         self.next3 = None
final = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def north(mat,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=mat[i][j]
    temp=t[r][c]
    t[r][c]=t[r-1][c]
    t[r-1][c]=temp
    return(t)

def south(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r+1][c]
    t[r+1][c]=temp
    return(t)

def east(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r][c+1]
    t[r][c+1]=temp
    return(t)
        
def west(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r][c-1]
    t[r][c-1]=temp
    return(t)

def findblank(mat,x):
    r=0
    for i in range(len(mat)):
        if x in mat[i]:
            r=i
            c=mat[i].index(x)
    return([r,c])

def children(mat):
    blank = findblank(mat,0)
    r = blank[0]
    c = blank[1]

    if(mat == final):
        print("Final state reached. Puzzle solved")
        return

    visited.append(mat)

    if r>=1:
        new_mat= north(mat,r,c)
        if new_mat not in seen:
            seen.append(new_mat)
    if(r<1):
        new_mat= south(mat,r,c)
        if new_mat not in seen:
            seen.append(new_mat)
    if(c>=1):
        new_mat= west(mat,r,c)
        if new_mat not in seen:
            seen.append(new_mat)
    if(c<1):
        new_mat= east(mat,r,c)
        if new_mat not in seen:
            seen.append(new_mat)
    
    for m in seen:
        if m not in visited:
            children(m)
        else:
            return
    
    return

print("Enter the initial state values with 0 as blank space: ")
current=[]
for i in range(3):
    temp = []
    for j in range(3):
        a = int(input())
        temp.append(a)
    current.append(temp)

seen =[]
visited =[]

seen.append(current)

children(current)


print(seen)
print(visited)



# print(findblank(current))

# initial=[[1,8,5],
#          [3,0,4],
#          [6,7,2]]

# initial = node(p)
# print(initial.data)

