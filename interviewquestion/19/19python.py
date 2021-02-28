import math
import random
def read_file():
    # 编写函数read_file从文件中读取数据，将所有的整数按照其在文件
    #中出现的顺序依次存储到数组arr中；
    with open("data.txt",'r') as fp:
        arr=fp.read().split()
    fp.close()
    return list(map(int, arr))
def print_file(arr:list,n):
    # 编写函数print将数组arr显示在屏幕上，每行显示n个数，每个整数占6列；
    for i in range(len(arr)//n):
        for j in range(i*n,(i+1)*n):
            print('%6d'%arr[j],end='')
        print()
def count(arr):
    # 编写函数count统计数字0至9在数组arr所有整数中的出现次数，将结果放入数组res
    res=[0]*10
    for num in arr:
        if num == 0:
                res[0] += 1
        else:
            while num:
                num, h = divmod(num, 10)
                res[h] += 1
    return res
def print_res(res):
    # 编写函数print_res将数组res显示在屏幕上，每行显示5个数，可以复用步骤(2)
    print_file(res, 5)
    '''
    for i in range(0,2):
        print("%6d%6d%6d%6d%6d"%(res[i*5+0],res[i*5+1],res[i*5+2],res[i*5+3],res[i*5+4]))'''
def sort_array(arr):
    # 编写函数sort_array将数组arr中的整数按照因子和从小到大排序
    return sorted(arr)
def filter_array(arr):
    # 编写函数filter_array对数组arr中的整数进行筛选
    arr.sort()
    size=0
    for i in range(0,100):
        if arr[i]!=0 and arr[i]%2==0:
            num=arr[size]
            arr[size]=arr[i]
            arr[i]=num
            #arr[size],arr[i]=swap(arr[i],arr[size])
            size+=1
    return size
def isprime(n):
    #判断数字n是否为质数
    edg=int(math.sqrt(n))+1
    for i in range(2,edg):
        if n%i==0:
            return i
    return False
def write_file(arr,size):
    # 编写函数write_file对数组arr中的有效内容（即所有偶数）进行质因数分解
    print(arr)
    with open("output.txt",'w')as sq:
        for i in range(0,size):
            new=isprime(arr[i])
            while(new):
                sq.write(str(new)+'*')
                arr[i]=arr[i]/new
                new=isprime(arr[i])
            sq.write(str(int(arr[i]))+'\n')
    sq.close()
                
def main():
    #主函数
    with open("data.txt",'w') as fp:
        for i in range(0,100):
            fp.write(str(random.randint(0,32768))+'\n')
    fp.close()
    arr=read_file()
    print_file(arr,10)
    res=count(arr)
    print_res(res)
    #print(type(arr[0]))
    sort_array(arr)
    size=filter_array(arr)
    write_file(arr,size)
    
if __name__=='__main__':
    main()

    
