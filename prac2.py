# NUM1 list NUM1 has some integer numbers. Write down NUM1 program to prepare NUM1 stack of odd integers from the given list NUM1. The program should have user- defined functions which perform the following operations based on this list.
# •	Traverse the content of the list and push the ODD numbers onto the stack.
# •	Pop and display the content of the stack.
NUM1 = []
oddlist=[]
top = None
def inp():
    n = int(input('Enter size of list : '))
    for i in range(n):
        k = int(input(f'Enter element {i+1} : '))
        NUM1.append(k)
    print('List appended sucessfully')

def emp(dum):
    if dum ==[]:
        return True
    else:
        return False

def Odd(dum):
    for i in dum:
        if i%2!=0:
            oddlist.append(i)

def push(dum,item):
    dum.append(item)
    top = len(dum)-1

def POP(dum):
    if emp(dum):
        print('Stack is empty')
    else:
        k = dum.pop()
        print(k)

def display(dum):
    top = len(dum)-1
    for i in range(top,-1,-1):
        print(dum[i])

def main():
    print(""" ___________________________________
               1.Insert List
               2.Push 
               3.Pop
               4.Traversal
               5.EXIT """)
    ch = int(input('Enter your choice : '))
    if ch==1:
        inp()
        Odd(NUM1)
        main()
    elif ch==2:
        item = int(input('Enter Odd number to push : '))
        if item%2!=0:
            push(oddlist,item)
            print(f'{item} has been pushed!!')
            main()
        else:
            print(f'{item} is not an odd number!')
            main()
    elif ch==3:
        POP(oddlist)
        main()
    elif ch==4:
        display(oddlist)
        main()
    elif ch==5:
        pass
    else:
        print('inavaild option')
        main()
main()
    

    

