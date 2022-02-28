from tkinter import *


class GuiQRGen:
    def __init__(self, function_button):
        window = Tk()

        window.geometry("1080x720")
        window.configure(bg="#ffffff")
        canvas = Canvas(
            window,
            bg="#ffffff",
            height=720,
            width=1080,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f".\\images\\background.png")
        background = canvas.create_image(540.0, 360.0, image=background_img)

        img0 = PhotoImage(file=f".\\images\\img0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: function_button(entry0.get("1.0", END)),
            relief="flat",
        )

        b0.place(x=725, y=545, width=170, height=44)

        entry0_img = PhotoImage(file=f".\\images\\img_textBox0.png")
        entry0_bg = canvas.create_image(809.5, 391.5, image=entry0_img)

        entry0 = Text(bd=0, bg="#ffffff", highlightthickness=0)

        entry0.place(x=687.0, y=254, width=245.0, height=273)

        window.resizable(False, False)
        window.mainloop()


if __name__ == "__main__":
    GuiQRGen(lambda x: print("Button Clicked", x))
