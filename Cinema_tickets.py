standard = 0
kid = 0
student = 0

film_name = input()
while film_name != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for free_tickets in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student += 1
        elif current_ticket == "standard":
            standard += 1
        elif current_ticket == "kid":
            kid += 1
        sold_seats += 1

    percent = sold_seats / free_seats * 100
    print(f"{film_name} - {percent:.2f}% full.")

    film_name = input()

total_tickets = kid + student + standard

print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")