# -*-coding: utf8
# http://learnpythonhardway.org/book/ex38.html
ten_things="Apples Oranges Crows Telephone Light Sugar"
# 문자열에 열개의 단어가 있어야하는데, 현재 그렇지 못하다
print ("Wait there are not 10 things in that list. Let's fix that.")
#이제, 문자열을 고쳐보곘다.
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while 10 !=len(stuff):
    next_one = more_stuff.pop()
    print("Adding: %s" %next_one)
    stuff.append(next_one)
    print("There as %d items now." % len(stuff))

print("There we go : %s" % str(stuff))
print("Let's do some things with stuff")

print("stuff[1] = %s" %stuff[1])
print("stuff[-1] = %s" %stuff[-1])
print("stuff.pop() = %s" % stuff.pop())
print(' '. join(stuff))
print('#'. join(stuff[3:6]))

