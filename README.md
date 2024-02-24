Football Match Probability Calculator

This script calculates the probabilities of various match outcomes for a football (soccer) match using the Poisson distribution. The Poisson distribution is a probability distribution that models the number of events occurring in a fixed interval of time or space, given a known average rate of occurrence.

Functionality:
Input: The script prompts the user to input the average goal rates for the home team and the away team. These rates represent the average number of goals scored by each team per match.

Probability Calculation: Using the entered average goal rates, the script computes the probabilities for each possible score for both the home and away teams separately, based on the Poisson distribution formula.

Match Outcome Calculation: It then combines these individual probabilities to calculate the probabilities for each possible match outcome, considering all possible combinations of home and away team scores.

Output: Finally, the script displays the calculated probabilities for each possible score for both teams, as well as the probabilities for each possible match outcome.

Usage:
Execution: To use the script, ensure you have Python installed on your system. Run the script by executing the command python football_match_probability.py in your terminal.

Input: Enter the average goal rates for the home team and the away team when prompted by the script.

Output: The script will then display the probabilities for each possible score for both teams, as well as the probabilities for each possible match outcome.

Dependencies:
Python 3.x
Standard math module for mathematical calculations.
Example:
Suppose the average goal rate for the home team is 1.5 and for the away team is 1.2. Running the script will produce the probabilities for different match outcomes based on these rates.

Note:
The script assumes that both teams' goal-scoring follows a Poisson distribution.
It considers scores up to 9 goals for each team, which is a common practical limit for football matches.
