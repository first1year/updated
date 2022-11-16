def IterativeFibbo(n):
    f1=0
    f2=1
    for i in range(n):
        if i<2:
            print(i,end= ' ')
        else:
            f3=f1+f2
            f1=f2
            f2=f3
            print(f3,end= ' ')
def RecursiveFibbo(n):
    if(n<=1):
        return n
    else:
        return(RecursiveFibbo(n-1) + RecursiveFibbo(n-2))
def main():
    print("Iterative")
    IterativeFibbo(n)
    print("\nrecu")
    n = int(input("Enter number:"))
    for i in range(n):
        print(RecursiveFibbo(i))
        
if __name__ == "__main__":
    main()


