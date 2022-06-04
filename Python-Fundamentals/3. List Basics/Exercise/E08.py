fire_list = input().split("#")
water_amount = int(input())

total_effort = 0
total_fire = 0
total_cells_saved = []
for fire in fire_list:
    fire_type, cell_value = fire.split(" = ")
    cell_value = int(cell_value)
    #  checking if it's valid cell value
    if fire_type == "High" and 81 <= cell_value <= 125 \
            or fire_type == "Medium" and 51 <= cell_value <= 80 \
            or fire_type == "Low" and 1 <= cell_value <= 50:
        if cell_value <= water_amount:
            water_amount -= cell_value
            total_effort += 0.25 * cell_value
            total_fire += cell_value
            total_cells_saved.append(cell_value)

print("Cells:")
for cell in total_cells_saved:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")