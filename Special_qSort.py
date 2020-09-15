def qsort(lst):
    return EOFError


def partition(lst, low, high):
    if low >= high:
        return
    i = low
    privot = lst[high]
    for j in range(low, high):
        if lst[j] < privot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[i], lst[high] = lst[high], lst[i]

    partition(lst, low, i-1)
    partition(lst, i+1, high)
    return lst


print(partition([1, 5, 3, 2, 8, 7, 6, 4], 0, 7))
