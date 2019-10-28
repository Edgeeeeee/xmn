def cal_GPA():
    lst = []
    try:
        grade = float(input("输入分数，学分，类型（0非专业，1专业）"))
        credit = float(input())
        type = float(input())
        # type = 0
    except Exception as e:
        return False
    if grade < 60:
        current_gpa = 0
    else:
        current_gpa = (grade - 50) * 0.1
    lst.append(current_gpa * credit)
    lst.append(credit)
    if type == 1:
        lst.append(grade * credit)
        lst.append(credit)
    return lst

if __name__ == '__main__':
    all_credit = 0
    all_credit_gpa = 0
    pro_all_credit = 0
    pro_all_credit_gpa = 0
    while True:
        temp = cal_GPA()
        if not temp:
            break
        all_credit_gpa += temp[0]
        all_credit += temp[1]
        try:
            pro_all_credit_gpa += temp[2]

            pro_all_credit += temp[3]
        except IndexError as e:
            pass
    try:
        print("总GPA: " + str(all_credit_gpa/all_credit))
        print("专业加权: " + str(pro_all_credit_gpa/pro_all_credit))
    except ZeroDivisionError as e:
        pass






