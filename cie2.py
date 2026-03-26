n = int(input("Enter number: "))

original = n
num_digits = len(str(n))
result = 0

while n > 0:
    digit = n % 10
    result += digit ** num_digits
    n //= 10

if result == original:
    print("Is an Armstrong Number")
else:
    print("Not an Armstrong Number")