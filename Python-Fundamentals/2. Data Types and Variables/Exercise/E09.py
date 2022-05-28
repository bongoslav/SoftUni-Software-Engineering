nums_snowballs = int(input())

highest_score = 0
snowballs_list = []
for _ in range(nums_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = int((weight / time_needed) ** quality)
    snowballs_list.append({"weight": weight,
                      "time": time_needed,
                      "quality": quality,
                      "snowball value": snowball_value})

for snowballs in snowballs_list:
    if highest_score < snowballs["snowball value"]:
        highest_score = snowballs["snowball value"]
        best_weight = snowballs["weight"]
        best_time = snowballs["time"]
        best_quality = snowballs["quality"]

print(f"{best_weight} : {best_time} = {highest_score} ({best_quality})")
