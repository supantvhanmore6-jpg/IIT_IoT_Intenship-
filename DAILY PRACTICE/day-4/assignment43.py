def fun_list(list1,list2):
        return bool(set(list1)&set(list2))

print(fun_list([9,7,1],[5,8,9]))