salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
spends = []
current_spend = spend
for month in range(months):
    spends.append(current_spend)
    current_spend *= (1 + increase)
needed_capital = 0
for i in range(months - 1, -1, -1):
    needed_capital = spends[i] + needed_capital - salary
    if needed_capital < 0:
        needed_capital = 0
money_capital = round(needed_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)