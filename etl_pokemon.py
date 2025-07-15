from utils import extract_pokemon_list, transform_pokemon_data, save_to_csv

def run_etl(limit=50):
    print("Starting ETL process...")
    pokemon_list = extract_pokemon_list(limit)
    df = transform_pokemon_data(pokemon_list)
    save_to_csv(df, "output/filtered_pokemon.csv")
    print("Done! File saved.")

if __name__ == "__main__":
    run_etl()
