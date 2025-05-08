
import sqlite3
from llm_utils import get_table_schema, ask_llm_for_sql

DB_PATH = "results.db"
TABLE_NAME = "results"

def run_query(sql):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute(sql)
        rows = c.fetchall()
        print("\nResult:")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error running query: {e}")
    finally:
        conn.close()

def main():
    print("🧠 LLM SQL Assistant")
    print("Type your question or 'exit' to quit.")

    schema = get_table_schema(DB_PATH, TABLE_NAME)

    while True:
        user_input = input("\n> ").strip()
        if user_input.lower() in ['exit', 'quit']:
            break

        print("\n⏳ Asking LLM to generate SQL...")
        response = ask_llm_for_sql(user_input, schema, TABLE_NAME)

        if "SQL:" in response:
            try:
                sql_section = response.split("SQL:")[1].split("Explanation:")[0].strip()
                explanation = response.split("Explanation:")[1].strip()
                print(f"\n✅ Generated SQL:\n{sql_section}")
                print(f"📝 Explanation: {explanation}")
                run_query(sql_section)
            except Exception as e:
                print(f"⚠️ Unable to parse LLM response:\n{response}\nError: {e}")
        else:
            print(f"⚠️ Unexpected LLM response:\n{response}")

if __name__ == "__main__":
    main()
