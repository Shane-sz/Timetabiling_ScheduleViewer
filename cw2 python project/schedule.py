from datetime import datetime
from hashTable import HashTable
from database import retrieve

class Schedule:
    def __init__(self):
        self.schedule = HashTable()
        self.retrieve_data_from_db()

    def retrieve_data_from_db(self):
        self.schedule_data = retrieve()

    #linear search
    def search(self, search_mode, search_value):
        results = []

        for entry in self.schedule_data:
            if entry[search_mode] == search_value:
                results.append(entry)
        return results

    def print_all(self):
        for entry in self.schedule_data:
            print_schedule_entry(entry)

    def sort_by_date(self):
        self.schedule_data.sort(key=lambda x: datetime.strptime(x[3], "%d %B %Y"))

def print_schedule_entry(entry):
    print(f"ID: {entry[0]}, Session Name: {entry[1]}, Module Name: {entry[2]}, Activity Dates: {entry[3]}, ScheduledDays: {entry[4]}, Start Time: {entry[5]}, End Time: {entry[6]}, Duration: {entry[7]}, Allocated Location Name: {entry[8]}, Size: {entry[9]}, Lecturer Name: {entry[10]}, Zone Name: {entry[11]}")
