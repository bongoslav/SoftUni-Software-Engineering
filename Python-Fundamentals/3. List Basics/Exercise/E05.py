cards_list = input().split()
shuffles = int(input())

middle_list = cards_list.copy()
final_list = []
middle_index = len(cards_list) // 2
for shuffles_count in range(shuffles):
    first_list = middle_list[:middle_index]
    second_list = middle_list[middle_index:]
    middle_list = []
    for index in range(len(first_list)):
        middle_list.append(first_list[index])
        middle_list.append(second_list[index])

final_list = middle_list

print(final_list)

