from student_app import grade

def test_grades():
    assert grade(95) == "A"
    assert grade(80) == "B"
    assert grade(65) == "C"
    assert grade(30) == "Fail"
    print("All grade tests passed!")

if __name__ == "__main__":
    test_grades()
