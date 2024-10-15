#s={10,30,20,40}
#s.add (30)
#print(s)#########
######update#####
s={10,20,30,40}
l={1,2,3,4}
s.update(l)
print(s)#{1,2,3,4,40,10,20,30}
##copy####
s={10,20,30}
l={1,2,3,4,5}
l=l.copy()
print(l)#####
#####pop####
s={1,2,3,4,5}
print(s.pop())
print(s)#####
####Remove####
s={40,30,10,5}
s.remove(30)
print(s)#######
###example  of remove###
s={10,20,30,40,50}
s.remove(40)
s.remove(20)
print(s)###
###discard###
s={10,20,30,40}
s.discard(30)
s.discard(20)
print(s)####
#####clear##
s={10,20,40,50,60}
s.clear()
print(s)#######
#########



