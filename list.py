# # 테스트 입니다. 코드 스페이스 2023-04-22 / 17:15
# # ipynb 는 주피터 확장자 입니다.

# import sys

# print(sys.version)

# orgPWd = int(input("id로 사용할 ID 입력 >> "))

# keyMa = 123456

# print(orgPWd ^ keyMa)

# # if 문 예시
# PM = 93

# if 151 <= PM:
#     print("... 등급 매우 나쁨")
# elif 81 <= PM:
#     print("... 등급 나쁨")
# elif 31 <= PM:
#     print("... 등급 보통")
# else:
#     print("... 등급 좋음")


# 2023-05-05

# %%
p = 'python'
y = "python"

print(p,y)

## immutanle 문자열, 정수, 실수
# p[0] = 'a' 'p' does not support item assignmentpylint(unsupported-assignment-operation)

print(id(p), id(y))
print(p is y)
print(type(p), type(y))

# %%
n = 1
print(type(n))
m = 1, # 콤마 붙으면 튜플 // m = (1, ) <== 이거와 같은 의미임
print(type(m))

# %%
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t1 == t2
# %%
t2 = (3, 2, 1)
t1 == t2
# %%
print(id(t1), id(t2))
t1 is t2

# %% 
t1 = (1, 2, 3)
# t1[0] = 1
lis = [1, 2, 3]
lis[2] = 20
lis
# 191 ~ 192 페이지 내용
# %%
help(tuple)
# %%
help(dict)
# %%
a = {'python': 1990, 'c': 1972}
type(a)
# %%
b = dict((('python', 1990), ('c', 1982)))
b
# %%
b['python'] = 1999
b['c#'] = 1992
# %%
for i in b:
    print(i)
# %%
e = dict([(list('python'), 1990)])
e
# %%
