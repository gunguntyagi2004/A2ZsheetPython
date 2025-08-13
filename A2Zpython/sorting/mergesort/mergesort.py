arr = [64, 25, 12, 22, 11]
print("Original:", arr)


def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left_part = a[:mid]
        right_part = a[mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0

        # Merge process
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                a[k] = left_part[i]
                i += 1
            else:
                a[k] = right_part[j]
                j += 1
            k += 1

        # Remaining elements in left_part
        while i < len(left_part):
            a[k] = left_part[i]
            i += 1
            k += 1

        # Remaining elements in right_part
        while j < len(right_part):
            a[k] = right_part[j]
            j += 1
            k += 1

    return a  
     

sorted_arr = merge_sort(arr)
print("Sorted:", sorted_arr)