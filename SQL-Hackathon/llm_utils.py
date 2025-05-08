
import openai
import sqlite3

openai.api_key "Your API KEY"

def get_table_schema(db_path, table_name):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(f"PRAGMA table_info({table_name})")
    rows = c.fetchall()
    conn.close()
    schema_lines = [f"{row[1]} ({row[2]})" for row in rows]
    return "\n".join(schema_lines)

def ask_llm_for_sql(user_input, schema, table_name):
    prompt = f"""
You are an assistant that generates SQLite-compatible SQL queries.

The following table exists:
Table: {table_name}
Schema:
{schema}

User question: "{user_input}"

Generate a valid SQL query and a one-line explanation.
Output format:
SQL:
<SQL QUERY>

Explanation:
<Short explanation>
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
