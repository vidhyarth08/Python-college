def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n + natural_sum(n-1)

num = int(input("Enter the value of num to print the natural sum of the numbers : "))

print(f"The natural sum of the number is : {natural_sum(num)}")
