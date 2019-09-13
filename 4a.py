def join(list1 = [], list2=[],*args):
    str3=""
    for x in range(0,4):            
        strl1=list1[x]
        strl2=list2[x]
        h1,rem1=divmod(len(strl1),2)
        h2,rem2=divmod(len(strl2),2)
        str1=strl1[:h1+rem1]
        str2=strl2[:h2+rem2]
        str3=str3+str1+str2+" "
    print (str3)
    f3=open("f3","w+")
    f3.write(str3)
def main():
    f1=open("f1","r")
    f2=open("f2","r")
    file1=f1.readline()
    file2=f2.readline()
    l1=file1.split(' ')
    l2=file2.split(' ')
    join(l1,l2)
if __name__=="__main__":
    main()
    
