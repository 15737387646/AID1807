import os

pid = os.fork()

if pid<0:
   print("Create process failed")
elif pid ==0:
   print("Child get pid",os.getpid())
   #获取当前父进程的PID
   print("Child get parent id",os.getppid())
else:
    #父进程PID返回值等于子进程的当前PID
    print("parent get child pid:",pid)
    #父进程的本身PID等于子进程获取父进程的PID创建
    print("parent get pid",os.getpid())
    