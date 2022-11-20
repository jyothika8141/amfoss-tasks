def removeZero(lst):
    for i in lst:
        if i == 0:
            lst.remove(0)
    return lst

lst1 = []
orig_lst = []
group = int(input())

for i in range(group):
    monsters = int(input())
    health = input()
    rm_space = health.split()
    for k in rm_space:
        lst1.append(int(k))
    orig_lst.append(lst1)
    lst1 = []
 
for lst in orig_lst:
    rev_lst = lst[::-1]
    i=0
    while i < len(rev_lst)-1:
      if rev_lst[i] < 0:
         rev_lst[i]=0
      i+=1
     
    while True:
        rev_lst = removeZero(rev_lst)
        max_val = max(rev_lst)
        index = rev_lst.index(max_val)  
        if sum(rev_lst) == max_val:
            print("YES")
            break
            
        elif index == len(rev_lst) - 1:
            print("NO")
            break

        elif rev_lst[index] - (rev_lst[index + 1] * rev_lst[index + 1])  > rev_lst[index + 1]:
            j = rev_lst[index] % rev_lst[index + 1]
            rev_lst[index] = j
            
        else:
            if rev_lst[index + 1] == 0:
                rev_lst.pop(index + 1)
                
            else:
                rev_lst[index] = max_val - rev_lst[index + 1]
