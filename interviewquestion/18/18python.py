from math import sqrt
from random import randint
def isprime(n:int):
    if n==2 or n==1:
        return True
    if n==0:
        return False
    edg=int(sqrt(n))+1
    for i in range(2,edg):
        if n%i==0:
            return False
    return True

def find_list(arr:list):
    out_list=[]
    #print(arr)
    arr=list(set(arr))
    #print(arr)
    for i in range(len(arr)):
        if isprime(arr[i]):
            out_list.append(arr[i])
    return out_list

def main():
    arr=[]
    for i in range(20000):
        arr.append(randint(0,32768))
    print(find_list(arr))
if __name__=='__main__':
    main()
