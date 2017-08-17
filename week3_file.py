"""
Write code to read a file like this and print each part separately with the price formatted like currency

Fender Stratocaster,2014,765.40\n
Gibson L-5 CES,1922,16035.40\n
Line 6 JTV-59,2010,1512.90\n
"""
FILENAME = "data.csv"
OUT_FILE = "out.txt"

in_file = open(FILENAME, "r")
out_file = open(OUT_FILE, "w")

#data = in_file.read() #read everything together
#data = in_file.readlines() #read into a list structure
for each in in_file:
    if "\n" in each:
        each = each.replace("\n","")
    if "\\n" in each:
        each = each.replace("\\n","")
    #print(each)
    datum = each.split(",")
    #print("{} from {} year cost ${}".format(datum[0], datum[1], datum[2])
    print("{} from {} year cost ${}".format(datum[0], datum[1], datum[2]), file=out_file) #write to file
    print("{} from {} year cost ${}".format(datum[0], datum[1], datum[2]))


in_file.close()
out_file.close()
##################################