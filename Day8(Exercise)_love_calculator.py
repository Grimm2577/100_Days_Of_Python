def calculate_love_score(name1, name2):
    sum_of_first_digits_counted = 0
    sum_of_second_digits_counted = 0
    val1 = ["t","r","u","e"]
    val2 = ["l","o","v","e"]
    string_to_count = list(name1.lower() + name2.lower())
    for letter in val1:
        counted_digit_total = string_to_count.count(str(letter))
        sum_of_first_digits_counted += counted_digit_total
    for letter in val2:
        counted_digit_total = string_to_count.count(str(letter))
        sum_of_second_digits_counted += counted_digit_total
    
    print("The Love Score Is : ", str(sum_of_first_digits_counted) + str(sum_of_second_digits_counted))
calculate_love_score("Angela Yu", "Jack Bauer")