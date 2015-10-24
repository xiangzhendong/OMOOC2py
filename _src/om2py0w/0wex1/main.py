 # -*- coding:utf-8 -*-
 mydiary=open('mydiary.txt','a')
 while True:
     content=input('-->')
     if content=='q':break
     mydiary.write(content+'\n')
  mydiary.close()
  
  for line in open('mydiary.txt'):
      print(line,end='')
      
