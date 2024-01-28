
plant_sample = "Spathiphyllum"

plant_in = input("Enter the plant name :")
message = f"No, I want a big {plant_sample}!"
if plant_sample == plant_in:
    message = f"Yes - {plant_sample} is the best plant ever!"

print(message)