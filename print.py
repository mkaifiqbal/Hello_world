//print("Hello World")
str = "hello world"
new=""

for j in range(0,len(str)):
    for i in range(97,123):
        if str[j]==" ":
            new+=" "
            print(new)
            break
        elif chr(i)==str[j]:
            new += str[j]
            print(new)
            break
        else:
            print(new+chr(i))
