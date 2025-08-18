#A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity,
#  Suppose, one unit will cost 100.Judge and print total cost for user.

quantity=(int(input("Enter quantity: ")))
price=quantity * 100
cost=price
actual_price=print("Amount is ",price)
if price >1000:
    discount= price * 0.10
    price-=discount
    print("Price after discount is ",price)
else:
    print("Pay the amount ",cost)    