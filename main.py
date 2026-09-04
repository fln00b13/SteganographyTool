import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os


class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.cover_path = tk.StringVar()
        self.secret_path = tk.StringVar()
        self.output_path = tk.StringVar(value="stego.png")
        self.stego_path = tk.StringVar()

        self.create_interface()

    def create_interface(self):
        title = ttk.Label(
            self.root,
            text="Steganography Tool",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(25, 5))

        subtitle = ttk.Label(
            self.root,
            text="Hide and extract files inside images",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 20))

        # Hide section
        hide_frame = ttk.LabelFrame(
            self.root,
            text="Hide Secret File",
            padding=20
        )
        hide_frame.pack(fill="x", padx=30)

        # Cover image
        ttk.Label(hide_frame, text="Cover Image:").grid(
            row=0, column=0, sticky="w", pady=8
        )

        ttk.Entry(
            hide_frame,
            textvariable=self.cover_path,
            width=55
        ).grid(row=0, column=1, padx=10)

        ttk.Button(
            hide_frame,
            text="Browse",
            command=self.select_cover
        ).grid(row=0, column=2)

        # Secret file
        ttk.Label(hide_frame, text="Secret File:").grid(
            row=1, column=0, sticky="w", pady=8
        )

        ttk.Entry(
            hide_frame,
            textvariable=self.secret_path,
            width=55
        ).grid(row=1, column=1, padx=10)

        ttk.Button(
            hide_frame,
            text="Browse",
            command=self.select_secret
        ).grid(row=1, column=2)

        # Output
        ttk.Label(hide_frame, text="Output File:").grid(
            row=2, column=0, sticky="w", pady=8
        )

        ttk.Entry(
            hide_frame,
            textvariable=self.output_path,
            width=55
        ).grid(row=2, column=1, padx=10)

        ttk.Button(
            hide_frame,
            text="Save As",
            command=self.select_output
        ).grid(row=2, column=2)

        ttk.Button(
            hide_frame,
            text="HIDE FILE",
            command=self.hide_file
        ).grid(row=3, column=1, pady=20)

        # Extraction section
        extract_frame = ttk.LabelFrame(
            self.root,
            text="Extract Secret File",
            padding=20
        )
        extract_frame.pack(fill="x", padx=30, pady=20)

        ttk.Label(extract_frame, text="Stego Image:").grid(
            row=0, column=0, sticky="w", pady=8
        )

        ttk.Entry(
            extract_frame,
            textvariable=self.stego_path,
            width=55
        ).grid(row=0, column=1, padx=10)

        ttk.Button(
            extract_frame,
            text="Browse",
            command=self.select_stego
        ).grid(row=0, column=2)

        ttk.Button(
            extract_frame,
            text="EXTRACT FILE",
            command=self.extract_file
        ).grid(row=1, column=1, pady=20)

        # Status
        self.status = ttk.Label(
            self.root,
            text="Status: Ready",
            relief="sunken",
            anchor="w"
        )
        self.status.pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=10
        )

    def select_cover(self):
        path = filedialog.askopenfilename(
            title="Select Cover Image",
            filetypes=[
                ("PNG Images", "*.png"),
                ("JPEG Images", "*.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )

        if path:
            self.cover_path.set(path)

    def select_secret(self):
        path = filedialog.askopenfilename(
            title="Select Secret File",
            filetypes=[
                ("Supported Files", "*.txt *.pdf *.doc *.png *.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )

        if path:
            self.secret_path.set(path)

    def select_output(self):
        path = filedialog.asksaveasfilename(
            title="Save Stego Image",
            defaultextension=".png",
            filetypes=[
                ("PNG Images", "*.png")
            ]
        )

        if path:
            self.output_path.set(path)

    def select_stego(self):
        path = filedialog.askopenfilename(
            title="Select Stego Image",
            filetypes=[
                ("PNG Images", "*.png"),
                ("All Files", "*.*")
            ]
        )

        if path:
            self.stego_path.set(path)

    def hide_file(self):
        messagebox.showinfo(
            "Not Implemented",
            "The hiding algorithm will be added next."
        )

    def extract_file(self):
        messagebox.showinfo(
            "Not Implemented",
            "The extraction algorithm will be added next."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()