#-*-coding:cp949
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
# ���� �̰��� �������ִ�.
    "That you could type up right.",
# ����� �ùٸ��� �Է��� �� �ִ�.
    "But it didn't sing.",
# ������ �װ��� �뷡�θ�������,
    "So I said goodnight."
# �׷��� ���� goodnight �̶�� ���ߴ�.
)
