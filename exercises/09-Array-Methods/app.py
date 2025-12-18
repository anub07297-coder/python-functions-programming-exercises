names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']

## CREATE YOUR FUNCTION HERE
def sort_names(names_list):
    """this function sorts a list of names in alphabetical order."""
    newNamesList = sorted(names_list)
    return newNamesList

print(sort_names(names))


# lambdaSortNames = lambda names : sorted(names,reverse=False)
# print(lambdaSortNames(names))


# # reconfirming the list
# print(names)



# for i in range(len(names)):
#     for j in range(0,len(names[i])-1):
#         if(names[j] > names[j+1]):
#               names[j],names[j+1] = names[j+1], names[j]
              
# print(names)