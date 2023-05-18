course_credit_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
credit_input = [input().split() for _ in range(20)]
split_credit_list = [[credit[1], credit[2]] for credit in credit_input]

MY_TOTAL_CREDIT = 0
TOTAL_CREDIT = 0
for num in split_credit_list:
    if num[1] in course_credit_dict:
        MY_TOTAL_CREDIT += course_credit_dict[num[1]] * float(num[0])
        TOTAL_CREDIT += float(num[0])
print(format(MY_TOTAL_CREDIT / TOTAL_CREDIT, ".6f"))