#https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/

# f=open("inventory.csv","r+")
# print(f.read())
# f.write("\nhello\n")
# #what you can do in read +, just read and write at start or end
# f.close()

f2=open("inventory.csv","a+")
print(f2.read())
f2.seek(3) #?? brain too tired rn check later
#f2.seek(2).write("rey\n")
f2.close()
#what you can do in write+, read write and seek

i="1234567890"
for num in i:
    print("23")