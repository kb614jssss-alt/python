score = int(input('점수>'))
grade=''
# print(type(grade), type(score))
if score >= 90:
    if score >= 95:
        grade = 'A+'
    else:
        grade = 'Ao'
elif score >= 80:
    if score >= 85:
        grade = 'B+'
    else:
        grade = 'Bo'
elif score >= 70:
    if score >= 75:
        grade = 'C+'
    grade = 'Co'
elif score >= 60:
    if score >= 65:
        grade = 'D+'
    grade = 'Do'
else:
    grade = 'F'
print(f'{score}의 학점은 {grade}입니다.')

