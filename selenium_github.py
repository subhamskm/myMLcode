#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d=webdriver.Chrome()
userhandles=['subhamskm','redashu','Parnidadu','kumar-spy']
last_update=[]
for name in userhandles:
    d.get('https://www.github.com/'+name+'?tab=repositories')
    last=d.find_element_by_tag_name('relative-time').text
    print(last)
    if last.split()[0]=='a':
        num=1
    else:
        num=int(last.split()[0])
    time=0
    if last.split()[1]=='second' or last.split()[1]=='seconds':
        time=num
    elif last.split()[1]=='minute' or last.split()[1]=='minutes':
        time=num*60
    elif last.split()[1]=='hour' or last.split()[1]=='hours':
        time=num*60*60
    elif last.split()[1]=='day' or last.split()[1]=='days':
        time=num*60*60*24
    elif last.split()[1]=='month' or last.split()[1]=='months':
        time=num*60*60*24*30
    elif last.split()[1]=='year' or last.split()[1]=='years':
        time=num*60*60*24*365
    last_update.append(time)
d.close()
print (last_update)
plt.xlabel('Users')
plt.ylabel('Last commit (in seconds)')
plt.bar(userhandles,last_update)
plt.grid()
plt.show()



