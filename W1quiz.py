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
    list_answer = []
    with open(filename) as f_obj:
        for line in f_obj:
            list1 = line.split()
            dict1 = {"symbol": list1[0], "rate:": list1[1]}
            #print (dict1)
            list_answer.append(dict1)
    print (list_answer)         

readcurrency("currency.txt")
