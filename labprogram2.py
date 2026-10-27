bill = 0
def bill (units):
    if units <=100:
        bill = units * 1.50
    elif units <=200:
        bill = 100 *1.50 + (units-100)*2.50
    elif units <= 500:
        bill = 100*1.50 +200 *2.50+ (units - 200)*4.00 
    else:
        bill = 100 * 1.50 +200*2.50 +300*4.00 + (units - 500)*6.00
    return bill
n = int (input ("enter the no of customer:"))
for i in range (1,n+1):
    name = input( (f"enter the customer name{i} :"))
    units = float (input ("enter the units consumed:" ))
    bill = bill(units)

print ("name of the costumer:",name)
print ("units consumed :",units)
print ("bill:",bill)
    
        