def me (lst):
    count =0
    for i in lst:
        if i[0]==i[-1] and len(i)>2:
            count=count+1
    return count