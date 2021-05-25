def MagicMatrix(n): 
    
    Matrix = [[0 for x in range(n)] for y in range(n)]    
    r = n / 2
    c = n - 1
    num = 1
    while num <= (n * n): 
        if r == -1 and c == n:  
            r = 0
            c = n - 2
        else:                     
            if r < 0:
                r = n - 1
            if c == n:
                c = 0  
        if Matrix[int(r)][int(c)]:
            r = r + 1
            c = c - 2
            continue
        else: 
            Matrix[int(r)][int(c)] = num 
            num = num + 1
            r = r - 1
            c = c + 1
    print ("Sum of each row or column: ",n * (n * n + 1) / 2, "\n") 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (Matrix[i][j]),end = '') 
             
            if j == n - 1:  
                print()
n=int(input("Number of rows of the Magic Matrix: "))
MagicMatrix(n)
