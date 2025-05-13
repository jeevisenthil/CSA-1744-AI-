import calendar

def main():
    print("Calendar Generator")
    try:
        year = int(input("Enter Year (e.g. 2025): "))
        month = int(input("Enter Month (1-12): "))
        
        if 1 <= month <= 12:
            # Display the calendar for the given month and year
            print("\n" + calendar.month(year, month))
        else:
            print("Invalid month! Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter numeric values for year and month.")

if __name__ == "__main__":
    main()
