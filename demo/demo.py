import json
from hyperdb import HyperDB

# Load documents from the JSONL file
documents = []

with open("demo/pokemon.jsonl", "r") as f:
    documents.extend(json.loads(line) for line in f)
# Instantiate HyperDB with the list of documents and the key "description"
db = HyperDB(documents, key="info.description")

# Save the HyperDB instance to a file
db.save("demo/pokemon_hyperdb.pickle.gz")

# Load the HyperDB instance from the file
db.load("demo/pokemon_hyperdb.pickle.gz")

print("Querying the HyperDB instance with a text input:")
print("\"Likes to sleep.\"\n")
# Query the HyperDB instance with a text input
results = db.query("Likes to sleep.", top_k=5)

# Define a function to pretty print the results
def format_entry(pokemon):
    pokemon = pokemon[0]
    name = pokemon["name"]
    hp = pokemon["hp"]
    info = pokemon["info"]
    pokedex_id = info["id"]
    pkm_type = info["type"]
    weakness = info["weakness"]
    description = info["description"]

    return f"""Name: {name}
Pokedex ID: {pokedex_id}
HP: {hp}
Type: {pkm_type}
Weakness: {weakness}
Description: {description}
"""

# Print the top 5 most similar Pokémon descriptions
for result in results:
    print(format_entry(result))