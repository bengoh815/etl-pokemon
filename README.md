# 🧬 Pokémon ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline that fetches Pokémon data from the [PokeAPI](https://pokeapi.co/), filters based on base experience, and saves the result as a CSV file.

This project is designed as an introductory ETL example for learning data engineering concepts using Python.

## 📌 Features

- Extracts a list of Pokémon from the public API
- Fetches detailed info for each Pokémon
- Filters Pokémon with `base_experience > 100`
- Transforms and structures the data into a clean format
- Loads the result into a CSV file

## 🛠 Tech Stack

| Layer          | Tool / Library |
| -------------- | -------------- |
| Language       | Python 3       |
| Data Fetch     | `requests`     |
| Data Transform | `pandas`       |
| Output         | CSV file       |


## 🚀 Getting Started

### 1. Clone the repo and create a virtual environment

```bash
git clone https://github.com/bengoh815/etl-pokemon.git
cd etl-pokemon
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the ETL pipeline

```bash
python etl_pokemon.py
```

The filtered Pokémon data will be saved to `output/filtered_pokemon.csv`.

## 📄 License

MIT License
