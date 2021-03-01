    """
    `2017`年复试上机题
    **要求：**
    已知：二进制数据文件`data.bin`中存放了若干个整数，请编写程序完成如下功能：
    * 编写程序读取所有数据.
    * 以每相邻两个整数为一对按顺序构成二维平面上的坐标点. 例如：有数据`12`，`34`，`53`，`25`，`61`，`28`，`78`等，
    则构成六个坐标点如下：`(12, 34)`、`(34, 53)`，`(53, 25)`, `(25, 61)`, `(61, 28)`, `(28, 78)`；
    * 以每个坐标点为圆心，以该点与其后面第一个点的欧氏距离为半径`r`. 计算每个圆包含的坐标点数. 计
    算最后一个点时以其和第一个点的欧氏距离为半径.
      例如：
      坐标点`(12, 34)`的圆半径$r=\sqrt{(12-34)^2+(34-53)^2}$是坐标点`(12, 34)`与`(34, 53)`的欧式距离.
      坐标点`(28, 78)`的圆半径$r=\sqrt{(28-12)^2+(78-34)^2}$是坐标点`(28, 78)`与`(12, 34)`的欧式距离.
    * 计算所有圆的点密度值，然后输出点密度值最大的`5`个坐标点以及相应圆中包含的点数和点密度值. 输出格式要求：
      |     坐标点     |    包含点数     |            点密度            |
      | :------------: | :-------------: | :--------------------------: |
      | (x坐标，y坐标) | (占5列，右对齐) | (占7列，右对齐，保留2位小数) |
      上述文字部分不需要显示.
    其中：圆的点密度为圆包含的点数除以圆面积，如果点在圆上，则也算圆包含该点，在计算点密度时，圆心也算一个点. 计算圆面积时$\pi=3.14$.
    例如：坐标点`(2, 1)`，则该坐标点也属该坐标点的圆内的一个点.
    **程序：**
    :return:
    """
def read_file():
    #读取data数据，每相邻的两个整数保存到point列表里
    with open('data.txt','r')as file:
        nums=file.read().split()
    num=list(map(int,nums))
    size=len(num)
    point=[]
    for i in  range(size-1):
        point.append([num[i],num[i+1]])
    return point

def coverage(point:list):
    #对每个点进行计算与下一个点的欧氏距离，将r的平方保存到point每个点的列表里
    psize=len(point)
    for i in range(psize-1):
        r2=(point[i][0]-point[i+1][0])**2+(point[i][1]-point[i+1][1])**2
        point[i].append(r2)
    r2=(point[psize-1][0]-point[0][0])**2+(point[psize-1][1]-point[0][1])**2
    point[psize-1].append(r2)
    for i in point:
        #计算每个点覆盖点数，用n来计数
        n=0
        for j in point:
            if (i[0]-j[0])**2+(i[1]-j[1])**2<=i[2]:
                n+=1
        i.append(n)
    return point

def print_result(point:list):
    #先将point列表进行更新，将r的平方替换为点密度，根据点密度进行排序，输出前五个
    for i in point:
        i[2]=i[3]/i[2]/3.14
    point.sort(key=lambda x:x[2],reverse=True)
    for i in range(5):
        print('(%d,%d)%5d%7.2f'%(point[i][0],point[i][1],point[i][3],point[i][2]))
def main():
    point=read_file()
    point=coverage(point)
    print_result(point)

if __name__=="__main__":
    main()
