#-*-coding:cp949
x= "There are %d types of people." % 10
# x=10������ ������ִ�.
binary = "binary"
# binary�� binary�̴�,
do_not = "don't"
# do_not�� don't �̴�,
y = "Those who know %s and those who %s." % (binary, do_not)
# y= 2������ �˰��ִ� ������ �׷������� �����.
print x
# x�� ����Ʈ�Ѵ�.
print y
# y�� ����Ʈ�Ѵ�,
print "I said: %r." % x
# "���� ���ߴ�: 10������ ������ִ�"�� ����Ʈ�Ѵ�.
print "I also said: '%s'." % y
# "���� ���� ���ߴ� : ������ �˰��ִ� ������ �׷������� �����."�� ����Ʈ�Ѵ�.
hilarious = False
# ���� �콺��� = ����
joke_evaluation = "Isn't that joke so funny?! %r"
# ���_�� = "�� ����� ����ִ�?! ����."
print joke_evaluation % hilarious
# ���_�� % ���� �콺���
w = "This is the left side of..."
# �̰��� ���� �����̴�...
e = "a string with a right side."
# ���ڿ��� ������ �����̴�.
print w + e
# w ���ڿ��� e ���ڿ��� ��ģ���� ����Ʈ�Ѵ�.