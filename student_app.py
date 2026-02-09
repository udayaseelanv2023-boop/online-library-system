def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "Fail"

if __name__ == "__main__":
    marks = [95, 82, 67, 40]
    for m in marks:
        print(f"Mark: {m} → Grade: {grade(m)}")
