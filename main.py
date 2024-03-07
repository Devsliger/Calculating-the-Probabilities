def find_numbers_within_range(target, options, percentage=0.8):
    within_range = []
    threshold = target * percentage

    for number in options:
        difference = abs(target - number)
        if difference <= threshold:
            within_range.append(number)

    return within_rangfe


# Example usage
target_number = 7.85
options = [7.84, 8.01, 14.56, 0.01, 8.45, 7.10, 6.98]
numbers_within_range = find_numbers_within_range(target_number, options)
print("Numbers within 80% range of", target_number, "are:", numbers_within_range)
