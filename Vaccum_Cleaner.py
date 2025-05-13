def vacuum_cleaner(env):
    location, status = env
    print(f"Initial: Location={location}, Status={status}")
    
    if status == "Dirty":
        print(f"Action: Suck")
        status = "Clean"
    
    if location == "A":
        print("Action: Move Right")
        location = "B"
    else:
        print("Action: Move Left")
        location = "A"
    
    print(f"Next: Location={location}, Status=Dirty")
    print("Action: Suck")
    print("Final: Both rooms are clean.")

environment = ("A", "Dirty")
vacuum_cleaner(environment)
