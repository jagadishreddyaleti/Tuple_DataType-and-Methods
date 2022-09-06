# a=10
# print(type(a))

# a=10,
# print(type(a))  #tuple

# pc=('apple','reliance','asus','dell')
# pc[1]='motorola'
# print(a)     # type error 'tuple object does not support item assignment

# n=('hello','world')
# # print(type(n))
# print(n[0])
# print(n[1])
# # print(n[2])


# v=(1,4.2,'hello',[2,3],('h','d'),None,True)
# print(v,type(v))
# v[0]=2
# print(type(v))


''' count '''

# v=(1,4.2,'hello',[2,7],('h','d'),4.2)
# print(v.count(4.2))
# print(v.count([2,7]))

''' index''' 

v=(1,4.2,'hello',[2,7],('h','d'),4.2)
print(v.index('hello'))
