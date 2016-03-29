#-*-coding:cp949
my_name = 'DongKeun Choi'
# 나의 이름은 최동근이다.
my_age = 24 # not a lie
# 나의 나이는 24살이다.
my_height_cm = 175
# 나의 키는 175cm이다.
cm_to_inch = 1.0 / 2.54
my_height_inch = my_height_cm * cm_to_inch
my_weight_kg = 60
# 나의 몸무게는 60kg이다.
my_eyes = 'Bronw'
# 나의 눈은 갈색이다.
my_teeth = 'White'
# 나의 이는 하얀색이다.
my_hair = 'Black'
# 나의 머리카락은 검은색이다.
print "Let's talk about %s." % my_name
# "최동근에 대해서 이야기를 해보자" 를 프린트한다.
print "He's %d cm tall." % my_height_cm
# "그의 키는 175cm이다" 를 프린트한다.
print "He's %g inches tall." % my_height_inch
# "그의 키는 68.8976인치이다"를 프린트한다.
print "He's %d kg heavy." % my_weight_kg
# " 그의 몸무게는 60kg이다"를 프린트한다.
print "Actually that's not too heavy."
# "사실은 너무 무거운것이 아니다"를 프린트한다.
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# "그는 갈색눈과 검은색 머리카락을 가지고있다"를 프린트한다.
print "His teeth are usually %s depending on the coffee." % my_teeth
# "그의 이는 보통 커피에 비하면 하얗다." 를 프린트한다.
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg)