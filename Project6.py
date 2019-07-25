import tkinter as tk


class MDLabel(tk.Frame):

    def __init__(self, parent=None, **options):
        tk.Frame.__init__(self, parent, bg=options["sc"])  # sc = shadow color
        self.label = tk.Label(self, text=options["text"], padx=15, pady=10)
        self.label.pack(expand=1, fill="both", padx=(0, options["si"]), pady=(0, options["si"]))  # shadow intensity


root = tk.Tk()
root.geometry("600x300+900+200")

main_frame = tk.Frame(root, bg="red")
body_frame = tk.Frame(main_frame)

for i in range(3):
    md_label = MDLabel(body_frame, sc="blue

    	", si=1, text="Label " + str(i))
    md_label.pack(expand=1, fill="both", pady=5)

body_frame.pack(expand=1, fill="both", pady=5, padx=5)
main_frame.pack(expand=True, fill="both")

root.mainloop()