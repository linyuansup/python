id = input()
if not len(id) == 18:
    print("身份证校验位错误")
    exit()
id_list = list(id)
if not id_list[16] in ['1', '2']:
    print("身份证校验位错误")
    exit()
check_code = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
result_code = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
check_sum = 0
for i in range(17):
    check_sum += int(id_list[i]) * check_code[i]
check_sum = check_sum % 11
if not result_code[check_sum] == int(id_list[17]):
    print("身份证校验位错误")
    exit()
print("身份证校验位正确")
