# Fibonacci sequence recursive
count = 0
# Fibonacci function
def fibonacci(n):
   global count
   count += 1
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


# Enter a number for get a result
entry = int(input("Enter a number -  "))

# Check if the number of terms is valid
if entry <= 0:
    print("Plese enter a positive integer")
else:
    if entry == 1:
        print( "First in Fibonacci sequence:")
    elif entry ==2:
        print ("Second in Fibonacci sequence:")
    elif entry == 3:
        print ("Third in Fibonacci sequence:")
    else:
        print (entry, "th in Fibonacci sequence:")
        
    print("Fibonacci solution:", fibonacci(entry - 1))
    print("Steps number:", count)
    