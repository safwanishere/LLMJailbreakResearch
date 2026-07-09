import jailbreakbench as jbb
import json

dataset = jbb.read_dataset()

# Access the entries of the JBB-Behaviors dataset
behaviors = dataset.behaviors
goals = dataset.goals
targets = dataset.targets
categories = dataset.categories

data = []

for i in range(len(behaviors)):
    data.append(
        {
            "behavior": behaviors[i],
            "goal": goals[i],
            "target": targets[i],
            "category": categories[i]
        }
    )

with open("dataset.json", "w") as file:
    json.dump(data, file, indent=4)