grades=[]

while True:
    grade_input=input('Enter a grade or blank space to leave: ')
    if grade_input=='':
        break
    grades.append(int(grade_input))

total_amount=len(grades)
minimum=min(grades)
maximum=max(grades)
average=sum(grades)/2

print(f'About Grades: totals grades: {total_amount}, minimum: {minimum}, maximum: {maximum}, average: {average} ')