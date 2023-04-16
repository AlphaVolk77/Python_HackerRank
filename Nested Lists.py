students=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    sorted_students=sorted(students, key=lambda x:x[1])
