def grade_in_words(grade):
    grade_word = None
    if 2.00 <= grade <= 2.99:
        grade_word = "Fail"
    elif 3.00 <= grade <= 3.49:
        grade_word = "Poor"
    elif 3.50 <= grade <= 4.49:
        grade_word = "Good"
    elif 4.50 <= grade <= 5.49:
        grade_word = "Very Good"
    elif 5.50 <= grade <= 6:
        grade_word = "Excellent"

    return grade_word


grade_data = float(input())

print(grade_in_words(grade_data))