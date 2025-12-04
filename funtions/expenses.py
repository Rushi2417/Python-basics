def cal_exp(expenses):
    '''
    :param expenses:
    :return:
    '''
    total = 0
    for expense in expenses:
        total+=expense
    return total

expense_rushi = [20,84,12,64,99]
expense_adi = [95,42,62,4,56]

total_ex_rushi = cal_exp(expense_rushi)
total_ex_adi = cal_exp(expense_adi)

print(f"Total expense of Rushi is {total_ex_rushi}")
print(f"Total expense of Adi is {total_ex_adi}")

help(cal_exp)