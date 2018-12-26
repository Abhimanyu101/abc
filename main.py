import fib
import prime
import reverse
def choice():
    ch=0
    while ch != 4:
        print("Type 1 to print fibonacci Series ")
        print("Type 2 to print prime numbers ")
        print("Type 3 to print reverse of a number ")
        print("Type 4 to exit ")
       
        ch=int(input("Enter a choice "))
        print(ch)
        
        if ch == 1:
            fib.fib()
        if ch == 2: 
            prime.prime()
        if ch == 3: 
            reverse.reverse()
choice()