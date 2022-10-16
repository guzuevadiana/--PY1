salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
#current_month = 0


# while current_month < months:
#     need_money += salary - spend
#     spend = spend * (1 + increase)
#     current_month += 1

for _ in range(months):
    need_money += salary - spend
    spend = spend * (1 + increase)

need_money = abs(need_money)

print(round(need_money))
