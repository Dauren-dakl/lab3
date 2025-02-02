def grams_to_ounces(grams):
    return 28.3495231 * grams

grams = float(input("граммов: "))
ounces = grams_to_ounces(grams)
print(grams, "грамм = ",ounces , "унций")
