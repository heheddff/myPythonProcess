def readFile(filename):
    f = open("./files/"+filename,"r",encoding="utf-8")
    students = []
    i =0
    for l in f:
        if i > 0:
            students.append(l.replace("\n","").strip().split(",")[0])
        i+=1
    return students
allStu={}

file = ["1.csv","2.csv","3.csv","4.csv","5.csv","6.csv","7.csv","8.csv","9.csv","10.csv"]
for j in file:
    for i in readFile(j):
        allStu[i]=allStu.get(i,0)+1
print("全勤同学有：",end ="")
for stu in allStu:
    if allStu[stu] == 10:
        print(stu,end=",")
