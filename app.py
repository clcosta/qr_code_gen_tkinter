import os
from tkinter import messagebox
from typing import Optional

import qrcode
from interface import GuiQRGen


def create_QR(
    value: str,
    *,
    filename: Optional[str] = "QR",
    path_output: Optional[str] = ".\\output\\"
):
    qr = qrcode.make(value)
    filename = filename + ".png" if len(filename.split(".")) == 1 else filename
    qr.save(os.path.join(path_output, filename))
    return messagebox.showinfo(
        title="QR CODE GENERATOR", message="QR Code criado com sucesso!"
    )


if __name__ == "__main__":
    GuiQRGen(create_QR)
