import requests
from flask import Flask, request, jsonify

Uang = 0
Uang_F = format(Uang, ",").replace(",", ".")
Uang_SF = 0
Pros_UangF = 0

verify_token = "testing"
whatapps_token = "EAALjnH7JPo8BP9IZBTh8tWRhNSAZCHeXsUuX5LbRo1RUKSuGfzsEIVHK167NAI85imbPJnhzn0XSgb7KVwltvlyt0WZBHGooh1KokXO3GVGQHkkwBlmH5p30E205E8g1YlVmLGdOontt5S4eMQWVekS5CmGGvJZBfbIx6c5iBoZBPzlZAku3wpVcgqVz2fPQZDZD"
phone_id = "875624918960314"
wa_phone_number_H = 6285187367024

app = Flask(__name__)

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == verify_token:
        print("WEBHOOK Verified")
        send_message(wa_phone_number_H, f"Webhook Terverifikasi")
        return challenge, 200
    else:
        return "Verified Failed", 403
    

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(f"Data Masuk {data}")

    if data and data.get("entry"):
        try:
            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            sender = msg["from"]
            text = msg["text"]["body"]
            print(f"Pesan dari {sender} : {text}")

            Prosess_Command(sender, text)

        except Exception as e:
            print("Error parsing pesan", e)

    return jsonify({"status" : "ok"}), 200

def send_message(to, message):
    url = f"https://graph.facebook.com/v22.0/875624918960314/messages"
    headers = {
        "Authorization": f"Bearer {whatapps_token}",
        "Content-Type": "application/json"
    }
    data = {
    "messaging_product": "whatsapp",
    "to": to,
    "type": "text",
    "text": {
        "body": message
        }
    }

    r = requests.post(url, headers=headers, json=data)
    print("Status Balas", r.status_code, r.text)


def Prosess_Command(to, message):
    global Uang
    Uang_sebelum = Uang
    command_chat = ["/tabung", "/simpan", "/ambil", "/pakai", "/cek"]
    split_text = message.split()


    if not "/" in split_text[0]:
        send_message(to, f"Pesan Di Terima: {message}")
    else:
        if split_text[0] == command_chat[0] or split_text[0] == command_chat[1]:
            Uang += int(split_text[1])
            print(f"Uang Di Tambah {Uang_sebelum} + {split_text[1]} = {Uang}")
            format_Uang(Uang_sebelum, split_text[1])
            send_message(to, f"Uang Di Simpan Dari \n*Rp {Uang_SF}* Di Tambah *Rp {Pros_UangF}*\n\n Uang Saat Ini Senilai *Rp {Uang_F}*")
            
        elif split_text[0] == command_chat[2] or split_text[0] == command_chat[3]:
            Uang -= int(split_text[1])
            print(f"Uang Di Pakai {Uang_sebelum} - {split_text[1]} = {Uang}")
            format_Uang(Uang_sebelum, split_text[1])
            send_message(to, f"Uang Di Ambil Dari \n*Rp {Uang_SF}* Di Pakai *Rp {Pros_UangF}*\n\n Uang Saat Ini Senilai *Rp {Uang_F}*")

        elif split_text[0] == command_chat[4]:
            print(f"CeK Nilai Uang")
            format_Uang(Uang_sebelum, 0)
            send_message(to, f"Uang Mu Saat ini Adalah *Rp {Uang_F}*")
        
        else:
            send_message(to, f"Perintah Tidak Valid")


def format_Uang(UangSF, AddUangF):
    global Uang, Uang_F, Uang_SF, Pros_UangF
    Pros_UangF = format(int(AddUangF), ",").replace(",", ".")
    Uang_SF = format(UangSF, ",").replace(",", ".")
    Uang_F = format(Uang, ",").replace(",", ".")


if __name__ == "__main__":
    app.run(port=5000)