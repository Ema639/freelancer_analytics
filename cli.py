import typer
from models.query_parser import parse_question
from db.db_loader import execute_query

app = typer.Typer()

@app.command()
def ask(question: list[str] = typer.Argument(...)):
    """Единичный запрос на естественном языке"""
    full_question = " ".join(question)
    sql_query = parse_question(full_question)
    print("Сформированный SQL-запрос:")
    print(sql_query)
    print("\nОтвет на запрос:")
    result = execute_query(sql_query)
    print(result)

@app.command()
def chat():
    """Интерактивный чат с ИИ-помощником"""
    print("💬 Чат-режим: просто вводи вопросы. Напиши 'exit' или 'quit' для выхода.\n")

    while True:
        try:
            question = input("> ").strip()
            if question.lower() in {"exit", "quit"}:
                print("До встречи!")
                break

            sql_query = parse_question(question)
            print("\nСформированный SQL-запрос:")
            print(sql_query)

            print("\nОтвет на запрос:")
            result = execute_query(sql_query)
            print(result)
            print()

        except KeyboardInterrupt:
            print("\nДо встречи!")
            break
        except Exception as e:
            print(f"Ошибка: {e}\n")

if __name__ == "__main__":
    app()


