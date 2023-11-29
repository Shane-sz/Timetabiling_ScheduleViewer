import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from schedule import Schedule
import csv

class TimetableGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PSB Academy Timetabling Scheduler Viewer")
        self.schedule_instance = Schedule()
        self.schedule_instance.retrieve_data_from_db()
        self.create_gui()

    def create_gui(self):
        label_style = ttk.Style()
        label_style.configure("TitleLabel.TLabel", font=("Arial", 18, "bold"), foreground="red")

        self.title_label = ttk.Label(self.root, text="PSB Academy Timetabling Scheduler Viewer", style="TitleLabel.TLabel")
        self.title_label.pack(pady=10)

        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=10)

        self.search_option = tk.StringVar()
        self.view_schedule_option_menu = ttk.OptionMenu(search_frame, self.search_option, "Search Options", "Location", "Module", "Date", "Lecturer", "Schedule Days")
        self.view_schedule_option_menu.grid(row=0, column=0, padx=5)

        self.search_entry = ttk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(search_frame, text="Search", style="SearchButton.TButton", command=self.display_timetable)
        self.search_button.grid(row=0, column=2, padx=5)

        self.sort_date_button = ttk.Button(self.root, text="Sort by Date", style="SortButton.TButton", command=self.sort_by_date)
        self.sort_date_button.pack(pady=10)

        self.download_button = ttk.Button(self.root, text="Download", style="DownloadButton.TButton", command=self.download_timetable)
        self.download_button.pack(pady=10)

        screen_height = self.root.winfo_screenheight()
        tree_height = int(0.7 * screen_height)  # Set table height to 70% of screen height

        self.tree = ttk.Treeview(self.root, height=tree_height, columns=(
            "Session", "Module", "Activity Dates", "Scheduled Days", "Start Time", "End Time", "Duration", "Location",
            "Planned Size", "Lecturer", "Zone"), show="headings")

        for col in range(1, 12):
            self.tree.column(f"#{col}", width=130, anchor="center")
            self.tree.heading(f"#{col}", text=self.tree.heading(f"#{col}")["text"], anchor="center")
            self.tree.tag_configure(f"col{col}", anchor="center")
            self.tree.heading(f"#{col}", anchor="center")

        self.tree.heading("#1", text="Session")
        self.tree.heading("#2", text="Module")
        self.tree.heading("#3", text="Activity Dates")
        self.tree.heading("#4", text="Scheduled Days")
        self.tree.heading("#5", text="Start Time")
        self.tree.heading("#6", text="End Time")
        self.tree.heading("#7", text="Duration")
        self.tree.heading("#8", text="Location")
        self.tree.heading("#9", text="Planned Size")
        self.tree.heading("#10", text="Lecturer")
        self.tree.heading("#11", text="Zone")

        # background and foreground colors for table headings
        heading_style = ttk.Style()
        heading_style.configure("Treeview.Heading", foreground="black", background="lightgray")

        self.tree.pack(pady=15)

    def display_timetable(self):
        query = self.search_entry.get()
        view_schedule_option = self.search_option.get()

        # Delete existing rows in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        search_mode = 0
        if view_schedule_option == "Lecturer":
            search_mode = 10
        elif view_schedule_option == "Location":
            search_mode = 8
        elif view_schedule_option == "Module":
            search_mode = 2
        elif view_schedule_option == "Date":
            search_mode = 3
        elif view_schedule_option == "Schedule Days":
            search_mode = 4

        results = self.schedule_instance.search(search_mode, query)

        if results:
            for idx, entry in enumerate(results, 12345):
                # even and odd rows for colors
                tag = "even" if idx % 2 == 0 else "odd"
                self.tree.insert("", "end", values=entry[1:], tags=(f"col{idx % 10 + 1}", tag))
                # selecting background color for the "even" and "odd"
                self.tree.tag_configure("even", background="lightgray")
                self.tree.tag_configure("odd", background="white")
        else:
            self.tree.insert("", "end", values=("No schedules found", "", "", "", "", "", "", "", "", "", ""))

    def sort_by_date(self):
        results = sorted(self.schedule_instance.schedule_data, key=lambda x: x[3])

        if results:
            for idx, entry in enumerate(results, 12345):
                tag = "even" if idx % 2 == 0 else "odd"
                self.tree.insert("", "end", values=entry[1:], tags=(f"col{idx % 10 + 1}", tag))
                self.tree.tag_configure("even", background="lightgray")
                self.tree.tag_configure("odd", background="white")
        else:
            self.tree.insert("", "end", values=("No schedules found", "", "", "", "", "", "", "", "", "", ""))

    def download_timetable(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

        if file_path:
            data = []
            for item in self.tree.get_children():
                values = self.tree.item(item, "values")
                data.append(values)

            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Session", "Module", "Activity Dates", "Scheduled Days", "Start Time", "End Time", "Duration",
                     "Location", "Planned Size", "Lecturer", "Zone"])
                writer.writerows(data)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimetableGUI(root)
    root.mainloop()
