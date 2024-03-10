L = [5, 8, 9, 3, 7, 10, 12, 1]

# set n to the number of records to be sorted
n = len(L)
# repeat
while True:

    # flag = false;
    flag = False
    # for counter = 1 to n-1 do
    for counter in range(n - 1):
        # if key[counter] > key[counter+1] then
        if L[counter] > L[counter + 1]:
            # swap the records;
            temp = L[counter]
            L[counter] = L[counter+1]
            L[counter+1] = temp
            # set flag = true;
            flag = True
        # print(L)
        # end if
    # end do
    # n = n-1;
    n = n-1
    # until flag = false or n=1
    if flag == False or n == 1:
        break

print(L)