import json
from ll_client import ask_gigachat
def analyze_review_prompt(review_text: str) -> str:
    
    
    return prompt 
if __name__ == "__main__":
    user_review = """ """
    print("1. Формируем сложный промпт...")
    final_prompt = analyze_review_prompt(user_review)
    
    print("2. Отправляем запрос в GigaChat...")
    raw_response = ask_gigachat(final_prompt, temperature=0.1)
    print(f"\nСырой ответ от модели:\n{raw_respone}\n")
    print("3. Проверяем валидность полученного JSON...")
    try:
        parsed_json = json.loads(raw_response.strip())
        print("Успех! Данные успшно преобразованы в Python dict:")
        print(f"Тональность: {parsed_json.get('sentiment')}")
        print(f"Плюсы: {parsed_json.get('pros')}")
        print(f"Минусы: {parsed_json.get('cons')}")
    except json.JSONDecodeError:
        print("Ошибка: Модель нарушила формат и вернула невалидный JSON.")