

# Sample student data
student_data = {
    "24BSCYS001": {"password": "2401", "name": "HANIA",  "results": {"Applied Calculus": 27, "Programming Fundamental": 29, "Functional English": 26,"Descreate structure": 20, "IICT":28,}},
    "24BSCYS002": {"password": "2402", "name": "SOURAJ",  "results": {"Applied Calculus": 26, "Programming Fundamental": 22, "Functional English": 26, "Descreate Structure": 28, "IICT":24}},
    "24BSCYS003": {"password": "2403", "name": "FIZA GADHIR", "results": {"Applied calculus": 25, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 23, "IICT": 29}},
    "24BSCYS005": {"password": "2405", "name": "DANIYAL", "results": {"Applied calculus": 26, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 22, "IICT": 27}},
    "24BSCYS006": {"password": "2406", "name": "SAMYA AYAZ", "results": {"Applied calculus": 25, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 27, "IICT": 28}},
    "24BSCYS007": {"password": "2407", "name": "FAISAL", "results": {"Applied calculus": 27, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 28, "IICT": 28}},
    "24BSCYS008": {"password": "2408", "name": "AISHA KHALID", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 22, "Descreate structure": 29, "IICT": 23}},
    "24BSCYS009": {"password": "2409", "name": "MANSAB ABBASI", "results": {"Applied calculus": 23, "Programing fundamental": 25, "Functional English": 22, "Descreate structure": 22, "IICT": 23}},
    "24BSCYS010": {"password": "2410", "name": "HASNAIN ABBASI", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 23, "IICT": 22}},
    "24BSCYS011": {"password": "2501", "name": "ASHJA KHAN", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 23, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS012": {"password": "2502", "name": "HABIBA KHAN", "results": {"Applied calculus": 23, "Programing fundamental": 25, "Functional English": 23, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS013": {"password": "2503", "name": "ERUM", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 23, "Descreate structure": 20, "IICT": 20}},
    "24BSCYS014": {"password": "2504", "name": "MUHAMMAD ZAWAR", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 23, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS015": {"password": "2505", "name": "MUHAMMAD SUFIYAN", "results": {"Applied calculus": 25, "Programing fundamental": 22, "Functional English": 24, "Descreate structure": 24, "IICT": 20}},
    "24BSCYS016": {"password": "2506", "name": "AHMED YASEEN", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 22, "Descreate structure": 24, "IICT": 25}},
    "24BSCYS017": {"password": "2507", "name": "MUHAMMAD FAIZAN", "results": {"Applied calculus": 23, "Programing fundamental": 25, "Functional English": 22, "Descreate structure": 24, "IICT": 26}},
    "24BSCYS018": {"password": "2508", "name": "HANIA", "results": {"Applied calculus": 23, "Programing fundamental": 26, "Functional English": 23, "Descreate structure": 22, "IICT": 24}},
    "24BSCYS019": {"password": "2509", "name": "GOUTAM KUMAR", "results": {"Applied calculus": 23, "Programing fundamental": 21, "Functional English": 24, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS021": {"password": "2601", "name": "ZAKIR HUSSAIN", "results": {"Applied calculus": 23, "Programing fundamental": 21, "Functional English": 25, "Descreate structure": 21, "IICT": 23}},
    "24BSCYS022": {"password": "2602", "name": "ZAMIN ALI MEMON", "results": {"Applied calculus": 23, "Programing fundamental": 21, "Functional English": 22, "Descreate structure": 21, "IICT": 27}},
    "24BSCYS023": {"password": "2603", "name": "MUEED KAIMKHANI", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 22, "Descreate structure": 22, "IICT": 23}},
    "24BSCYS024": {"password": "2604", "name": "DURGESH KUMAR", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 25, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS025": {"password": "2605", "name": "ZAMIN ALI MASTOI", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 24, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS026": {"password": "2606", "name": "MUHAMMAD TARIQ", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 23, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS027": {"password": "2607", "name": "ABRISH KHAN", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS028": {"password": "2608", "name": "MUHAMMAD TAHA", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 25, "IICT": 20}},
    "24BSCYS029": {"password": "2609", "name": "JAWAD NIZAM", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 22, "Descreate structure": 24, "IICT": 30}},
    "24BSCYS030": {"password": "2610", "name": "ZAHID HUSSAIN", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 22, "Descreate structure": 24, "IICT": 29}},
    "24BSCYS031": {"password": "2701", "name": "MUHAMMAD HASEEB", "results": {"Applied calculus": 25, "Programing fundamental": 22, "Functional English": 22, "Descreate structure": 23, "IICT": 29}},
    "24BSCYS032": {"password": "2702", "name": "SIKANDAR BAREJO", "results": {"Applied calculus": 24, "Programing fundamental": 23, "Functional English": 22, "Descreate structure": 21, "IICT": 24}},
    "24BSCYS033": {"password": "2703", "name": "KEWAL KOHLI", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 23, "Descreate structure": 21, "IICT": 22}},
    "24BSCYS034": {"password": "2704", "name": "NIL", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 23, "Descreate structure": 22, "IICT": 23}},
    "24BSCYS035": {"password": "2705", "name": "MARIA", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 24, "Descreate structure": 22, "IICT": 23}},
    "24BSCYS036": {"password": "2706", "name": "IQRAR ALI", "results": {"Applied calculus": 23, "Programing fundamental": 22, "Functional English": 25, "Descreate structure": 22, "IICT": 23}},
    "24BSCYS037": {"password": "2707", "name": "NIL", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 25, "Descreate structure": 22, "IICT": 25}},
    "24BSCYS038": {"password": "2708", "name": "ABDUL SAMAD", "results": {"Applied calculus": 3, "Programing fundamental": 24, "Functional English": 25, "Descreate structure": 22, "IICT": 25}},
    "24BSCYS039": {"password": "2709", "name": "WAJID ALI", "results": {"Applied calculus": 23, "Programing fundamental": 25, "Functional English": 24, "Descreate structure": 23, "IICT": 24}},
    "24BSCYS040": {"password": "2710", "name": "AHSAN ALI", "results": {"Applied calculus": 23, "Programing fundamental": 26, "Functional English": 24, "Descreate structure": 23, "IICT": 24}},
    "24BSCYS041": {"password": "2801", "name": "HASEEB UR REHMAN", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 24, "Descreate structure": 25, "IICT": 23}},
    "24BSCYS042": {"password": "2802", "name": "RIMSHA", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 24, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS043": {"password": "2803", "name": "ARCHANA LOHANA", "results": {"Applied calculus": 24, "Programing fundamental": 23, "Functional English": 24, "Descreate structure": 26, "IICT": 26}},
    "24BSCYS044": {"password": "2804", "name": "ZAKIR ALI", "results": {"Applied calculus": 26, "Programing fundamental": 24, "Functional English": 22, "Descreate structure": 24, "IICT": 25}},
    "24BSCYS045": {"password": "2805", "name": "MUHAMMAD SAMEER", "results": {"Applied calculus": 23, "Programing fundamental": 25, "Functional English": 22, "Descreate structure": 25, "IICT": 23}},
    "24BSCYS046": {"password": "2806", "name": "MAZHAR ALI", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 24, "Descreate structure": 25, "IICT": 25}},
    "24BSCYS047": {"password": "2807", "name": "SHARDHA ARTI", "results": {"Applied calculus": 23, "Programing fundamental": 24, "Functional English": 12, "Descreate structure": 25, "IICT": 25}},
    "24BSCYS048": {"password": "2808", "name": "SAFA", "results": {"Applied calculus": 23, "Programing fundamental": 23, "Functional English": 25, "Descreate structure": 23, "IICT": 13}},
    "24BSCYS049": {"password": "2809", "name": "NIL", "results": {"Applied calculus": 25, "Programing fundamental": 26, "Functional English": 22, "Descreate structure": 23, "IICT": 23}},
    "24BSCYS050": {"password": "2810", "name": "MUHAMMAD HZAIFA", "results": {"Applied calculus": 24, "Programing fundamental": 25, "Functional English": 24, "Descreate structure": 23, "IICT": 24}},
    "24BSCYS051": {"password": "2901", "name": "ASHOK KUMAR", "results": {"Applied calculus": 28, "Programing fundamental": 27, "Functional English": 25, "Descreate structure": 22, "IICT": 24}},
}

# Maximum marks for each subject
MAX_MARKS = 30
TOTAL_SUBJECTS = 5
MAX_TOTAL_MARKS = MAX_MARKS * TOTAL_SUBJECTS

# Function to handle login
def login():
    roll = roll_entry.get().strip()
    password = password_entry.get().strip()
    
    if not roll or not password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if roll in student_data:
        if student_data[roll]["password"] == password:
            display_result(roll)
        else:
            messagebox.showerror("Error", "Incorrect password.")
    else:
        messagebox.showerror("Error", "Roll number not found.")

# Function to display results
def display_result(roll):
    result_window = tk.Toplevel(root)
    result_window.title("Student Results")
    result_window.geometry("700x500")
    result_window.configure(bg="#eef6f9")

    # Header
    tk.Label(result_window, text="Student Results", font=("Arial", 20, "bold"), bg="#eef6f9", fg="#4682b4").pack(pady=10)
    
    # Student Information
    tk.Label(result_window, text=f"Name: {student_data[roll]['name']}", font=("Arial black", 14), bg="#eef6f9").pack(pady=5)
    tk.Label(result_window, text=f"Roll Number: {roll}", font=("Arial black", 14), bg="#eef6f9").pack(pady=5)

    # Result Header
    tk.Label(result_window, text="Subjects and Marks", font=("arial rounded MT bold", 14, "bold"), bg="#eef6f9").pack(pady=10)

    # Create Table for Results
    table_frame = tk.Frame(result_window, bg="#eef6f9")
    table_frame.pack(pady=10)
    
    tree = ttk.Treeview(table_frame, columns=("Subject", "Marks"), show="headings", height=len(student_data[roll]["results"]))
    tree.column("Subject", width=200, anchor="center")
    tree.column("Marks", width=100, anchor="center")
    tree.heading("Subject", text="Subject")
    tree.heading("Marks", text="Marks")
    
    total_marks = 0
    for subject, marks in student_data[roll]["results"].items():
        total_marks += marks
        tree.insert("", "end", values=(subject, marks))
    tree.pack()

    # Percentage Calculation
    percentage = (total_marks / MAX_TOTAL_MARKS) * 100

    # Total Marks and Percentage Display
    tk.Label(result_window, text=f"Total Marks: {total_marks}/{MAX_TOTAL_MARKS}", font=("Arial bold", 14), bg="#eef6f9").pack(pady=5)
    tk.Label(result_window, text=f"Percentage: {percentage:.2f}%", font=("Arial bold", 14, "bold"), bg="#eef6f9", fg="#2e8b57").pack(pady=5)

    # Close Button
    tk.Button(result_window, text="Close", command=result_window.destroy, font=("Arial", 12), bg="#4682b4", fg="white").pack(pady=10)

# Function to clear login fields
def clear_fields():
    roll_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("Student Result Management System")
root.geometry("500x450")
root.configure(bg="#eef6f9")
root.resizable(False, False)

# Title
tk.Label(root, text="Student Result Management System", font=("Arial", 18, "bold"), bg="#eef6f9", fg="#4682b4").pack(pady=10)

# Login Frame
login_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
login_frame.pack(pady=20, ipadx=20, ipady=10)

tk.Label(login_frame, text="Login", font=("Arial bold", 16, "bold"), bg="#ffffff", fg="#4682b4").pack(pady=10)

# Roll Number
tk.Label(login_frame, text="Roll Number:", font=("Arial bold", 12), bg="#ffffff").pack(pady=5)
roll_entry = tk.Entry(login_frame, font=("Arial", 12), width=30)
roll_entry.pack(pady=5)

# Password
tk.Label(login_frame, text="Password:", font=("Arial bold", 12), bg="#ffffff").pack(pady=5)
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(login_frame, bg="#ffffff")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Login", command=login, font=("Arial", 12), bg="#4682b4", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields, font=("Arial", 12), bg="#4682b4", fg="white", width=10).grid(row=0, column=1, padx=5)

# Exit Button
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="#b22222", fg="white", width=15).pack(pady=20)

# Run the application
root.mainloop()
