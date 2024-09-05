student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
#..........................or.....................................


student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score=0
min_score=student_scores[0]
total_sum=0
count_of_number=0
for score in student_scores:
    if score > max_score:
        max_score=score
    if score < min_score:
        min_score=score
    total_sum +=score
    count_of_number+=1

print(max_score)
print(min_score)
print(f"{total_sum}, {count_of_number}")
print(len(student_scores))
print(average:=total_sum/count_of_number)
