#-*-coding:cp949
cars = 100
# �ڵ����� 100���̴�.
space_in_a_car = 4.0
# �ڵ����� ������ 4.0���̴�.
drivers = 30
# �����ڴ� 30���̴�.
passengers = 90
# �°��� 90���̴�.
cars_not_driven = cars - drivers
# ���� ���� ���ϴ� �ڵ����Ǽ� = �ڵ����Ǽ� - �������Ǽ�
cars_driven = drivers
# ���� �Ǵ� �ڵ����Ǽ� = �������Ǽ�
carpool_capacity = cars_driven * space_in_a_car
# īǮ �� �� �ִ� �����ο� = ���� �Ǵ� �ڵ����� * �ڵ����� ����
average_passengers_per_car = passengers / cars_driven
# �� �ڵ����� Ż �� �ִ� �°��� �� = ��� �°� / ���� �Ǵ� �ڵ���

print "There are", cars, "cars available."
# ��� ������ �ڵ����� 100���̴�.
print "There are only", drivers, "drivers available."
# �����ڴ� 30�� ���̴�.
print "There will be", cars_not_driven, "empty cars today."
# ���� �� �ڵ����� 70���ϰ��̴�.
print "We can transport", carpool_capacity, "people today."
# �츮�� ���� 120���� �ο��� ����Ҽ��ִ�.
print "We have", passengers, "to carpool today."
# �츮�� īǮ�ؾ��� �°��� 90���� �ִ�.
print "We need to put about", average_passengers_per_car, "in each car."
# �츮�� �� �ڵ����� 3���� �°��� �¿� �ʿ䰡�ִ�.