# Intelligent Summarization System Based on Large Language Model and GaussDB

This project is a natural language question-answering system built on PostgreSQL (compatible with GaussDB) and the DeepSeek API. Users can input natural language questions, and the system will automatically generate SQL queries, fetch answers from the database, and return human-readable responses.

## Project Structure

```bash
./
├── code/
│   ├── idsum.csv                     # Data file for the first table (id, summary)
│   ├── 视频1_summary_output.csv      # Data file for second table (video_id = 1)
│   ├── 视频2_summary_output.csv      # Data file for second table (video_id = 2)
│   ├── setup.py                      # Database initialization and data import
│   └── main.py                       # Main script for interactive Q&A
├── README.md
├── example.txt                       # Example question file
```

## Environment Requirements

Please make sure the following Python packages are installed:

```bash
pip install psycopg2 openai
```

Or using conda:
```bash
conda install psycopg2 openai
```

## Getting Started

1. Initialize the Database

Run the setup.py script to create the database and tables, and import data from the CSV files:

```bash
python code/setup.py
```

Make sure your database connection settings (host, port, user, password, etc.) are correctly configured.

2. Run the Q&A System

Run main.py to start the question-answering system. The process includes:

    1.Using the DeepSeek API to generate a SQL query based on the natural language question
    
    2.Executing the SQL query and retrieving results
    
    3.Using the DeepSeek API again to generate a natural language answer from the result
    
```bash
python code/main.py
```

Ensure that your DeepSeek API key and database configuration are correctly set in main.py.

3. DeepSeek API Configuration

This project uses the OpenAI SDK to call the DeepSeek API (OpenAI-compatible).

Replace the API key in main.py with your own DeepSeek API key.
    
Model used: deepseek-chat
    
API Base URL: https://api.deepseek.com

4. Common Issues

Make sure your .csv files are encoded in UTF-8.

5. Contact

If you have any questions, feel free to contact:bowen20041225@sina.com

This project is submitted as the final assignment for the Database Systems course (Instructor: Prof. De Peng Dang) at the School of Artificial Intelligence, Beijing Normal University, Spring Semester 2024–2025. Team Number: Group 1

6. License and Academic Use

You are welcome to use this project for non-commercial academic purposes. If you find it helpful for your work, please cite or acknowledge this repository.

However, academic integrity is important. Do not submit this project directly as your own coursework.
