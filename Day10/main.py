# exception handling
# a = 10
# b = 3
# c = a - d
# print(c)

a = [10, 20, 30, 40]

try:
    ind = input("enter index to add ")
    total = a[1] + a[ind]
    print("total isL ", total)
# except IndexError as e:
#     print("Error: ", e)
# except ValueError as e:
#     print("Error: ", e)
# except TypeError as e:
    # print("Error: ", e)
except (TypeError, ValueError) as e:
    print("Error: ", e)
    
print("today")
