import re

file = open('Actual data.txt', 'r')
summ = 0
for line in file:
    line = line.rstrip()
    if re.search('[0-9]', line):
        a = re.findall('[0-9]+', line)
        for i in a:
            summ = summ+int(i)
print(summ)

