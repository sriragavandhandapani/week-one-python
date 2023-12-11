'''f=open("data.txt","w")
a=input("enter data: ")
print(f.write(a))
f.close()
f=open("data.txt","r")
print(f.read(5))'''

'''f=open("data.txt","a")
f.write("hello")'''

'''f=open("data2.txt","r+")
print(f.readline())
print(f.tell())'''

f=open("data.text","r+")
f.seek(10)
data=f.read(6)
f1=open("data3.text","w")
f2.write(data)
