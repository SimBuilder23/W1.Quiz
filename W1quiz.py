# ## Fulltime Week1 Quiz

# * Write a function ```readcurrency(filename)```
# that takes a filename as its argument.

# * This function reads the lines of a file, which are of the form

# ```
# USD 1.141911
# ```

# Where the first value is a currency and the second value is the
# Euro's value in that currency.

# * Return a list of dictionaries from this data, with each
# line of the file corresponding to an element in the dictionary.

# * Each element should have two keys, "symbol" and "rate" with the
# appropriate values.

# * The list will look like:

# ```
# [
#   {"symbol": "AED", "rate": 4.194468},
#   {"symbol": "AFD", "rate": 83.493676},
#   {"symbol": "ALL", ... and so on
# ]


def readcurrency(filename):
    data = []
    with open(filename) as f_obj:
        for line in f_obj:
            list1 = line.split()
            dict1 = {"symbol": list1[0], "rate:": list1[1]}
            #print (dict1)
            data.append(dict1)
    #print (data)
    return (data)     

readcurrency ("currency.txt")


def save(filename, data):
    import json
    
    list2 = readcurrency(filename)
    dict2 = {"data": list2}
        
    with open (filename.json, "w") as write_file_object:
        json.dump(dict2, write_file_object, indent = 5)

# save ("currency.txt", readcurrency)


