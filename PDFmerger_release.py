import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import os

def merge_pdfs(pdf_files, output_path):
    merger = PyPDF2.PdfMerger()
    
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    
    merger.write(output_path)
    merger.close()
    messagebox.showinfo("Success", "PDF files merged successfully!")

def browse_pdf_files():
    pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if pdf_files:
        pdf_files_list.delete(0, tk.END)
        for file in pdf_files:
            filename = os.path.basename(file)
            pdf_files_list.insert(tk.END, filename)

def add_single_pdf_file():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_file:
        filename = os.path.basename(pdf_file)
        pdf_files_list.insert(tk.END, filename)

def merge_files():
    pdf_files = pdf_files_list.get(0, tk.END)
    if len(pdf_files) < 2:
        messagebox.showerror("Error", "Please select at least two PDF files to merge.")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if output_path:
        merge_pdfs(pdf_files, output_path)

# Create the main window
root = tk.Tk()
root.title("PDF Merger")
root.configure(bg="#1E1E1E")

# Apply dark theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Frame for the PDF files list
pdf_files_frame = tk.Frame(root, bg="#1E1E1E")
pdf_files_frame.pack(padx=10, pady=10)

# Label for PDF files list
pdf_files_label = tk.Label(pdf_files_frame, text="PDF Files to Merge:", bg="#1E1E1E", fg="#FFFFFF")
pdf_files_label.pack()

# Listbox to display selected PDF files
pdf_files_list = tk.Listbox(pdf_files_frame, width=50, height=5, selectmode=tk.MULTIPLE, bg="#1E1E1E", fg="#FFFFFF", selectbackground="#3A3A3A")
pdf_files_list.pack()

# Frame for the buttons
buttons_frame = tk.Frame(root, bg="#1E1E1E")
buttons_frame.pack(pady=(0, 10))

# Button to browse and select PDF files
browse_button = ctk.CTkButton(buttons_frame, text="Browse PDF Files", command=browse_pdf_files, corner_radius=20)

browse_button.pack(side=tk.LEFT, padx=(0, 10))

# Button to add a single PDF file
add_single_button = ctk.CTkButton(buttons_frame, text="Add Single PDF File", command=add_single_pdf_file, corner_radius=20)

add_single_button.pack(side=tk.LEFT)

# Button to merge PDF files
merge_button = ctk.CTkButton(root, text="Merge PDF Files", command=merge_files, corner_radius=20)

merge_button.pack()

# Start the GUI
root.mainloop()