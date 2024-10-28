"""Introduction to Dictionaries"""

"""Examples of dictionary syntax with ice cream shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of ENTRIES
print(len(ice_cream))  # prints 3

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3

# access entries by their key
print(ice_cream["chocolate"])  # prints 12, the value associated with key choc

# test if pbj is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream  # can also use in if statements

# to remove, we use the pop method and give the KEY we want to remove
ice_cream.pop("strawberry")

# to iterate over every key in a loop, use for in (flavor is variable assigned each key in loop)
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")


def mint_finder(orders: dict[str, int]) -> None:
    if "mint" in orders:
        print(orders["mint"])
    else:
        print("no orders of mint")


mint_finder(ice_cream)

print(ice_cream)
