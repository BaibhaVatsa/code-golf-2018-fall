#!/usr/bin/python3
[print(i) for i in range(1,999999) if (i%3 is 0 or i%5 is 0 or i%7 is 0) and (str(i)[0] == str(i)[-1])]