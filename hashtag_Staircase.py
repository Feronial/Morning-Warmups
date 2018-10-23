def staircase(n):
    
    hashtag = str()
    count = 0
    
    for i in range(n,0,-1) :
        
        for k in range(i,1,-1):
            
            print(' ',end="")
        
        count += 1
        
        for m in range(count):
            
            hashtag += '#'
        
        print(hashtag)
        hashtag = str()
