import tkinter
from tkinter import *
from note.note import Note

class noteEditGUI:
    def __init__(self, title, content):
        CANVAS_SIZE_WIDTH = 1100  # canvas 가로 길이
        CANVAS_SIZE_HEIGHT = 750  # canvas 세로 길이

        # root
        self.root = tkinter.Tk()
        self.root.title("노트 수정")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)  # 창 길이 조절 불가능

        # background image
        wall = PhotoImage(file="../image/note_bg.PNG")
        wall_label = Label(image=wall)
        wall_label.place(x=-2, y=-2)

        # PhotoImage(back)
        img_back = tkinter.PhotoImage(file="../image/button_back.PNG")
        btn_back = tkinter.Button(self.root, image=img_back, relief="solid", highlightthickness=0, borderwidth=0,
                                  command=lambda: self.btnBack(title, content))
        btn_back.place(x=10, y=10)

        # label(노트 수정)
        label = tkinter.Label(self.root, text="노트 수정", foreground="#ffffff", background="#503A2E", font=("Nirmala UI", "35", 'bold'))
        label.pack(pady=50)

        # entry(title)
        entry_title = tkinter.Entry(self.root, width=59, background="#FAF7F4", font=("Nirmala UI", "20"), borderwidth=9,
                                    relief="flat")
        entry_title.insert(0, title)
        entry_title.place(x=99, y=210)

        # text(content)
        text_con = tkinter.Text(self.root, width=60, height=9, background="#FAF7F4", wrap='word',
                                font=("Nirmala UI", "20"), spacing1=7)
        text_con.insert(tkinter.CURRENT, content)
        text_con.place(x=99, y=290)

        # button(save)
        btn_new = tkinter.Button(self.root, text="SAVE", width=8, foreground="#000000", background="#CCB9A8", relief="raised",
                                 font=("Arial", "20"), command=lambda: self.btnSave(title, entry_title.get(), text_con.get("1.0", END)))
        btn_new.place(x=910, y=120)


        self.root.mainloop()

    # Click event
    def btnSave(self, title, mTitle, mContent):
        from GUI.noteListGUI import noteListGUI
        Note.update_note(None, title, mTitle, mContent)
        tkinter.messagebox.showinfo("수정 확인", "수정되었습니다")
        self.root.destroy()
        noteListGUI()

    def btnBack(self, title, content):
        from GUI.noteDetailGUI import noteDetailGUI
        self.root.destroy()
        noteDetailGUI(title, content)

if __name__ == '__main__':
    noteEditGUI = noteEditGUI()
