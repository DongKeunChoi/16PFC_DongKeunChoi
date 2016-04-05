#-*-coding:cp949
cars = 100
# 자동차는 100대이다.
space_in_a_car = 4.0
# 자동차의 공간은 4.0평이다.
drivers = 30
# 운전자는 30명이다.
passengers = 90
# 승객은 90명이다.
cars_not_driven = cars - drivers
# 운전 되지 못하는 자동차의수 = 자동차의수 - 운전자의수
cars_driven = drivers
# 운전 되는 자동차의수 = 운전자의수
carpool_capacity = cars_driven * space_in_a_car
# 카풀 할 수 있는 수용인원 = 운전 되는 자동차수 * 자동차의 공간
average_passengers_per_car = passengers / cars_driven
# 한 자동차에 탈 수 있는 승객의 수 = 모든 승객 / 운전 되는 자동차

print "There are", cars, "cars available."
# 운용 가능한 자동차가 100대이다.
print "There are only", drivers, "drivers available."
# 운전자는 30명 뿐이다.
print "There will be", cars_not_driven, "empty cars today."
# 오늘 빈 자동차는 70대일것이다.
print "We can transport", carpool_capacity, "people today."
# 우리는 오늘 120명의 인원을 운송할수있다.
print "We have", passengers, "to carpool today."
# 우리는 카풀해야할 승객이 90명이 있다.
print "We need to put about", average_passengers_per_car, "in each car."
# 우리는 각 자동차에 3명의 승객을 태울 필요가있다.