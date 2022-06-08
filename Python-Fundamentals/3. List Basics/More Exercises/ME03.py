steps = list(map(float, input().split()))
finish_line = (len(steps) - 1) // 2

total_time_left = 0
total_time_right = 0

# time for left driver
left_list = steps[:finish_line]
for left_step in left_list:
    total_time_left += left_step
    if left_step == 0:
        total_time_left *= 0.8

# time for right driver
right_list = steps[len(steps):finish_line:-1]
for right_step in right_list:
    total_time_right += right_step
    if right_step == 0:
        total_time_right *= 0.8

if total_time_left < total_time_right:
    winner = "left"
else:
    winner = "right"
winning_time = min(total_time_right, total_time_left)

print(f"The winner is {winner} with total time: {winning_time:.1f}")