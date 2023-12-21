import tkinter as tk 
import tkinter.ttk as ttk 

# CALL UP WINDOW 
root = tk.Tk() # window 
root.title('NHL Graphs Widget')
# root.resizable(False, False) # tkinter window can't be resized
root.attributes("-topmost", True) # tkinter window stays on top 

message = tk.Label(root, text = "Hello!")
message.pack()

# root.protocol("WM_DELETE_WINDOW", main_window.on_closing) # exit the program when X button clicked 
root.mainloop()