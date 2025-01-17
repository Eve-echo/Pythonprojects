#WAP to check if a list contains a palindrome of elements
List=[1,"abc","abc",1,]
List.reverse()
Rev_list=List.copy()
List.reverse()
if (List==Rev_list):
    print("Palindrome")
else:
    print("Not palindrome")