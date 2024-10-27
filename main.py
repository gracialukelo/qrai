import qrcode


def build_qrcode(url):
    img = qrcode.make("https://realpython.com/if-name-main-python/")
    img.save("TheCode.jpg")






if __name__ == "__main__":
    url = "https://realpython.com/if-name-main-python/"

    print(f"Der Code wird erstellt...")
    build_qrcode(url=url)
    print(f"Der Code ist gespeichert.")