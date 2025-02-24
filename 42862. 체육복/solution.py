def solution(n, lost, reserve):
    students_with_extra = set(reserve) - set(lost)
    students_who_lost = set(lost) - set(reserve)

    for student in students_with_extra:
        if student - 1 in students_who_lost:
            students_who_lost.remove(student - 1)
        elif student + 1 in students_who_lost:
            students_who_lost.remove(student + 1)
        
    return n - len(students_who_lost)
