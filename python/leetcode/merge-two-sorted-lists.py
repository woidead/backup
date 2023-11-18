def mergeTwoLists( list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        else:
            list3 = list1 + list2
            list3.sort()
            return list3
print(mergeTwoLists([1,2,4],[1,3,4]))