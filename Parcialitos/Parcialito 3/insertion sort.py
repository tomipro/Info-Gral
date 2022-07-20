# def bubble_sort(nums):
#     # We set swapped to True so the loop looks runs at least once
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 # Swap the elements
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 # Set the flag to True so we'll loop again
#                 swapped = True


# # Verify it works
# random_list_of_nums = [5, 2, 1, 8, 4, 4, 10, 5, 2]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)

# def insertion_sort(nums):
#     # Start on the second element as we assume the first element is sorted
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         # And keep a reference of the index of the previous element
#         j = i - 1
#         # Move all items of the sorted segment forward if they are larger than
#         # the item to insert
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         # Insert the item
#         nums[j + 1] = item_to_insert

def ordenar(lst):
    for i in range(1, len(lst)):
        a = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > a:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = a

# def ordenar(lst):
#     for i in range(1, len(lst)):
#         a = lst[i]
#         j = i - 1
#         while j >= 0 and lst[j] > a:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = a

# Verify it works
random_list_of_nums = [9, 1, 15, 28, 6, 9, 21, 21]
print(random_list_of_nums)
ordenar(random_list_of_nums)
print(random_list_of_nums)