import tkinter as tk


HEIGHT = 400
WIDTH = 600


root = tk.Tk()
root.title("AES Cryptography")


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor="n" )


entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.7, relheight=1)


open_button = tk.Button(frame, text="Open file", font=25)
open_button.place(relx=0.7, relwidth=0.3, relheight=1)

encrypt_button = tk.Button(root, text="Encrypt", font=40)
encrypt_button.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.2)

decrypt_button = tk.Button(root, text="Decrypt", font=40)
decrypt_button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.2)

exit_button = tk.Button(root, text="Exit", command = root.destroy)
exit_button.pack()

second_frame = tk.Frame(root, bg="white")
second_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.05, anchor="n")

label = tk.Label(second_frame, font=30, text = "Password:")
label.grid(row=0, column=1)


entry = tk.Entry(second_frame, font=30)
entry.grid(row=0, column=2)










label = tk.Label()

root.mainloop()

