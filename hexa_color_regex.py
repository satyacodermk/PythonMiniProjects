from operator import index
import re

from cv2 import split
#regex to detect the color code is of hex or not
"""
n=int(input("Enter the number="))
for i in range(n):
    hexcode=input("Enter the color code=")
    print(bool(re.search(reg,hexcode)))
    
st1="color:#FfFdF8; background-color:#aef;"
st2="background: -webkit-linear-gradient(top,#f9f9f9,#fff);"
#part-1] getting index of start and end for color code
print(st1.index(":"),st1.index(";"))

#part-2] printing the color code start with #  using list slicing
print("color code=",st1[(st1.index(":")+1):st1.index(";")])
#print('#' in st1)  #=> to check in string # is present or not

#part-3] to split the attributes to get all color code and printing the validation of hexa color code
st1_lst=st1.split(" ")
for i in st1_lst:
    code=i[(i.index(':')+1):i.index(';')]
    print(code,"=>",bool(re.search(reg,code)))

#part-4] doing the code for st2 to get hexacolor use same .index() method and slicing
st2_codes=(st2[(st2.index('(')+1):st2.index(')')]).split(',') 
print(st2_codes)
#spliting the value of property
for i in st2_codes:
    if "#" in i:    # note the each hexa code contains or start with "#" symbol checking process
        print(i,"=>",bool(re.search(reg,i)))    # printing code and validating hexa code


#part=5] for shortand properties
st3="border: 2px dashed #fff;"
print((st3[(st3.index(':')+1):st3.index(';')]).split(' '))
"""

# Now our  code tryal-1] goes here to validate the hexa color code in css
"""
n=int(input("Enter the number of lines="))
for i in range(n):
    sent=input()
    if ";" in sent:
        if "#" in sent:
            if sent.count(';')>1:
                prop_val=sent.split(' ')    # getting property:value; 
                print(prop_val)
                for i in prop_val:
                    if ":" in i and ";" in i:
                        val=i[(i.index(':')+1):i.index(';')]
                        if "(" in val:
                            val_lst=(val[(val.index('(')+1):val.index(')')]).split(', ') # note: to split commaspace 
                            for j in val_lst:
                                if "#" in j:
                                    if bool(re.search(reg,j)):
                                        print(j)
                        elif val.count(' ')>1:
                            val_lst=val.split(' ')
                            for k in val_lst:
                                if bool(re.search(reg,k)):
                                    print(k)
                    elif "#" in i:
                        code=i[:-1]
                        if bool(re.search(reg,code)):
                            print(code)
            else:
                val=sent[(sent.index(':')+1):sent.index(';')]
                if val.count(' ')>1:
                    val_lst=val.split(' ')
                    for l in val_lst:
                        if bool(re.search(reg,l)):
                            print(l)
                else:
                    val_without_space=val.strip()
                    if bool(re.search(reg,val_without_space)):
                        print(val_without_space)
"""
# above code is more complex so we will divide it into som parts as functions to make code more reliable and easy to understand
#major three cases for each we write 3 functions
def check(val):
    reg="^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
    flag=bool(re.search(reg,val))
    if flag:
        print(val)

def without_para(val):
    val_lst=val.split(' ')
    for i in val_lst:
        if "#" in i:
            check(i)

def with_para(val):
    val_lst=[]
    if val.count("(")>1:
        while()
    print(val_lst)
    for i in val_lst:
        check(i)
                
    

#part-1] Reading the data first and then adding the particular data into list
if __name__=="__main__":
    prop_val_lst=[]
    #n=int(input("Enter the number of lines="))
    f1=open("csstest.txt","r")
    data=f1.read()
    data_lst=data.split("\n")
    #print(data_lst)
    for sent in data_lst:
        #sent=input("").strip()
        if ("#" in sent) and (";" in sent) and(":" in sent):
            if sent.count(";")>1:
                sub_sent=sent.split(';')
                for j in sub_sent:
                    if "#" in j:
                        prop_val_lst.append(j)
            else:
                prop_val_lst.append(sent[:-1])
    #part-2] getting the value form prop_val_lst
    val_lst=[]
    for pair in prop_val_lst:
        temp=(pair[(pair.index(":")+1):]).strip() # strip() is used to remove extra spaces
        val_lst.append(temp)
    #print(val_lst)
    for i in val_lst:
        if "(" in i:
            with_para(i)
        elif i.count(" ")>1 and "(" not in i:
            without_para(i)
        else:
            check(i)


