import sqlite3


texts = {
    "id" : {
        "Title" : "---------- Task ----------",
        "title Menu" : "---------- Menu Tugas ----------",
        "Menu" : [
            "Tambah Tugas",
            "Lihat Tugas",
            "Hapus Tugas",
            "Tandai Tugas Dalam Proses",
            "Tandai Tugas Selesai",
            "Lihat Tugas Yang Sudah Selesai",
            "Lihat Tugas Berdasarkan ID",
            "Ganti Mode",
            "Ganti Bahasa",
            "Keluar"
        ],
        "Title List" : "---------- List Tugas ----------",
        "Title List Done" : "---------- Tugas Selesai ----------",
        "Added Task" : "Tugas Baru Telah Di Tambahkan",
        "Input Task" : "Masukan Tugas Baru : ",
        "Input Choice" : "Pilih Menu : ",
        "Input Inprogress" : "Masukan ID Tugas Yang Mau Di Tandai Dalam Progress : ",
        "Task Inprogress" : "Tugas Telah Di Tandai Dalam Progress",
        "Input Done" : "Masukan ID Tugas Yang Mau Di Tandai Sudah Selesai : ",
        "Task Done" : "Tugas Telah Di Tandai Sudah Selesai",
        "Input Delete" : "Masukan ID Tugas Yang Mau Di Hapus : ",
        "Task Deleted" : "Tugas Berhasil Di Hapus",
        "No Task" : "Tidak Ada Tugas Atau Daftar Tugas Belum Di Isi",
        "Done" : "Selesai",
        "Pending" : "Belum Dikerjakan",
        "Inprogress" : "Dalam Pengerjaan",
        "Exit" : "Keluar ....",
        "Lang Changed" : "Bahasa Telah Di Ganti Ke Indonesia",
        "ID Error" : "ID Harus Berupa Angka",
        "Input View" : "Masukan ID Tugas Yang Mau DI Cek"
    },
    "en" : {
        "Title" : "---------- Task ----------",
        "title Menu" : "---------- Task Menu ----------",
        "Menu" : [
            "Add Task",
            "View Task",
            "Delete Task",
            "Mark Task Inprogress",
            "Mark Task Done",
            "View Completed Taks",
            "View Task From ID",
            "Change Mode",
            "Change Language",
            "Exit"
        ],
        "Title List" : "---------- Task List ----------",
        "Title List Done" : "----------- Task Done -----------",
        "Added Task" : "New Task Has Been Added",
        "Input Task" : "Input New Task : ",
        "Input Choice" : "Choose Menu : ",
        "Input Inprogress" : "Input ID Of Task To Mark Inprogress : ",
        "Task Inprogress" : "Task Has Been Marked InProgress",
        "Input Done" : "Input ID Of Task To Mark Done : ",
        "Task Done" : "Task Has Been Marked Done",
        "Input Delete" : "Input ID Of Task To Delete : ",
        "Task Deleted" : "Task Successfully Deleted",
        "No Task" : "Task Empty Or Task List Not Filled Yet",
        "Done" : "Done",
        "Pending" : "Pending",
        "Inprogress" : "Inprogress",
        "Exit" : "Exiting ....",
        "Lang Changed" : "Language Changed To English",
        "ID Error" : "ID Must Be A Number",
        "Input View" : "Input ID To Cek The Task"
    }
}

language_n = 0
language = "id"


## Language Code
def language_check(n):
    global language
    global language_n
    if n == 0:
        language = "id"
    elif n == 1:
        language = "en"
    else:
        print("Error Value Language Set To Default Id (Indonesian)")
        language = "id"
        language_n = 0

def t(key):
    return texts[language][key]

    
## Data Base Code
def setup_done():
    conn = sqlite3.connect("Tasks_Done.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Task TEXT,
                Done BOOLEAN
    )                  
    """)
    conn.commit()
    conn.close()

def view_complete_taks():
    conn = sqlite3.connect("Tasks_Done.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    print("\n"*50, t("Title List Done"), "\n")
    if not rows:
        print(t("No Task"))
    else:
        for row in rows:
            id, Task, Done = row
            status = t("Done") if Done else t("Inprogress")
            print(f"{id}. {Task} [{status}]")
    print("\n", t("Title List Done"), "\n")
    
def Connect():
    return sqlite3.connect("Tasks.db")

def setup():
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Task TEXT,
                Inprogress BOOLEAN
    )                  
    """)
    conn.commit()
    conn.close()

def add_task(task):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (Task, Inprogress) VALUES (?, ?)", (task, False))
    conn.commit()
    conn.close()

def view_task():
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    print("\n"*50, t("Title List"), "\n")
    if not rows:
        print(t("No Task"))
    else:
        for row in rows:
            id, Task, Inprogress = row
            status = t("Inprogress") if Inprogress else t("Pending")
            print(f"{id}. {Task} [{status}]") 
    print("\n", t("Title List"),"\n")

def delete_task(task_id):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def Inprogress_task(task_id):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET Inprogress = ? WHERE id = ?", (True, task_id))
    conn.commit()
    conn.close()

def done_task(task_id):
    conn = Connect()
    conn1 = sqlite3.connect("Tasks_Done.db")
    cursor = conn.cursor()
    cursor1 = conn1.cursor()
    
    cursor.execute("SELECT Task, Inprogress FROM tasks WHERE id = ?", (task_id,))
    temp_data = cursor.fetchone()
    cursor1.execute("INSERT INTO tasks (Task, Done) VALUES (?, ?)", temp_data)
    conn1.commit()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    last_id = cursor1.lastrowid
    cursor1.execute("UPDATE tasks SET Done = ? WHERE id = ?", (True, last_id))

    conn1.commit()
    conn.commit()

    conn.close()
    conn1.close()

def view_n_task(task_id):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Task, Inprogress FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    print(f"{task_id}. {task}")
    conn.close()

## Main Code

def main():
    global language_n
    global Mode
    setup()
    setup_done()
    while True:
        print("\n", t("title Menu"), "\n")

        for i, item in enumerate(t("Menu"), 1):
            print(f"{i}. {item} ")

        print("\n", t("title Menu"), "\n")

        choice = int(input(t("Input Choice")))

        if choice == 1:
            task = input(t("Input Task"))
            add_task(task)
            print("\n"*30, t("Added Task"))

        elif choice == 2:
            view_task()
            print("\n"*2)

        elif choice == 3:
            view_task()
            print("\n"*2, t("Title"))
            while True:
                try:
                    task_id = int(input(t("Input Delete")))
                    delete_task(task_id)
                    print("\n", t("Task Deleted"))
                    break

                except ValueError:
                    print("\n", t("ID Error"), "\n")

            print("\n", t("Title"))
        
        elif choice == 4:
            view_task()
            print("\n"*2, t("Title"))
            while True:
                try:
                    task_id = int(input(t("Input Inprogress")))
                    Inprogress_task(task_id)
                    print("\n", t("Task Inprogress"))
                    break

                except ValueError:
                    print("\n", t("ID Error"), "\n")

            print("\n", t("Title"))
        
        elif choice == 5:
            view_task()
            print("\n"*2, t("Title"))
            while True:
                try:
                    task_id = int(input(t("Input Done")))
                    done_task(task_id)
                    print("\n", t("Task Done"))
                    break

                except ValueError:
                    print("\n", t("ID Error"), "\n")

            print("\n", t("Title"))

        elif choice == 6:
            view_complete_taks()

        elif choice == 7:
            view_task()
            print("\n"*2, t("Title"))
            while True:
                try:
                    task_id = int(input(t("Input View")))
                    view_n_task(task_id)
                    print("\n", t("Task Done"))
                    break

                except ValueError:
                    print("\n", t("ID Error"), "\n")

            print("\n", t("Title"))

        elif choice == 8:
            Mode = 2
            print("Change Mode ", Mode)
            break
        
        elif choice == 9:
            language_n = not language_n
            language_check(language_n)
            print("\n"*50, t("Title"), "\n", t("Lang Changed"), "\n")

        elif choice == 10:
            print("\n", t("Exit"))
            break

        else:
            print("Error Data")


main()