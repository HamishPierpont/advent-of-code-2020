f = open('input.txt', 'r')
expense_report_data = [int(line) for line in f.readlines()]
for item1 in expense_report_data:
    for item2 in expense_report_data:
        for item3 in expense_report_data:
            if item1 + item2 + item3 == 2020 and item1 != item2 != item3:
                print(item1*item2*item3)
                quit()
