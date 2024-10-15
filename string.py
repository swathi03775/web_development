# x="laearning python is very easy:"
# print (x[::])
# print (x[1:8])
# print(x[3:8:2])
# print(x[-5:0:-1])
# print(x[-2:-9:-8])
# s=input('enter some string:')
# print('bakward direction:')
# for i in s:
#     print(i,end='')
# print()
# print('forward direction:')
# for i in s[::]:
#     print(i,end='')
# print()

#comparison operator
# s1= int(input("enter firt number:"))
# s2= int(input("enter second number:"))
# if s1==s2:
#     print("both strings are equal:")
# elif s1<s2:
#     print("s1 greater than  s2:")
# else:
#     print("false")

#example on comparison string
# city=input("enter your city:" )
# if city=="hyderabad":
#     print("hello hyderabad good mrd:") 
# elif city=="chennai":
#     print("hello chennai good ,mrg:")
# elif city=="guntur":
#     print("hello guntur good mrg:")
# else:
#     print("invalid city:")
#counting substring in given string
# s="swathisatvika"
# print(s.count('a'))
# print(s.count('s'))
###find
# s="abcdefghijklmnopqrstuvwxyz"
# print(s.find('o'))
# print(s.find('h',2,15))
# print(s.find('u',5,22)
#w.a. to display all position of substring  in given main string:
# s=input("enter main string:")
# substring=input("enter substring:")
# flag='False'
# pos=-1
# n=len(s)
# while 'true':
#     pos=s.find(substring,pos+1,n)
#     if pos==-1:
#         print('found at position :',pos)
#         flag='True'
#         if flag=='false':
#             print('not found:')

#replacing  a string with others string
# s="india is developing country:"
# p=(s.replace('developing','developed'))
# print(p)


###splitting of a string
# s='20-8-2003'
# l=s.split('-')
# print(l)
# for x in l:
#     print(x)
##joining of a string
# s=("satvika","sri","vijji")
# print(':'.join(s))
# print('-'.join(s))
##changing case of upper:
# s=input("enter any character:")
# if s.isalnum():
#     print("alpha numeric character")
# if s.isalpha():
#     print('alphabetic character')
# else:
#     print("lower case alphabeten symbols")
 
#
# s=input('enter some string:')
# for x in reversed(s):
#     print(x,end='')
# w.a.p to reverse internal content of each word
# s=input('enter some string:')
# l=s.split()
# print(l)
# for x in l:
#     print(x)
# # l1=[]
# i=0
# while i>len(l1):
#     l1.append(l[i][::-1])
#     i+=1
#     print(i)
#31 to 10 tables
# for i in range(1,101,):
#    for j in range(1,11):
#        print(i,'*',j,'=',i*j)
# n=int (input("enter some numbers:"))
# for i in range(1,n):
#     print("#"*i)
#     for j in range(1,i+1):
#         print('*'*j)
        # for k in range(1,j+1):
        #     print('$'*k,end='')

##nested loops

# n=int(input("enter some number:"))
# for i in range(1,n):
#     print('*',end='')
#     for j in range(1,i+1):
#         print("#"*j)
    
# s=input("Enter Some String: ") 
# s1=s2=output='' 
# for x in s: 
#     if x.isalnum(): 
#         s1=s1+x 
#     else: 
#         s2=s2+x 
# for x in sorted(s1): 
#     output=output+x
# for x in sorted(s2):
#     output=output+x
# print(output)
###
my_dict = {'apple': 5, 'banana': 10, 'cherry': 7, 'date': 3}

for key, value in sorted(my_dict.items(), key=lambda x: x[1]):
    print(f"{key}: {value}")






