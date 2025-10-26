import sqlite3, os
from plyer import notification


def notification_Show(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("SELECT Task, Inprogress FROM tasks WHERE Inprogress = ? ORDER BY Inprogress ASC LIMIT 3", (True,))
    inprogress_list = cursor.fetchall()

    cursor.execute("SELECT Task, Inprogress FROM tasks WHERE Inprogress = ? ORDER BY Inprogress ASC LIMIT 3", (False,))
    not_inprogress_list = cursor.fetchall()

    data = inprogress_list + not_inprogress_list

    if data:
        pesan = ""
        for i, row in enumerate(data[:3], start=1):
            Task, Inprogress = row
            Status = "Dalam Pengerjaan" if Inprogress else "Belum Dikerjakan"
            pesan += f"{i}. {Task} ({Status})\n"

        notification.notify(
            title= "3 List Teratas Project Yang Belum Selesai",
            message= pesan.strip(),
            timeout= 10
        )
    else:
        notification.notify(
            title = "List Project Saat Ini Kosong",
            message = "List Tidak Ada",
            timeout = 5
        )


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(root, "Tasks.db")
    notification_Show(file_path)