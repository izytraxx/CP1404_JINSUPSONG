shippingCostList = []
itemNumberList = []
totalShippingCost = 0

numItems = int(input("Enter the total number of items " + "\n" + ">>> "))
while numItems < 0 :
    print("Invalid number of items!")
    numItems = int(input("Enter the number of items "+ "\n" + ">>> "))
for i in range (0,numItems):
    itemNumber = int(input("Enter the number of the item " + str(i+1) + "\n" + ">>> "))
    itemNumberList.append(itemNumber)
    shippingCost = int(input("Enter the shipping cost for the item " + str(i+1) + "\n" + ">>> "))
    shippingCostList.append(shippingCost)
    totalShippingCost = totalShippingCost + (itemNumberList[i] * shippingCostList[i])
print("\n")
for i in range (0,numItems):
    print("The shipping cost for item " + str(i+1) + " is: ${:.2f}".format(itemNumberList[i]*shippingCostList[i]) + "\n")

if totalShippingCost > 100 :
    totalShippingCost *= 9/10
print("Total shipping cost for every item is: ${:.2f}".format(totalShippingCost))