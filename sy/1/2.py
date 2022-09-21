salary = float(input())
if salary <= 0:
    print("err")
else:
    five_one_insurance_fund = float(input())
    exemption = float(input())
    need_tax = salary - five_one_insurance_fund - exemption
    if need_tax > 0:
        tax = min(need_tax, 3000) * 0.03
        if need_tax > 3000:
            tax += (min(need_tax, 12000) - 3000) * 0.1 - 210
        if need_tax > 12000:
            tax += (min(need_tax, 25000) - 12000) * 0.2 - 1410
        if need_tax > 25000:
            tax += (min(need_tax, 35000) - 25000) * 0.25 - 2660
        if need_tax > 35000:
            tax += (min(need_tax, 55000) - 35000) * 0.3 - 4410
        if need_tax > 55000:
            tax += (min(need_tax, 80000) - 55000) * 0.35 - 7160
        if need_tax > 80000:
            tax += (need_tax - 80000) * 0.45 - 15160
    else:
        tax = 0
    print("应缴税额" + str(tax) + "元，实发工资" + str(salary - five_one_insurance_fund - tax) + "元")
