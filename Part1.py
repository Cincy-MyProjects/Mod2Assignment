foodamount = float(input("Enter the amount of food: $"))
tipamount = foodamount * 0.18
salestax = foodamount * 0.07
totalamount = foodamount+tipamount+salestax
print(f"Food charge: ${foodamount:.2f}")
print(f"Tip(18%): ${tipamount:.2f}")
print(f"Sales Tax(7%): ${salestax:.2f}")
print(f"Total: ${totalamount:.2f}")
