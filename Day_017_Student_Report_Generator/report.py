import csv 

reports = []

with open("students.csv",newline="") as file:
    for row in csv.DictReader(file):
        keys = ("maths","programing","english")
        scores = [float(row[key]) for key in keys]
        average = sum(scores) / len(scores)
        reports.append(f"{row['name']} : average {average:.2f}")

with open("report.txt","w",encoding="utf-8") as file:
    file.write("STUDENT REPORT\n")
    file.write("\n".join(reports))
print("created report.txt!")