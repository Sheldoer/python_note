'''算法思想：根据堆排序来选择最大的数到堆顶，然后将最大的数与最后一个数进行交换
剩下的数继续进行堆排序，直到结束

'''
def adjustdown(clist,k,length):
    j=clist[k]
    i=2*k+1
    while i<length:
        if i<length-1 and clist[i]<clist[i+1]:
            i+=1
        if j>=clist[i]:
            break
        else:
            clist[k]=clist[i]
            k=i
        i*=2
    clist[k]=j

def buildmaxheap(clist,length):
    for i in range(int(length/2),-1,-1):
        adjustdown(clist,i,length)
def heapsort(clist):
    buildmaxheap(clist,len(clist))
    for i in range(len(clist)-1,-1,-1):
        j=clist[i]
        clist[i]=clist[0]
        clist[0]=j
        adjustdown(clist,0,i-1)

def main():
    clist=[]
    for i in range(int(input("你要排几个数:"))):
        clist.append(int(input("数字都包含：")))
    heapsort(clist)
    print(clist)

if __name__=='__main__':
    main()
