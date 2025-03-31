# The adapter will work if its ampere is greater than or equal to the tree’s ampere.

# Watt: measure of power
# Volt: measure of electric potential
# Ampere: measure of current
# watt = ampere × volt → ampere = watt / volt

# The first input line contains an integer, a (1 ≤ a ≤ 20), indicating the ampere for the Christmas tree. 
# The second input line contains two integers: w (1 ≤ w ≤ 2000), 
# indicating the watt for the candidate adapter and v (1 ≤ v ≤ 100), indicating the volt for the candidate adapter. 
# Assume that the input will not result in fractions in divisions.

# Print 1 if the candidate adapter will work with the tree, 0 (zero) otherwise.

tree_ampere = int(input())
watt, volt = map(int, input().split(" "))
adapter_ampere = watt / volt

print(int(tree_ampere <= adapter_ampere))