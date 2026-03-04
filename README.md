# 🏅 Olympic Winter ETL & ML Pipeline

A Python ETL pipeline that extracts, transforms, and loads Olympic athlete data into a SQLite database — extended with Machine Learning for medal prediction and an AI-powered chatbot for natural language queries.

## What it does

- **Extract** – Downloads Olympic athlete and NOC region data from GitHub
- **Transform** – Filters for Winter Olympics, fills missing values, and cleans data types
- **Load** – Stores the cleaned data in a local SQLite database
- **Chatbot** – Natural language interface to query the database using Claude AI (Text-to-SQL)

## Project Structure

```
project/
├── src/
│   ├── extract.py         # Download and load CSV data
│   ├── transform.py       # Clean and transform data
│   ├── load.py            # Save data to SQLite
│   └── config.py          # URLs and constants
├── notebooks/
│   ├── eda.ipynb          # Exploratory data analysis
│   ├── query.ipynb        # SQL queries
│   └── chatbot.ipynb      # AI-powered chatbot
├── tests/
│   └── test_transform.py  # Unit tests
├── data/
│   └── olympics.db        # SQLite database (generated)
├── pipeline.py            # Main pipeline script
├── requirements.txt       # Python dependencies
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/project.git
cd project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=sk-ant-...
```

### 5. Run the pipeline

```bash
python3 pipeline.py run
```

The database will be created at `data/olympics.db`.

### 6. Run tests

```bash
pytest tests/
```

## AI Chatbot

The chatbot (`notebooks/chatbot.ipynb`) uses Claude AI to translate natural language questions into SQL queries.

```python
ask("Which country has won the most gold medals?")
# → Russia | 379
```

## Data Sources

- [Olympic History Dataset](https://github.com/rgriff23/Olympic_history) — athlete and event data from the modern Olympic Games
- NOC regions — country codes and region mapping

## Dependencies

- `pandas` – Data manipulation
- `anthropic` – Claude AI API
- `python-dotenv` – Environment variables
- `sqlite3` – Database storage (built into Python)
