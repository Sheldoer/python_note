def read_file():
    with open("input.txt",'r') as fp:
        words=list(fp.read().split())
    fp.close()
    word=list(set(words))
    count=[]
    for i in word:
        count.append(words.count(i))
    with open("output.txt",'w')as fp:
        for i in range(len(count)):
            if count[i]>1:
                fp.write(str(word[i])+':'+str(count[i])+'\n')
    fp.close()

def main():
    read_file()

if __name__=="__main__":
    main()
    with open("output.txt",'r')as fp:
        print(fp.read())
    fp.close()

    
