def bill_calc(n):
    bill=0
    if n<=100:
        bill=n*1.50
    elif n<=200:
        bill=(100*1.50)+(n-100)*2.50
    elif n<=500:
        bill=(100*1.50)+(100*2.50)+(n-200)*4.00
    else:
        bill=(100*1.50)+(100*2.50)+(300*4.00)+(n-500)*6.00
    return bill
x=int(input("Enter number of customers:"))
for i in range(1,x+1):
    print(f"\nCustomer {i}:")
    name =input("Enter Customer name :")
    n=float(input("Enter number of units consumed :"))
    bill=bill_calc(n)
    print("Customer Name :",name)
    print("Units Consumed :",n)
    print("Total Bill amount : Rs",round(bill,2))