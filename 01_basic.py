print("salam sharif")

str1 = "sam"
print(str1)         # sam
print(type(str1))   # str

a = "10"            
print(a)            # 10
print(type(a))      # str

b = 20              
print(type(b))      # int

s = True
print(type(s))      # boolean

v = False
print(type(v))      # boolean

n = "False"
print(n)            # False
print(type(n))      #str

print(a,b,s,v,n,)   # 10 20 True False False

name = "sharifur rahman"
age = 20
marks = 82.876
print(name , "is", age , "years old and got the", marks ,
      "marks")                                                                # sharifur rahman is 20 years old and got the 82.876 marks
print("%s is %d years old and got the %f marks" %(name,age,marks))            # sharifur rahman is 20 years old and got the 82.876 marks

print(type(name))    # str
print(type(age))     # int
print(type(marks))   # float

print(f"{name} is {age} year old and got the {marks} marks")                 # sharifur rahman is 20 years old and got the 82.876 marks

print("%s is %d years old and got the %2f marks" %(name,age,marks))            # sharifur rahman is 20 years old and got the 82.876 marks

str1 = "sharif"
print(type(str1))          # string
name = " rahman"
print(str1 + name)         # sharifur rahman

k = 12
l = 34
print(k>l)                 # False
print(k==l)                # False
print(k<l)                 # True


b = input("entert the number : ")
b = int(b)
print(b , type(b))                          # n = 60
d = b + 90             
print(d)                                    # n+ 90 = 150

c = input ("Enter your name :" )            # sharif
print(f"Hello {c} ")                        # Hello sharif

is_number = bool(int(input("Are you member press 1 for yes 0 for no : ")))  #1
print("Membership status", is_number)       # Member status True
                
name = input("Enter the name and age : ")  
print(name)                                 # sharif , 19

name_age = input("Enter the name and age : press , to separate ")  # sharif , 20
name, age = name_age.split(",")
print("name",name)                                #  sharif
print("age",age)                                 # 20