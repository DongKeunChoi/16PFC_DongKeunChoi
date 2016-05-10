#-*-coding:utf8
print ("Let's practice everything.")
print('You \'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.' )
# \'는 따옴표안에 따옴표를 표시해주기 위해 사용 \\ 프린트는 \ , \n은 한 줄 엔터, \t는 빈칸

poem ="""
\t The lovely world
with logic so finmly planted
cnanot discern \n the nedds of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""
# 큰따옴표 세개를 연속해서 사용하여 문자열을 만들수있다.
print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print ("This should be five: %d" % five)
# %d의 사용 %d에 넣고 싶은 내용을 문자열뒤에 %내용 으로 표시.

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return  jelly_beans,jars,crates
# def 함수 정의 와 return의 사용
start_point = 10000
beans, jars, crates = secret_formula (start_point)

print("With a starting point of : %d"% start_point)
print("We'd have %d beans, %d jars, and %d crates."%(beans,jars,crates))

start_point=start_point/10

print("We can also do that this way:")
print("We'd have %d beans,%d jars, and %d crates.") % secret_formula(start_point)

