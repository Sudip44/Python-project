import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename,asksaveasfilename
#function to open file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text.delete("1.0",tk.END)
    status_bar.config(text=f"{filepath}")
    filepath.replace("C:/Users/DELL/Documents/"," ")
    window.title(f"Text Editor by LUCIFER - {filepath}")   
    input_file = open(filepath,'r+')
    text_data = input_file.read()
    text.insert(tk.END, text_data)
    filepath.close()
#function to save file
def save_as_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    status_bar.config(text=f"{filepath}")
    filepath.replace("C:/Users/DELL/Documents/"," ")
    window.title(f"Text Editor by LUCIFER - {filepath}") 
    text_file =open(filepath,"w")
    text_file.write(text.get(1.0,tk.END))
    
#function to create new file
def new_file():
    text.delete("1.0", tk.END)
    window.title("New File------Text Editor by LUCIFER")
    status_bar.config(text="New file       ")
#def save_file():
    

#window and frames
window = tk.Tk()
window.title("Text editor by Lucifer")
window.geometry("1200x660")
frame =tk.Frame(window)
text_scroll = tk.Scrollbar(frame)
text_scroll.pack(side=tk.RIGHT,fill=tk.Y)

text = tk.Text(master=frame,width=970,height=250,selectbackground="yellow",
               selectforeground="black",yscrollcommand= text_scroll.set,undo=True,font=('Ariel',16))
text_scroll.config(command=text.yview)
my_menu = tk.Menu(window)
window.config(menu=my_menu)
#add file menu
file_menu=tk.Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",)
file_menu.add_command(label="Save AS.....",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Close",command=window.destroy)
#add edit menu
edit_menu=tk.Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
#add status bar
status_bar=tk.Label(window,text="Ready     ",anchor=tk.E)
status_bar.pack(fill=tk.X,side=tk.BOTTOM)

frame.pack(fill=tk.BOTH,ipadx=5,ipady=5)
text.pack()
window.mainloop()

