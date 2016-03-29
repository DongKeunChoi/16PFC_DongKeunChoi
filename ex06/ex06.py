#-*-coding:cp949
x= "There are %d types of people." % 10
# x=10종류의 사람이있다.
binary = "binary"
# binary는 binary이다,
do_not = "don't"
# do_not은 don't 이다,
y = "Those who know %s and those who %s." % (binary, do_not)
# y= 2진법을 알고있는 사람들과 그렇지않은 사람들.
print x
# x를 프린트한다.
print y
# y를 프린트한다,
print "I said: %r." % x
# "나는 말했다: 10종류의 사람이있다"를 프린트한다.
print "I also said: '%s'." % y
# "또한 나는 말했다 : 진법을 알고있는 사람들과 그렇지않은 사람들."을 프린트한다.
hilarious = False
# 아주 우스운것 = 거짓
joke_evaluation = "Isn't that joke so funny?! %r"
# 농담_평가 = "이 농담이 재미있니?! 부정."
print joke_evaluation % hilarious
# 농담_평가 % 아주 우스운것
w = "This is the left side of..."
# 이것은 왼쪽 방향이다...
e = "a string with a right side."
# 문자열은 오른쪽 방향이다.
print w + e
# w 문자열과 e 문자열을 합친것을 프린트한다.