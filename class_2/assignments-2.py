# Done by me
# n=int(input("n = "))
# x=1
# while n >= x:
#     if x % 3 == 0 and x % 5 == 0 :
#         print("FizzBuzz")
#     elif x % 3 == 0 :
#         print("Fizz")
#     elif x % 5 == 0 :
#         print("Buzz")
#     else:
#         print(x)
#     x+=1

# after learning about nested loop

n=int(input("n = "))
for i in range(1, n+1):
    for j in range (1, i+1):
        if j % 3 == 0 and j % 5 == 0 :
            j= "FizzBuzz"
        elif j % 3 == 0 :
            j= "Fizz"
        elif j % 5 == 0 :
            j="Buzz"
        print(j, end=" ")
    print()

