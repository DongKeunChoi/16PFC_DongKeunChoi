#-*-coding:cp949
my_name = 'DongKeun Choi'
# ���� �̸��� �ֵ����̴�.
my_age = 24 # not a lie
# ���� ���̴� 24���̴�.
my_height_cm = 175
# ���� Ű�� 175cm�̴�.
cm_to_inch = 1.0 / 2.54
my_height_inch = my_height_cm * cm_to_inch
my_weight_kg = 60
# ���� �����Դ� 60kg�̴�.
my_eyes = 'Bronw'
# ���� ���� �����̴�.
my_teeth = 'White'
# ���� �̴� �Ͼ���̴�.
my_hair = 'Black'
# ���� �Ӹ�ī���� �������̴�.
print "Let's talk about %s." % my_name
# "�ֵ��ٿ� ���ؼ� �̾߱⸦ �غ���" �� ����Ʈ�Ѵ�.
print "He's %d cm tall." % my_height_cm
# "���� Ű�� 175cm�̴�" �� ����Ʈ�Ѵ�.
print "He's %g inches tall." % my_height_inch
# "���� Ű�� 68.8976��ġ�̴�"�� ����Ʈ�Ѵ�.
print "He's %d kg heavy." % my_weight_kg
# " ���� �����Դ� 60kg�̴�"�� ����Ʈ�Ѵ�.
print "Actually that's not too heavy."
# "����� �ʹ� ���ſ���� �ƴϴ�"�� ����Ʈ�Ѵ�.
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# "�״� �������� ������ �Ӹ�ī���� �������ִ�"�� ����Ʈ�Ѵ�.
print "His teeth are usually %s depending on the coffee." % my_teeth
# "���� �̴� ���� Ŀ�ǿ� ���ϸ� �Ͼ��." �� ����Ʈ�Ѵ�.
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg)