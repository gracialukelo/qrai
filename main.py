import qrcode


def build_qrcode(url):
    img = qrcode.make(url)
    img.save("YoloCourse.jpg")






if __name__ == "__main__":
    # YOLO QR Code
    url = "https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb"  

    print(f"Der Code wird erstellt...")
    build_qrcode(url=url)
    print(f"Der Code ist gespeichert.")