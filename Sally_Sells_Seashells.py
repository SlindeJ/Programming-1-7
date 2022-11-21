seashells = int(input("How many shells? ", ))
gshells = 0
if seashells <= 100:
    for seashells in range(1, seashells + 1, 1):
        gshells = gshells + int(input("Enter the weights of each shell: ", ))

buckets = gshells / 100
buckets = round(buckets + 0.5, 0)
print("Total grams of shells: ", gshells)
print("Buckets needed: ", int(buckets))
if seashells > 100:
    print("Please enter a number less than 100.")
