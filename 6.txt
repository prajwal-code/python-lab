
open_list = ["[","{","("] 
close_list = ["]","}",")"] 

class parenthisis:  
    def validate(self, Str): 
        list1 = [] 
        for i in Str: 
            if i in open_list: 
                list1.append(i) 
            elif i in close_list: 
                pos = close_list.index(i) 
                if ((len(list1) > 0) and (open_list[pos] == list1[len(list1)-1])): 
                    list1.pop() 
                else: 
                    return "Invalid"
        if len(list1) == 0: 
            return "Valid"


p=parenthisis()  
string = str(input("Enter the String of parenthisis : "))
print(string," is ", p.validate(string))
