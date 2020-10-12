import re
fhand = open("regex_sum_1018112.txt")

total = 0
for line in fhand:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    for n in num:
        n = int(n)
        total = total + n

print("Total:", total)
