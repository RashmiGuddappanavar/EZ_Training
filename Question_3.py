'''a simple Python code snippet that demonstrates filling three jars with capacities of 10, 20, and 30 chocolates sequentially. The code will fill each jar to its capacity before moving on to the next jar'''

n1=int(input("Enter jar1 capacity:"))
n2=int(input("Enter jar2 capacity:"))
n3=int(input("Enter jar3 capacity:"))
if n1%3==0 or n2%3==0 or n3%3==0:
    print("Jar is empty.")
    print(n%3)
    
elif n%3!=0 or n2%3!=0 or n3%3!=0:
    print("Jar is not empty.")
    print(n%3)
