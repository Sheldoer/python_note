'''算法思想：
基于划分的方法，选择一个元素，经过左右对调比较，找到它应该在的位置
然后对该元素左右两侧进行快速排序
'''
def part(blist,low,high):
    mid=blist[low]
    while low<high:
        while low<high and blist[high]>=mid:
            high-=1
        blist[low]=blist[high]
        while low<high and blist[low]<=mid:
            low+=1
        blist[high]=blist[low]
    blist[low]=mid
    return low
def quicksort(blist,low,high):
    if low<high:
        mid=part(blist,low,high)
        quicksort(blist,low,mid-1)
        quicksort(blist,mid+1,high)

def main():
    blist=[]
    for i in range(int(input("你要排几个数:"))):
        blist.append(int(input("数字都包含：")))
    quicksort(blist,0,len(blist)-1)
    print(blist)

if __name__=='__main__':
    main()
            
    
