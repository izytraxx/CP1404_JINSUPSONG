"""
Get into your preferred group, and work on the following:
1. Construct a read_file() method that reads in a string input as filename then return the list of data from file.
    def read_file(filename):
        ........
        return data
    calling:
        data = read_file("data.txt")
        data[0] = "2005-Q1, 0.00062"
2. Second function that cleans up the data.
    def clean_up(data):
        ........
        return data
    calling:
        data = clean_up(data)
        data[0] = [2005, "Q1", 0.00062]
3. Finally display all data from main()
"""

def read_file(FILENAME):
    in_file = open(FILENAME, "r")
    data = in_file.readlines()
    #for each in data:
    #    if "\n" in each:
    #        each = each.replace("\n","")
    return data
    in_file.close()

def clean_up(data):
    new_list = []
    for each in data:
        each = each.replace("-",",")
        year = each.split(',')[0]
        quarter = each.split(',')[1]
        data_usage = each.split(',')[2]
        new_data = [int(year), str(quarter), float(data_usage)]
        new_list.append(new_data)
    return new_list



def main():
    FILENAME = "mobile-data-usage.csv"
    data = read_file(FILENAME)
    data = clean_up(data)
    for each in data:
        print(each)
main()



