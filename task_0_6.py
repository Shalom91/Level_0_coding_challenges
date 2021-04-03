def maximum(*arguments):

    *max_number, = arguments 
    new_list = [i for i in max_number]
    x = 0
    for i in new_list:
        x += 1
    while x > 1:
        for i in max_number:
            for j in new_list:
                if i > j:
                    x -= 1
    print(i)

maximum(1,2,3,22)

        