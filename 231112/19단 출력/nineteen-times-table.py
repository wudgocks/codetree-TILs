for i in range(1,20) :
    for j in range(1, 20) :
        if j % 2 == 0 and j != 19:
            print(f'{i} * {j} = {i*j} \n', end = "")
        elif j == 19 :
            print(f'{i} * {j} = {i*j} \n', end = "")
        else :
            print(f'{i} * {j} = {i*j} / ', end = "")