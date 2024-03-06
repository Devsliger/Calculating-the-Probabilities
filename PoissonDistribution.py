import math

def calculate_target_probability(prob_home, prob_away):
    total_probability = max(prob_home.values()) + max(prob_away.values())
    target_percentage = (total_probability / 9) * 100
    return target_percentage

def find_closest_percentages(target_percentage, options):
    differences = [(option, abs(target_percentage - option)) for option in options]
    sorted_differences = sorted(differences, key=lambda x: x[1])
    closest_percentages = [x[0] for x in sorted_differences]
    return closest_percentages

# Ask the user for match data
print("Enter data for the match")
lambda_value = float(input("Home team's average goal rate: "))
mu_value = float(input("Away team's average goal rate: "))

# Calculate the probability of a goal for each team
prob_home = {}
prob_away = {}
for i in range(0, 10):
    prob_home[i] = math.exp(-lambda_value) * pow(lambda_value, i) / math.factorial(i)
    prob_away[i] = math.exp(-mu_value) * pow(mu_value, i) / math.factorial(i)

# Display the probability for each possible home team score
print("\nProbabilities for the home team")
for i in range(0, 10):
    print("Score {}: {:.2f}%".format(i, prob_home[i] * 100))

print("largest posibility for the home team {:.2f}%".format( max(prob_home.values()) * 100))

# Display the probability for each possible away team score
print("\nProbabilities for the away team")
for j in range(0, 10):
    print("Score {}: {:.2f}%".format(j, prob_away[j] * 100))

print("largest posibility for the away team {:.2f}%".format( max(prob_away.values()) * 100))

# Calculate the probability of each possible result
prob_result = {}
for i in range(0, 10):
    for j in range(0, 10):
        if i not in prob_result:
            prob_result[i] = {}
        prob_result[i][j] = prob_home[i] * prob_away[j]

# Display the probability for each possible result
print("\nProbabilities for each possible result")
for i in range(0, 10):
    for j in range(0, 10):
        print("Result {}-{}: {:.2f}%".format(i, j, prob_result[i][j] * 100))

# Calculate the target probability
target = calculate_target_probability(prob_home, prob_away)

# Find the 4 closest percentages to the target percentage
options = [prob_result[i][j] * 100 for i in range(10) for j in range(10)]
closest_percentages = find_closest_percentages(target, options)

print("Target percentage:", target)
print("Closest percentages to target in ascending order are:", closest_percentages[:4])
