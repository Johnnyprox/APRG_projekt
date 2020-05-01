import tkinter as tk


HEIGHT = 400
WIDTH = 600


root = tk.Tk()
root.title("AES Cryptography")


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor="n" )


second_frame = tk.Frame(root, bg="white")
second_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.05, anchor="n")


encrypt_button = tk.Button(root, text="Encrypt", font=40)
encrypt_button.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.2)

decrypt_button = tk.Button(root, text="Decrypt", font=40)
decrypt_button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.2)

encryptdecrypt_button = tk.Button(root, text="Encrypt/Decrypt", font=40)
encryptdecrypt_button.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.2)

exit_button = tk.Button(root, text="Exit", command = root.destroy)
exit_button.pack()


label = tk.Label(second_frame, font=30, text = "Output")
label.place(relx=0.7, relwidth=0.3, relheight=1)

inputLabel = tk.Label(frame, text="Input", font=30)
inputLabel.place(relx=0.7, relwidth=0.3, relheight=1)

entry = tk.Entry(second_frame, font=30)
entry.place(relwidth=0.7, relheight=1)

entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.7, relheight=1)


root.mainloop()