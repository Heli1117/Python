# print("Hello, World!")
# a=30
# b=20
# if(a>b):
#        print(a)


# b=c=d=20
# print(d)
def greet():
    global d,name,a
    d=45
    name="hi"
    a=12
    print("Inside func",a)

greet()
print(d)
print(name)
print("Outside func",a)

