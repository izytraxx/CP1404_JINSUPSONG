TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0\n>>>")
tariff = int(input("Which tariff? 11 or 31: "))
while (tariff != 11) and (tariff != 31):
    print("Invalid value!")
    tariff = int(input("Which tariff? 11 or 31: "))
### price = int(input("Enter cents per kWh: "))
dailyUse = float(input("Enter daily use in kWh: "))
billingDays = int(input("Enter the number of billing days: "))
if tariff == 11:
    estimatedBill = (dailyUse * billingDays * TARIFF_11)
elif tariff == 31:
    estimatedBill = (dailyUse * billingDays * TARIFF_31)
print("Estimated bill: ${:.2f}".format(estimatedBill))