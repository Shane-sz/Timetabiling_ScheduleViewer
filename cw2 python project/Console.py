import schedule
from schedule import print_schedule_entry

def view_timetable():
    schedule_instance = schedule.Schedule()
    schedule_instance.retrieve_data_from_db()

    while True:
        print("\nView Timetable Options:")
        print("1. View by Lecturer")
        print("2. View by Allocated Location Name")
        print("3. View by Module")
        print("4. View by Selecting Date")
        print("5. View Entire Timetable")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            lecturer_name = input("Enter the name of the lecturer: ")
            results = schedule_instance.search(10, lecturer_name)
            if results:
                print("\nSchedules for Lecturer:", lecturer_name)
                for entry in results:
                    print_schedule_entry(entry)
            else:
                print("No schedules found for the lecturer:", lecturer_name)

        elif choice == "2":
            Allocated_Location_Name = input("Enter the name of the Allocated Location Name: ")
            results = schedule_instance.search(8, Allocated_Location_Name)
            if results:
                print("\nSchedules for Allocated Location Name:", Allocated_Location_Name)
                for entry in results:
                    print_schedule_entry(entry)
            else:
                print("No schedule found for Allocated Location Name:", Allocated_Location_Name)

        elif choice == "3":
            module_name = input("Enter the name of the Module: ")
            results = schedule_instance.search(2, module_name)
            if results:
                print("\nSchedules for Module:", module_name)
                for entry in results:
                    print_schedule_entry(entry)
            else:
                print("No schedule found for the Module:", module_name)

        elif choice == "4":
            date = input("Enter the date range (e.g., '6/4/2021 to 4/6/2021'): ")
            results = schedule_instance.search(3, date)
            if results:
                print("\nSchedules for Date Range:", date)
                for entry in results:
                    print_schedule_entry(entry)
            else:
                print("No schedule found for this date range:", date)

        elif choice == "5":
            print("\nEntire Timetable:")
            schedule_instance.print_all()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    view_timetable()
