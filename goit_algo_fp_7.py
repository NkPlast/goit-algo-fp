import random
import matplotlib.pyplot as plt

def monte_carlo_dice_rolls(num_rolls):
    counts = {i: 0 for i in range(2, 13)}  # Від 2 до 12 можливі суми двох кубиків
    
    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        counts[roll_sum] += 1
    
    probabilities = {k: (v / num_rolls) * 100 for k, v in counts.items()}
    return probabilities

def plot_probabilities(probabilities):
    # Теоретичні ймовірності відповідно до вашої таблиці
    theoretical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    # Сортування ключів для графіку
    keys = sorted(probabilities.keys())
    monte_carlo = [probabilities[k] for k in keys]
    theoretical = [theoretical_probabilities[k] for k in keys]
    
    plt.figure(figsize=(10, 5))
    plt.bar(keys, monte_carlo, width=0.4, label='Monte Carlo', color='b', align='center')
    plt.bar(keys, theoretical, width=0.4, label='Theoretical', color='r', alpha=0.7, align='edge')
    plt.xlabel('Sum of dice rolls')
    plt.ylabel('Probability (%)')
    plt.title('Monte Carlo Simulation vs Theoretical Probability of Dice Rolls')
    plt.legend()
    plt.xticks(keys)
    plt.show()

# Кількість кидків для симуляції
num_rolls = 100000
probabilities = monte_carlo_dice_rolls(num_rolls)
plot_probabilities(probabilities)

