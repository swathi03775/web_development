
#### dict operators##
#d={}
#print(type(d))
#d[100]='swathi'
#d[200]='mouni'
#d[300]='priya'
#d[400]='bhuvana'
#print(d)#####
##how to access data from the dict?
#d={100:'sunny',200:'swathi',300:'bujji'}
#print(d[100])
#print(d[200])####
###w.a.p to enter name an % of marks in a dict and display information of the screen
#
        ##print ('\t',x,'\t\t',rec[x])#####
################ 
#key points###
#d1=dict({100:'sinny',200:'swathi',300:'priya'})
#print(d1)#{100: 'sinny', 200: 'swathi', 300: 'priya'}
#d2=dict([(33,'katrina'),(66,'swathi'),(56,'priya')])
#print(d2)#{33: 'katrina', 66: 'swathi', 56: 'priya'}
#d3=dict((('a','apple'),('b','ball'),('c','cat')))
#print(d3)####{'a': 'apple', 'b': 'ball', 'c': 'cat'}
#len function##
#d1=[("swati","a"),("priya","b")]
#print(len(d1))###2
###clear function
#d1=[("sri","a"),("vijji","b"),("swathi","c")]
#d1.clear()
#print(d1)#[]
######get functipon
#d1={'satvi':'a','sri':'b','vijji':'c'}
#d1.get('a')
##print(d1)
##pop function##
####d1={1,4,5,6,7,8,8,9}
##d1.pop()
##print(d1)
#pop item
#d1={1:"swathi",2:"pinky"}
#print(d1.popitem())
#print(d1)
##value##
### first question#
#a=45
##f=78
#c=a|f
#print(c)
### we take o+ne variable with common values and next we take another variable with common variable 
## finally both variable take only one  common variables.
#set1={2,3,4,7,8,9}
#set2={1,2,3,4,5,6}
#set=set1.intersection(set2)
#print(set))
#a4b3c2###
s='a4b3c6'
previous=''
for x in s:
    if x.isalpha():
        previous+=x
        output =x
    else:
        previous+=(output*(int(x)-1))
print(previous)
        