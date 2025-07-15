import requests
import pandas as pd
import os

def extract_pokemon_list(limit=50):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["results"]

def transform_pokemon_data(pokemon_list):
    data = []

    for pokemon in pokemon_list:
        details = requests.get(pokemon["url"]).json()
        base_exp = details.get("base_experience", 0)

        if base_exp > 100:
            data.append({
                "name": details["name"],
                "base_experience": base_exp,
                "height": details["height"],
                "weight": details["weight"]
            })

    return pd.DataFrame(data)

def save_to_csv(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)