X = int(input("คะแนนเก็บ: "))
Y = int(input("คะแนนสอบกลางภาค: "))
Z = int(input("คะแนนสอบปลายภาค: "))
sumScore = X + Y + Z

if sumScore >= 80: print("A");
elif sumScore >= 75: print("B+");
elif sumScore >= 70: print("B");
elif sumScore >= 65: print("C+");
elif sumScore >= 60: print("C");
elif sumScore >= 55: print("D+");
elif sumScore >= 50: print("D");
else: print("F");