import tkinter as tk 
from tkinter import filedialog
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image
import os

root=tk.Tk()
root.minsize=(200,200)
root.maxsize=(800,800)
root.geometry=("700x700+50+50")
root.configure(background="grey")

def submit():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files","*.pdf"),("all files","*,+")]
    )
    if file_path:
        print("selected file:",file_path)
        output_path = os.path.splitext(file_path)[0] + ".docx"
        change=Converter(file_path)
        change.convert(output_path, start=0, end=None)
        change.close()
        print("conversion done", output_path)
        done_popup =tk.Label(root, text="converted into pdf sucessfully✅", bg="grey",fg="green",font=("calibre",20,"bold"))
        done_popup.grid(row=3, column=4,columnspan=4,pady=20)
        
def word2pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Word files","*.docx"),("all files","*,+")]
    )
    if file_path:
        print("selected file:",file_path)
        output_path = os.path.splitext(file_path)[0] + ".pdf"
        convert(file_path)
        #change.convert(output_path, start=0, end=None)
        #change.close()
        print("conversion done", output_path)
        done_popup =tk.Label(root, text="converted into pdf sucessfully✅", bg="grey",fg="green",font=("calibre",20,"bold"))
        done_popup.grid(row=3, column=4,columnspan=4,pady=20)
def imgtopdf():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")])
        if file_path:
             print("Selected image:", file_path)
        output_path = os.path.splitext(file_path)[0] + ".pdf"
        Img = Image.open(file_path)
        if Img.mode in("RGBA", "P"):
            Img= Img.convert("RGB")
        Img.save(output_path)
        print("converted into pdf", output_path)
        done_popup = tk.Label(root, text="Image converted to PDF ✅", bg="grey", fg="green", font=("calibre", 20, "bold"))
        done_popup.grid(row=4, column=1, columnspan=3, pady=20)
        
        
browse_label = tk.Label(root, text="FILE CONVERTER",font=("arail",45,"bold",),bg="grey",fg="lightblue")
h2 = tk.Label(root,text="Easily convert files from one format to another, online", font=("comic sans ms",24,"italic"), bg="grey", fg="white")
footer=tk.Label(root, text="project by khushal garg bca 5th 23ca1026", font=("forte",35,"bold"), fg="yellow", bg="grey")
browse_button = tk.Button(root, text="Pdf to Word Convertor", command=submit, font=("calibre",25,"bold"),bg="lightblue",fg="white")
browse_button1 = tk.Button(root, text="Word to Pdf Convertor", command=word2pdf, font=("calibre",25,"bold"),bg="lightblue",fg="white")
browse_button2 = tk.Button(root, text="img to pdf converter", command= imgtopdf, font=("calibre",25,"bold"),bg="lightblue",fg="white")
browse_label.grid(row=0, column=0, columnspan=3, pady=20)
h2.grid(row=1,column=0, columnspan=5,pady=20)
browse_button.grid(row=2, column=1, padx=20, pady=40)
browse_button1.grid(row=2, column=2, padx=20, pady=40)
browse_button2.grid(row=3, column=1, padx=50, pady=50)
footer.grid(row=5,column=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3,weight=1)

root.mainloop()



