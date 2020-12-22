#file=open("test.txt", mode="w", encoding="utf-8")
#file.write("你好嗎?\n大帥哥")
#file.close()

#with open("test.txt", mode="w", encoding="utf-8") as file:
#    file.write("你好嗎?\n大帥哥")
"""
with open("test2.csv", mode="r", encoding="ANSI") as file:
    data=file.read()
print(data)
"""
"""
from time import sleep 

with open("test.txt", mode="w", encoding="utf-8") as file:
    file.write("3\n8")
sum=0
with open("test.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
"""

"""
i=0
while i <10:
    print(i)
    sleep(0.5)
    i=i+1

print(i)
"""

#import os
#import shutil

#s = "link.txt"
#t = ".\\abc\\abc.txt"

#os.rename(s,t)
#shutil.move(s, t)

with open("ucs2.rep", mode="r", encoding="utf16") as file:
    data=file.read()
print(data)

