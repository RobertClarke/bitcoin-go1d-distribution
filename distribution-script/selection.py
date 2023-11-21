import requests
import random
import os

# Function to get block hash
def get_block_hash(block_height):
    url = f"https://ordinals.com/blockhash/{block_height}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Error fetching block hash: HTTP {response.status_code}")

# Function to select a random number
def select_random_number(numbers, entropy):
    random.seed(entropy)
    return random.choice(numbers)

# Prompt user for inputs
block_height = input("Bitcoin block height for selection: ")
btc_address = input("Bitcoin address for distribution: ")

# Fetch block hash
block_hash = get_block_hash(block_height)

# Read available numbers
with open("available.txt", "r") as file:
    numbers = file.readlines()

# Remove newline characters
numbers = [num.strip() for num in numbers]

# Generate entropy
entropy = block_height + btc_address + block_hash

# Select random number
selected_number = select_random_number(numbers, entropy)

# Remove selected number from list
numbers.remove(selected_number)

# Rewrite available.txt without the selected number
with open("available.txt", "w") as file:
    for number in numbers:
        file.write(number + '\n')

# Write to distributed.txt
with open("distributed.txt", "a") as file:
    file.write(f"Bitcoin Go1d bar selected at random: {selected_number}\n")
    file.write(f"Bitcoin block height for selection: {block_height}\n")
    file.write(f"Bitcoin address: {btc_address}\n")
    file.write("\n")  # Extra line for readability

print("Process completed. The selection has been written to distributed.txt.")
