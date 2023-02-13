# Fibonacci sequence

# Enter a number for get the nth in the sequence
entry = int(input("Enter a number - "))


# Fibonacci function
def fib (n): 
     f = [0, 1]
     count = 0
     for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        count = i
     return f[n], count
         

# Check if the number of terms is valid
if entry <= 0:
    print("Plese enter a positive integer")
else:
    if entry == 1:
        print( "First in Fibonacci sequence(First 2 numbers are already defined):")
    elif entry == 2:
        print ("Second in Fibonacci sequence(First 2 numbers are already defined):")
    elif entry == 3:
        print ("Third in Fibonacci sequence + number of steps:")
    else:
        print (entry, "th in Fibonacci sequence + number of steps:")
       
    print(fib(entry - 1))

