print("Electricity bill estimator\n>>>")
price = int(input("Enter cents per kWh: "))
dailyUse = float(input("Enter daily use in kWh: "))
billingDays = int(input("Enter the number of billing days: "))
estimatedBill = (dailyUse * billingDays * price)/100
print("Estimated bill: ${:.2f}".format(estimatedBill))