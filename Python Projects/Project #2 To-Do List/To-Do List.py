import sqlite3
import os

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
            "Ganti Bahasa",
            "Keluar"
        ],
        "Title List" : "---------- List Tugas ----------",
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
        "ID Error" : "ID Harus Berupa Angka"
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
            "Change Language",
            "Exit"
        ],
        "Title List" : "---------- Task List ----------",
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
        "ID Error" : "ID Must Be A Number"
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

def Connect():
    DB_file  = os.path.join("Python Projects/Project #2", "Tasks.db")
    return sqlite3.connect(DB_file)

def setup():
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Task TEXT,
                   Inprogress BOOLEAN,
                   Done BOOLEAN
    )                  
    """)
    conn.commit()
    conn.close()

def add_task(task):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (Task, Inprogress, Done) VALUES (?, ?, ?)", (task, False, False))
    conn.commit()
    conn.close()

def view_task():
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    print("\n", t("Title List"), "\n")
    if not rows:
        print(t("No Task"))
    else:
        for row in rows:
            id, Task, Inprogress, Done = row
            status = t("Done") if Done else t("Inprogress") if Inprogress else t("Pending")
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
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET Done = ? WHERE id = ?", (True, task_id))
    cursor.execute("UPDATE tasks SET Inprogress = ? WHERE id = ?", (False, task_id))
    conn.commit()
    conn.close()

## Main Code

def main():
    global language_n
    setup()
    while True:
        print("\n", t("title Menu"), "\n")

        for i, item in enumerate(t("Menu"), 1):
            print(f"{i}. {item} ")

        print("\n", t("title Menu"), "\n")
        
        choice = int(input(t("Input Choice")))

        if choice == 1:
            task = input(t("Input Task"))
            add_task(task)
            print(t("Added Task"))

        elif choice == 2:
            view_task()

        elif choice == 3:
            view_task()
            print("\n", t("Title"))
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
            print("\n", t("Title"))
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
            print("\n", t("Title"))
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
            language_n = not language_n
            language_check(language_n)
            print("\n", t("title"), "\n", t("Lang Changed"), "\n")

        elif choice == 7:
            print("\n", t("Exit"))
            break
        

main()