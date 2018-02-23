import sys
digit_string = sys.argv[1]

sum = 0
for char in digit_string:
    sum += int(char)
print(sum)