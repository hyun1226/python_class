# 출력
# print(123)
print("Hello World")
a=5
print(a)
# int : 정수 (-1, 0, 1)
# float : 실수 (1.2, 2.5)
# str : 문자 ('hello')
print(type(a))
print(type(1.2))
print(type('hello'))
# 파이썬 입력은 str
# b = input()
# print(b)
# print(type(b))
# hap = b + b
# print(hap)
# 입력은 정수로
# b = int(input())
# print(type(b))
# hap = b + b
# print(hap)
# 반복문
for i in range(0,10):
    print(i,"Hello")
#  연산자
#  +,-,/,*,%
a = 4
b =2
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
# bool
# 참 : 1(true), 거짓 : 0(false)
print(type(1==2))
print(1==1)

# list
a = [1,2,3,4,5]
print(type(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print("-----")
for i in range(0,5):
    print(a[i])
# 리스트의 합 구하기(for문)
print("-----")
hap = 0
for i in a:
    print(i)
    hap = hap + i

print(hap)

# 리스트의 합 구하기(함수)
print(sum(a))

# 리스트 정렬하기
a = [5,4,3,2,1]
a = sorted(a)
print(a)

# 리스트의 길이 구하기(함수)
print("-----")
print(len(a))

# 리스트에 값 추가하기
print("-----")
hyun = [100, 95, 100]
minji = [80, 90, 95]

print(hyun,minji)

hyun.append(100)
minji.append(100)

print(hyun,minji)

del minji[1]

print(minji)

hyun.remove(95)
print(hyun)

print(hyun.count(100))

# if문
print("-----")

minji.append(25)
hyun_sum = sum(hyun)
minji_sum = sum(minji)

print(hyun)
print(hyun_sum)
print(minji)
print(minji_sum)


if hyun_sum > minji_sum:
    print("hyun : A")
    print("minji : B")
elif hyun_sum == minji_sum:
    print("hyun : A")
    print("minji : A")
else:
    print("hyun : B")
    print("minji : A")
