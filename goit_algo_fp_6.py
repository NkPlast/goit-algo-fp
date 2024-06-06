def greedy_algorithm(items, budget):
    # Сортуємо елементи за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if info['cost'] <= budget:
            selected_items.append(item)
            budget -= info['cost']
            total_calories += info['calories']
            if budget <= 0:
                break
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо таблицю для збереження оптимальних значень калорій для кожного бюджету
    dp = [0] * (budget + 1)  # dp[j] буде містити максимальну калорійність для бюджету j

    for item, info in items.items():
        cost, calories = info['cost'], info['calories']
        for j in range(budget, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + calories)
    
    # Відновлення набору страв, які дають оптимальний результат
    selected_items = []
    j = budget
    for item, info in reversed(list(items.items())):
        cost, calories = info['cost'], info['calories']
        if j >= cost and dp[j] == dp[j - cost] + calories:
            selected_items.append(item)
            j -= cost
    
    return selected_items, dp[budget]

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print("Greedy Algorithm Result:", greedy_algorithm(items, budget))
print("Dynamic Programming Result:", dynamic_programming(items, budget))
