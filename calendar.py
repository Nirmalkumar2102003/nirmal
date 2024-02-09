def january():
    days = 31
    day = 1
    print("January 2024")
    print("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    for i in range(6):
        for j in range(7):
            if day <= days:
                print(f"{day:3}", end=" ")
                day += 1
            else:
                print(" ",end=" ")
        print()
january()
