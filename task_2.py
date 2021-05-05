reg_nums = ['A123AA11', 'A222AA123', 'A12AA123',
            'A123CC1234', 'AA123A12', 'X067TH13',
            'H000YY70', 'Л899HH90', 'K777YA768',
            'M675MAM0', 'A786XX1', 'A888AA790']
incorrect = []
numbers = ['0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']
letters = ['A', 'B', 'E', 'K', 'M', 'H',
           'O', 'P', 'C', 'T', 'Y', 'X']
three_num_list = [102, 113, 116, 121, 122, 123,
                  124, 125, 126, 134, 136, 138,
                  142, 147, 150, 152, 154, 156,
                  159, 161, 163, 164, 173, 174,
                  177, 178, 186, 190, 196, 197,
                  198, 199, 702, 716, 750, 761,
                  763, 774, 777, 790, 797, 799]

for i in reg_nums:
    IsCorrect = True
    if len(i) > 9 or len(i) < 8:
        IsCorrect = False
    elif len(i) == 8:
        for j in [6, 7]:
            if i[j] not in numbers:
                IsCorrect = False
    else:
        for j in [6, 7, 8]:
            if i[j] not in numbers:
                IsCorrect = False
        if IsCorrect:
            if int(i[6] + i[7] + i[8]) not in three_num_list:
                IsCorrect = False
    if IsCorrect:
        for j in [0, 4, 5]:
            if i[j] not in letters:
                IsCorrect = False
        cnt_zero = 0
        for j in [1, 2, 3]:
            if i[j] not in numbers or i[j] == '0' and cnt_zero == 2:
                IsCorrect = False
            elif i[j] == '0':
                cnt_zero += 1
    if not IsCorrect:
        incorrect.append(i)

for i in incorrect:
    reg_nums.remove(i)
print(reg_nums)
