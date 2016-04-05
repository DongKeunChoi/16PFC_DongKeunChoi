#-*-coding:cp949
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
# 나는 이것을 가지고있다.
    "That you could type up right.",
# 당신은 올바르게 입력할 수 있다.
    "But it didn't sing.",
# 하지만 그것은 노래부를수없다,
    "So I said goodnight."
# 그래서 나는 goodnight 이라고 말했다.
)
