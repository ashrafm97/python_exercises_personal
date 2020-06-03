# initial_list = ["Apple", "Banana", "Grapes", "Apple", "Mango", "Peach", "Grapes"]
# check_list = []
# duplicates = []
# # Loop through initial list
# for item in initial_list:
#     # check if that item is already in the check list
#     if item in check_list:
#         # if it does exist in the check list already then we append it to the duplicates list
#         duplicates.append(item)
#     # if it is not a duplicate then we add it to the check list to see if it pops up again later
#     check_list.append(item)
#
# print("These are the duplicates")
# # loop through duplicates array to show which items were duplicates
# for duplicate in duplicates:
#     print(duplicate)
#


first_list = ["LeBron James", "Lamar Jackson", "Ricardo Kaka", "Riyad Mahrez", "LeBron James", "Lamar Jackson", "Tom Brady"]
checking_list = []
dupe_list = []

for blob in first_list:
    if blob in checking_list:
        dupe_list.append(blob)
    checking_list.append(blob)

print("You perfected cloning this guy?!?")

for clone in dupe_list:
    print(clone)