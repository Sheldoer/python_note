'''算法思想：
每次排序通过交换的方法把最小的元素送到最前面，剩下的元素继续排序，
直到每个最小元素送到他该属于的位置'''
def bubblesort(alist):
    for i in range(len(alist)):
    
        j=len(alist)-1
        while j>i:
            if alist[j-1]>alist[j]:
                k=alist[j-1]
                alist[j-1]=alist[j]
                alist[j]=k
            j-=1
            
    return alist
def bubblesort2(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-1,0,-1):
            if j>i:
                if alist[j-1]>alist[j]:
                    k=alist[j-1]
                    alist[j-1]=alist[j]
                    alist[j]=k
    return alist

def main():
    alist=[]
    for i in range(int(input("你要排几个数:"))):
        alist.append(int(input("数字都包含：")))
    
    print(bubblesort2(alist))

if __name__=='__main__':
    main()
            
