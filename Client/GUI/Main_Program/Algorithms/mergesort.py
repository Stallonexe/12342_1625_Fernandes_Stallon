def MergeSort(mergelist):
    if len(mergelist) > 1:
        mid = len(mergelist) // 2
        lefthalf = mergelist[:mid]
        righthalf = mergelist[mid:]
        MergeSort(lefthalf)
        MergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                mergelist[k] = lefthalf[i]
                i += 1
            else:
                mergelist[k] = righthalf[j]
                j += 1
            k += 1

        # check if left half has elements not merged
        while i < len(lefthalf):
            mergelist[k] = lefthalf[i]
            i += 1
            k += 1

        # check if right half has elements not merged
        while j < len(righthalf):
            mergelist[k] = righthalf[j]
            j += 1
            k += 1

    return mergelist

