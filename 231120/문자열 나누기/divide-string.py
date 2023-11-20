n = int(input())

num_str_lst = list(input().split())
counter = 0
for row in num_str_lst :
    for element in row :
        counter += 1
        print(element, end = "")
        if counter == 5 :
            print()
            counter = 0