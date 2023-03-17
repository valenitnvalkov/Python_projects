need_money = float(input())
money_now = float(input())

spent_counter = 0
days_counter = 0
con = False

while money_now < need_money:
    condition = input()
    current_sum = float(input())

    days_counter += 1

    if condition == "save":
        spent_counter = 0
        money_now += current_sum
    elif condition == "spend":
        spent_counter += 1

        if spent_counter == 5:
            print(f"You can't save the money.")
            print(f"{days_counter}")
            con = True
            break
        if current_sum > money_now:
            money_now = 0
        else:
            money_now -= current_sum

if not  con:
    print(f"You saved the money for {days_counter} days.")