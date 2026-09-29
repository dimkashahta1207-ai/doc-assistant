def ask_gigachat(prompt: str, temperature: float=0.3) -> str:
    credentials = os.getenv("GIGACHAT_CREDENTIALS")
    if not credentials:
        raise ValueError("Ошибка: Переменная GIGACHAT_CREDENTIALS не найдена в .env")
    with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
        response = giga.chat({
            "model": "GigaChat-3-Lightning",
            "temperature": temperature,
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
        return response.choices[0].message.content
if __name__ == "__main__":
    print("Проверка связи с GigaChat...")
    test_question = "Что такое промпт-инжинеринг в трёх предложениях?"
    try:
        answer = ask_gigachat(test_question)
        print(f"\nВопрос: {test_question}")
        print(f"Ответ:\n{answer}")
    except Exception as e:
        print(f"Произошла ошибка при подключении: {e}")