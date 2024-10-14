#Octal To Decimal Conversion
# Method 1:
def OctalToDecimal(num):
    decimal_value = 0
    base = 1

    while num:
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value


octal = 512
print("The decimal value of",octal, " is",OctalToDecimal(octal))


#Method 2 : Inbuilt Method

octal_num = 512

decimal_value = int(str(octal_num), 8)

print("The decimal value of {} is {}".format(octal_num, decimal_value))