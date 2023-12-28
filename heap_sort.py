def heap_sort(a):

    def down_heap(a, left, right):
        temp = a[left]  # root

        parent = left
        while parent < (right + 1) // 2:    # while parent is not leaf
            cl = parent * 2 + 1     # left child
            cr = cl + 1        # right child
            
            if cr <= right and a[cr] > a[cl]:
                child = cr
            
            else: child = cl

            if temp >= a[child]:
                break

            a[parent] = a[child]
            parent = child

        a[parent] = temp