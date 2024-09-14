# question 1:
movie: int = int(input("Enter a few minutes?"))
hours: int = movie // 60
minutes: int = movie % 60
print(f"movie hours", hours, "and movie minutes", minutes)

# question 2:
## 2.1:
for a in range(0, 11):
    print(a, end=" ")
print()

##2.2:
for b in range(40, 90, 2):
    print(b, end=" ")
print()

##2.3:
for c in range(77, 112, 7):
    print(c, end=" ")
print()

##2.4:
for d in range(99, 63, -3):
    print(d, end=" ")
print()

# question 3:
##3.1:

while True:
    height: float = float(input("Enter your height?"))
    if 0.4 <= height <= 2.5:
        print(f'your height is {height}')
        break
    else:
        print("wrong input")

##3.2:
num1: int = int(input("enter a number 1?"))
num2: int = int(input("enter a number 2?"))
if num1 > num2:
    for i in range(num1, num2 - 1, -1):
        print(i, end=" ")
else:
    for i in range(num1, num2 + 1, 1):
        print(i, end=" ")
print()

##3.3:

pie: float = float(input("How much is a pie?"))
counter: int = 1
while pie != 3.14 and counter < 3:
    counter += 1
    pie: float = float(input("How much is a pie?"))
if pie == 3.14:
    print("you are correct")
else:
    print("pie is 3.14")

#3.4:
while True:
    a: int = int(input("what the number a?"))
    b: int = int(input("what the number b?"))
    c: int = int(input("what the number c?"))
    if 0 <= a <= 10 and 11 <= b <= 60 and 61 <= c <= 100 and b - a == c - b:
        print(f'{a} {b} {c}')

#etgar:
age: int = int(input("what your age?"))
beer: int = 1
while age >= 18 and beer < 10 or age < 18:
    if age >= 18:
        beer += 1
        print("You are allowed to beer")
    elif age < 18:
        print("You can't have beer")
    age: int = int(input("what your age?"))
