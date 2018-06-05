# print("The number {0} in binary is {0:b}".format(255))
# print("This is %4.5f" % (2550.8943583))

for i in range(1,11):
    print("{:<4}|".format(i),end="")
    for j in range(1,11):
        print("{:>5}".format(i*j),end="")
        #print ("{0} x {1} = {2}".format(i,j,i*j))
    if i==1:
        print("\n{:-^55}".format(""),end="")
    print("")

# for i in range(1,20):
#     print("{:<4}|".format(i),end="")
#     for j in range(1,11):
#         if i<10:
#             print ("{0} x {1} = {2:<5}".format(j,i,i*j),end="")
#         else:
#             print ("{0} x {1} = {2:<4}".format(j,i,i*j),end="")
#     print("")
#     input("")
