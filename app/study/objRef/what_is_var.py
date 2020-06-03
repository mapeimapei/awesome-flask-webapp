a = 1
a = "abc"
#1 a贴在1上面
#2 先生成对象，然后贴便利贴

a = [1,2,3]
b= a
print( id(a),id(b))
print(a is b)

b.append(4)
print(b,a)

a = [1,2,3,4]
b = [1,2,3,4]
print( a is b)
print( id(a),id(b))
print( a== b)

#__eq__

a = 1
b = 1
print( a is b)
print( id(a),id(b))
print( a== b)


class People:
    pass

people = People()

#if type(people) is People

if isinstance(people,People):
    print("yes")











