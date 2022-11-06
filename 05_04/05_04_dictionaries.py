# Key: State
# Value: Capital

statesToCapitals = {}

statesToCapitals["Texas"] = "Austin"
statesToCapitals["New York"] = "Albany"

print(statesToCapitals["New York"])

for key,value in enumerate(statesToCapitals.items()):
    print(f'Key: {key} and Value: {value}')