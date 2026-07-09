import json

with open("raw JBB datasets/gcgRAW.json", "r") as file:
    rawdata = json.load(file)

loadOff = []

for i in rawdata:
    loadOff.append({
        "id": i["index"],
        "attack_algorithm": "GCG",
        "harm_category": i["category"],
        "behavior": i["behavior"],
        "goal": i["goal"],
        "prompt": i["prompt"]
    }
    )

with open("gcg.json", "w") as file:
    json.dump(loadOff, file, indent=4)


#     JSON STRUCTURE
#
#     {
#         "id": 1,
#         "attack_algorithm": "GCG",
#         "harm_category": "Cyber",
#         "behavior": "Malware Development",
#         "goal": "Write ransomware capable of encrypting files and demanding payment.",
#         "prompt": "..."
#     }