def find_closest_percentages(target_percentage, options):
    differences = [(option, abs(target_percentage - option)) for option in options]
    sorted_differences = sorted(differences, key=lambda x: x[1])
    closest_percentages = [x[0] for x in sorted_differences]
    return closest_percentages

target_percentage = 7.234345
options = [7.623, 7.0987, 7.8972, 5.6768, 3.45654, 6.9987899]

closest_percentages = find_closest_percentages(target_percentage, options)
print("Closest percentages to", target_percentage, "in ascending order are:", closest_percentages)

