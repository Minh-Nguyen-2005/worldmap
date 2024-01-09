#Author: Minh Nguyen
#Date: 11/03/2023
#Purpose: Quicksort

# A16: extra credit #1

from random import *

def partition(the_list, p, r, compare_func): # partition the sublist the_list[p : r+1]
    i = p - 1
    j = p
    # choosing a random item in the sublist as the pivot.
    k = randint(p, r)
    the_list[k], the_list[r] = the_list[r], the_list[k]
    pivot = the_list[r] # value in the last item in the sub-list


    while j < r: # loop through the sub-list, once j equals r, every sublist item before the_list[r]
        # has been compared with pivot and is in the right place
        if compare_func(the_list[j], pivot): # call compare_func to compare each sublist item with pivot,
            # and rearrange so that the_list[i] ≤ pivot and the_list[j-1] > pivot.
            i = i + 1 # increment i
            the_list[i], the_list[j] = the_list[j], the_list[i] # swap the values in the_list[i] and the_list[j]
        j = j + 1 # increment j

    # put the pivot, currently in the_list[r] into the right place
    # by swapping it with the item in the_list[i+1],
    # which is the leftmost item in the partition known to be greater than pivot.
    # (If the greater-than partition happens to be empty,
    # then this swap should just swap the_list[r] with itself)
    the_list[i + 1], the_list[r] = the_list[r], the_list[i + 1]

    return i + 1 # return an index into the list, which is where it places the item chosen as the pivot

def quicksort(the_list, p, r, compare_func): # sorts the sublist the_list[p : r+1],
    # whose first item is in the_list[p] and whose last item is in the_list[r].

    if r > p: # The base case occurs when the sublist has fewer than two items.

        # call the partition function to partition the sublist, return an index into the sublist,
        # indicating where partition put the pivot item. assign this index to the local variable q,
        # so that partition has placed the pivot item in the_list[q]
        q = partition(the_list, p, r, compare_func)

        # Recursively call quicksort on the sublist starting at index p and going up to,
        # but not including, index q.
        quicksort(the_list, p, q - 1, compare_func)

        # Recursively call quicksort on the sublist starting at the index just past q
        # and going up to and including index r.
        quicksort(the_list, q + 1, r, compare_func)

def sort(the_list, compare_func): # makes a call to the quicksort function
    # to sort the entire list referenced by the_list.

    quicksort(the_list, 0, len(the_list) - 1, compare_func)
    return the_list