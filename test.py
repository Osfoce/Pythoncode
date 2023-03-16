# to make the words be in past tense
words = ["adopt","Marry", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for word in words:
    if word[-1] !="e":# and word[-1] == "y":
        past_tense.append(word+"ed")
    elif word[-1] == "y":
        past_tense.append(word+"ied")
    else:
        past_tense.append(word+"d")

print(past_tense)
