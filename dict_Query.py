iter_Number = int(input())
phone_Book = dict()
query_List = list()


for i in range(iter_Number) :
    
    entry = list(map(str, input().split()))
    
    phone_Book[entry[0]] = entry[1]
    

for m in range(iter_Number) :
    
    query = str(input())
    
    if query in phone_Book:
        print(query + '=' + phone_Book[query])
        
    else:
        print('Not found')
