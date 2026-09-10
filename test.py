#print(“hello”) ; a=int(input(“enter number”)) ; s=input(“enter string”);
#if(a==1):
#print(“1”)
#Else:
#print(a)
#elif(between else and if)

lesson_6='''

a=int(input("enter number: "))
b=int(input("enter another number: "))

print("Logical AND:", a and b)
print("Logical OR:", a or b)

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
logical =(a and b)+ (a or b)+(bool(a!=b))
bitwise =(a & b)+(a | b)+(a ^ b)
print("logical: ", logical)
print("bitwise: ", bitwise)

t=(a and b)
s= ( a & b)
'''

lesson_7='''

text=input("Enter text: ")
asci_text=ord(text)
new_text=asci_text+3
print("Encrypted text: ", chr(new_text))
numbers = list(map(int, input().split()))

encripted_word=""
word="Hello"
for char in word:
    if char.islower():
        asci_text=ord(char)
        new_text=asci_text+3
        print("Encrypted text: ", chr(new_text))
        encripted_word+=chr(new_text)
    else:
        encripted_word+=char
print(encripted_word)


numbers=[1,2,3,4,5,6]
numbers.append(7)
numbers.insert(1,10)
numbers.sort()
numbers.pop()
numbers.sort(reverse=True)
numbers.remove(1)
orianebi=numbers.count(2)
print(orianebi)
print(numbers)
print(len(numbers))
numbers_1= list(map(int, input().split()))

'''
# numbers = [1,2,3,4,5,6]

numbers=list(map(int, input().split()))

def count_even(numbers):
    count=1001
    for i in numbers:
        if i%2==0:
            if i<count:
                count=i
    if(count>0):
        return count
    else:
        return -1
print(count_even(numbers))