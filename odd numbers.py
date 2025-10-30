N = int(input("Enter a value: "))
sum_odd = 0
for i in range (1, N+1, 2):
    sum_odd += i
print(f"Sum of odd number from 1, {N} is {sum_odd}")
