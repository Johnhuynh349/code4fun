# function to check whether a student pass or fail

score_list = [30, 20, 60, 70, 50, 40, 40]
def pass_fail(score):
    amount = 0
    result = []
    while amount < len(score):
        if score[amount] >= 50:
            result.append("pass")
            amount+=1
        else:
            result.append("fail")
            amount+=1
    return result
print(score_list)
print(pass_fail(score_list))
