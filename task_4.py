def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if divisors_sum == num:
        return True
    else:
        return False
    
number = int(input("Print number:"))
if is_perfect_number(number):
    print("True")
else:
    print("False")