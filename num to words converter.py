
ones = ["", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"]

teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"]

num = int(input("Enter a number (0-999): "))

if num == 0:
    print("Zero")
elif num < 10:
    print(ones[num])
elif num < 20:
    print(teens[num - 10])
elif num < 100:
    print(tens[num // 10] + " " + ones[num % 10])
else:
    result = ones[num // 100] + " Hundred"
    remainder = num % 100

    if remainder >= 20:
        result += " " + tens[remainder // 10]
        if remainder % 10 != 0:
            result += " " + ones[remainder % 10]
    elif remainder >= 10:
        result += " " + teens[remainder - 10]
    elif remainder != 0:
        result += " " + ones[remainder]


Enter a number (0-999): 247
Two Hundred Forty Seven

