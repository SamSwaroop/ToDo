# def PrimeorNot(n):
#     if(n<2):
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True


    

# def output(n):
#     count=[]
#     m=0
#     i=2
#     while(n!=0):
#         if(PrimeorNot(i)):
#             if(n%i==0):
#                 n=n/i
#                 m=m+1
#             else:
#                 count.append(m)
#         else:
#             i=i+1
#     return count


# print(output(int(input())))


def PrimeorNot(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)

    

def output(n):
    k=factorial(n)
    count=[1]
    m=0
    i=2
    while(k!=1.0):
        if(PrimeorNot(i)):
            if(k%i==0):
                k=k/i
                m=m+1
                continue
            
            
            count.append(m)
            i=i+1
            m=0
        else:
            i=i+1
        
        
    return (count)


print(output(int(input())))