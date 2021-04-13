import os

# old_i = 0
# for i in [1,2,2,2,2,3,4,5]:#range(0,5):
#     command_str = "working"
#     command = "start cmd /K echo " + str(i+1)

#     if old_i !=i :
#         os.system(command)

#     old_i=i
# import subprocess
# # from sh import ifconfig
# # print(ifconfig("eth0"))
# from importlib import reload
import sys

# from petshop import parrot
# from sh import vgdisplay
# print(vgdisplay())
# print (vgdisplay('-v'))
# print(vgdisplay(v=True))
# for i in range(0,5):
#     command = "start cmd /K echo " + str(i+1)
#     subprocess.run(["echo", "1"])
# def main(argv):
#     args = sys.argv[1:]
#     print(argv[1])
#     print(argv[2])
# if __name__ == "__main__":
#     main(sys.argv)    
# import multiprocessing

# result = []

# def square_list(mylist):
#     global result

#     for num in mylist:
#         result.append(num * num)
#     print("Result: {}".format(result))

# mylist = [1,2,3,4]

# p1 = multiprocessing.Process(target=square_list, args=(mylist,))
# p1.start()
# p1.join()
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))