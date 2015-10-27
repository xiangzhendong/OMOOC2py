 # -*- coding:utf-8 -*-
 for line in open('mydiary.txt'):
     print(line,end='')
 
 mydiary=open('mydiary.txt','a')
 while True:
     content=input('-->')
     if content=='q':break
     mydiary.write(content+'\n')
 mydiary.close()
  
 if __name__=="__main__"
     main()
     
     
