import random

symbol = ['🍒', '🍇', '🍉', '7️⃣ ']
results = random.choices(symbol, k=3)

print(f'{results[0]} | {results[1]} | {results[2]}')

if results.count(results[0]) == len(results) and results[0] == '7️⃣ ':
    print('Jackpot! 💰')
else:
    print('Thanks for playing!')