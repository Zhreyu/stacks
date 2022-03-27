# A list NUM has some integer numbers. Write down a program to prepare a stack of even integers from the given list NUM. The program should have user- defined functions which perform the following operations based on this list.
# Traverse the content of the list and push the EVEN numbers onto the stack.
# Pop and display the content of the stack.
A = []
def inp():
    n=int(input("Enter the size of the list : "))
    for i in range(int(n)):
         k=int(input(f'enter element number{i+1} : '))
         A.append(k)
    print('LIST appended sucessfully')

evenlist = []
oddlist = []
top = None

def emp(dum):
    if dum ==[]:
        return True
    else:
        return False

def isEVEN(stk):
    for i in stk:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)


def PUSH(dum,item):
    dum.append(item)
    top = len(dum) - 1

def POP(dum):
    if emp(dum):
        print('empty')
    else:
        k = dum.pop()
        print(k) 

def Display(dum):
    if emp(dum):
        print('Stack is empty')
    else:
        top = len(dum)-1
        for i in range(top,-1,-1):
            print(dum[i])

def main():
    print("""-----------------------------------------------
                     1.INPUT LIST
                     2.PUSH
                     3.POP 
                     4.DISPLAY                 
        ----------------------------------------------------- """)
    ch = int(input('select one option : '))
    if ch==1:
        inp()
        isEVEN(A)
        main()
    elif ch==2:
        item = int(input('Enter an even number to push : '))
        if item%2==0:
            PUSH(evenlist,item)
            print(f'{item} has been pushed!!')
            print('--------------------------------------------')
            main()
        else:
            print(f'{item} is not an even number')
            print('--------------------------------------------')
            main()
    elif ch==3:
        POP(evenlist)
        print('--------------------------------------------')
        main()
    elif ch==4:
        Display(evenlist)
        print('--------------------------------------------')
        main()

main()
