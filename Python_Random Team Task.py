# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:07:51 2024

@author: Mostafa
"""

import random

# Define the level lists
level1 = [1, 2, 3, 4]
level2 = ['a', 'b', 'c', 'd']
level3 = [66, 77, 88, 99]
level4 = ['1$', '2&', '3%', '4©']

# Number of teams to create
num_teams = 4

# Ensure we have the same number of elements in each level list
assert len(level1) == len(level2) == len(level3) == len(level4) == num_teams, "All level lists must have the same number of elements"

# Randomize the order of elements in each level list
random.shuffle(level1)
random.shuffle(level2)
random.shuffle(level3)
random.shuffle(level4)

# Combine elements from each level to form teams
teams = []
for i in range(num_teams):
    team = [level1[i], level2[i], level3[i], level4[i]]
    teams.append(team)

# Print the teams
for i, team in enumerate(teams, start=1):
    print(f"team{i} = {team}")
