import asyncio
import requests

async def send_post_request(charname, cdkey):
    url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"

    payload = {
        'ac': 'get_gifts',
        'type': '1',
        'iggid': '0',
        'charname': charname,
        'cdkey': cdkey,
        'lang': 'ru'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(f"Запрос успешно отправлен для {charname.strip()} с кодом {cdkey.strip()}!")
        try:
            data = response.json()
            print("Ответ сервера:", data["msg"])
        except ValueError:
            print(f"Ошибка при обработке ответа для {charname.strip()} с кодом {cdkey.strip()}: Некорректный JSON")
    else:
        print(
            f"Произошла ошибка при отправке запроса для {charname.strip()} с кодом {cdkey.strip()}: {response.status_code}")

async def main():
    with open("names.txt", "r") as names_file, open("gift_codes.txt", "r") as codes_file:
        names = [name.strip() for name in names_file.readlines() if name.strip()]  # Удаляем пустые строки
        codes = [code.strip() for code in codes_file.readlines() if
                 not code.startswith("#") and code.strip()]  # Удаляем строки, начинающиеся с '#' и пустые строки

    for name in names:
        for code in codes:
            await send_post_request(name, code)
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
