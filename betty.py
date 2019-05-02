def darab(a):
    great = 0
    db = 0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            true = 0
            for k in range(j,i,-1):
                if a[i] < a[j] and a[k] < a[j]:
                    true += 1
                    print(k)
                if true == k:
                    db += 1
    if db > great:
        great = db
    return great
    
a = [1,2,3]

print(darab(a))
