import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import os
import struct


class SteganographyApp:

    MAGIC = b"STEG"
    HEADER_FORMAT = ">4sIQ"
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

    def __init__(self, root):
        self.root = root

        self.root.title("Steganography Tool")
        self.root.geometry("750x600")
        self.root.resizable(False, False)

        self.cover_path = tk.StringVar()
        self.secret_path = tk.StringVar()
        self.output_path = tk.StringVar(value="stego.png")
        self.stego_path = tk.StringVar()

        self.create_interface()

    # =========================================================
    # GUI
    # =========================================================

    def create_interface(self):

        title = ttk.Label(
            self.root,
            text="Steganography Tool",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(25, 5))

        subtitle = ttk.Label(
            self.root,
            text="Hide and extract secret files inside images",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 20))

        # -----------------------------------------------------
        # HIDE SECTION
        # -----------------------------------------------------

        hide_frame = ttk.LabelFrame(
            self.root,
            text="Hide Secret File",
            padding=20
        )

        hide_frame.pack(
            fill="x",
            padx=30
        )

        # Cover Image

        ttk.Label(
            hide_frame,
            text="Cover Image:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8
        )

        ttk.Entry(
            hide_frame,
            textvariable=self.cover_path,
            width=58
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        ttk.Button(
            hide_frame,
            text="Browse",
            command=self.select_cover
        ).grid(
            row=0,
            column=2
        )

        # Secret File

        ttk.Label(
            hide_frame,
            text="Secret File:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=8
        )

        ttk.Entry(
            hide_frame,
            textvariable=self.secret_path,
            width=58
        ).grid(
            row=1,
            column=1,
            padx=10
        )

        ttk.Button(
            hide_frame,
            text="Browse",
            command=self.select_secret
        ).grid(
            row=1,
            column=2
        )

        # Output

        ttk.Label(
            hide_frame,
            text="Output File:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        ttk.Entry(
            hide_frame,
            textvariable=self.output_path,
            width=58
        ).grid(
            row=2,
            column=1,
            padx=10
        )

        ttk.Button(
            hide_frame,
            text="Save As",
            command=self.select_output
        ).grid(
            row=2,
            column=2
        )

        # Hide button

        ttk.Button(
            hide_frame,
            text="HIDE FILE",
            command=self.hide_file
        ).grid(
            row=3,
            column=1,
            pady=20
        )

        # -----------------------------------------------------
        # EXTRACTION SECTION
        # -----------------------------------------------------

        extract_frame = ttk.LabelFrame(
            self.root,
            text="Extract Secret File",
            padding=20
        )

        extract_frame.pack(
            fill="x",
            padx=30,
            pady=20
        )

        ttk.Label(
            extract_frame,
            text="Stego Image:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8
        )

        ttk.Entry(
            extract_frame,
            textvariable=self.stego_path,
            width=58
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        ttk.Button(
            extract_frame,
            text="Browse",
            command=self.select_stego
        ).grid(
            row=0,
            column=2
        )

        ttk.Button(
            extract_frame,
            text="EXTRACT FILE",
            command=self.extract_file
        ).grid(
            row=1,
            column=1,
            pady=20
        )

        # -----------------------------------------------------
        # INFORMATION
        # -----------------------------------------------------

        info_frame = ttk.LabelFrame(
            self.root,
            text="Information",
            padding=10
        )

        info_frame.pack(
            fill="x",
            padx=30
        )

        info_text = (
            "Supported secret files: TXT, PDF, DOC, PNG, JPG, JPEG\n"
            "Stego images are saved as PNG files.\n"
            "The tool uses Least Significant Bit (LSB) steganography."
        )

        ttk.Label(
            info_frame,
            text=info_text,
            justify="left"
        ).pack(anchor="w")

        # -----------------------------------------------------
        # STATUS
        # -----------------------------------------------------

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

    # =========================================================
    # FILE SELECTION
    # =========================================================

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
            self.status.config(
                text=f"Cover image selected: {os.path.basename(path)}"
            )

    def select_secret(self):

        path = filedialog.askopenfilename(
            title="Select Secret File",
            filetypes=[
                (
                    "Supported Files",
                    "*.txt *.pdf *.doc *.png *.jpg *.jpeg"
                ),
                ("Text Files", "*.txt"),
                ("PDF Files", "*.pdf"),
                ("Word Documents", "*.doc"),
                ("PNG Images", "*.png"),
                ("JPEG Images", "*.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )

        if path:
            self.secret_path.set(path)
            self.status.config(
                text=f"Secret file selected: {os.path.basename(path)}"
            )

    def select_output(self):

        path = filedialog.asksaveasfilename(
            title="Save Stego Image",
            defaultextension=".png",
            filetypes=[
                ("PNG Images", "*.png")
            ]
        )

        if path:

            if not path.lower().endswith(".png"):
                path += ".png"

            self.output_path.set(path)

            self.status.config(
                text=f"Output selected: {os.path.basename(path)}"
            )

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

            self.status.config(
                text=f"Stego image selected: {os.path.basename(path)}"
            )

    # =========================================================
    # HIDE FILE
    # =========================================================

    def hide_file(self):

        cover = self.cover_path.get()
        secret = self.secret_path.get()
        output = self.output_path.get()

        # Check cover image

        if not cover:

            messagebox.showerror(
                "Error",
                "Please select a cover image."
            )

            return

        if not os.path.exists(cover):

            messagebox.showerror(
                "Error",
                "The selected cover image does not exist."
            )

            return

        # Check secret file

        if not secret:

            messagebox.showerror(
                "Error",
                "Please select a secret file."
            )

            return

        if not os.path.exists(secret):

            messagebox.showerror(
                "Error",
                "The selected secret file does not exist."
            )

            return

        # Check output

        if not output:

            messagebox.showerror(
                "Error",
                "Please select an output file."
            )

            return

        try:

            self.status.config(
                text="Status: Reading files..."
            )

            self.root.update()

            # -------------------------------------------------
            # Load cover image
            # -------------------------------------------------

            image = Image.open(cover)

            # Convert to RGB

            image = image.convert("RGB")

            width, height = image.size

            # -------------------------------------------------
            # Read secret file
            # -------------------------------------------------

            with open(secret, "rb") as file:

                secret_data = file.read()

            filename = os.path.basename(secret)

            filename_bytes = filename.encode("utf-8")

            filename_length = len(filename_bytes)

            secret_size = len(secret_data)

            # -------------------------------------------------
            # Create header
            #
            # MAGIC
            # filename length
            # secret file size
            # -------------------------------------------------

            header = struct.pack(
                self.HEADER_FORMAT,
                self.MAGIC,
                filename_length,
                secret_size
            )

            # Complete payload

            payload = (
                header
                + filename_bytes
                + secret_data
            )

            # -------------------------------------------------
            # Convert bytes to bits
            # -------------------------------------------------

            bits = []

            for byte in payload:

                for bit in range(7, -1, -1):

                    bits.append(
                        (byte >> bit) & 1
                    )

            # -------------------------------------------------
            # Calculate capacity
            # -------------------------------------------------

            capacity_bits = width * height * 3

            required_bits = len(bits)

            if required_bits > capacity_bits:

                capacity_bytes = capacity_bits // 8

                messagebox.showerror(
                    "File Too Large",
                    f"The secret file is too large for this image.\n\n"
                    f"Available capacity: approximately "
                    f"{capacity_bytes:,} bytes\n"
                    f"Required: {len(payload):,} bytes"
                )

                return

            # -------------------------------------------------
            # Embed bits
            # -------------------------------------------------

            pixels = list(image.getdata())

            new_pixels = []

            bit_index = 0

            for pixel in pixels:

                r, g, b = pixel

                channels = [r, g, b]

                for channel_index in range(3):

                    if bit_index < len(bits):

                        # Clear LSB

                        channels[channel_index] &= 0xFE

                        # Insert secret bit

                        channels[channel_index] |= bits[bit_index]

                        bit_index += 1

                new_pixels.append(
                    tuple(channels)
                )

            # -------------------------------------------------
            # Create stego image
            # -------------------------------------------------

            stego_image = Image.new(
                "RGB",
                image.size
            )

            stego_image.putdata(
                new_pixels
            )

            # -------------------------------------------------
            # Save as PNG
            # -------------------------------------------------

            stego_image.save(
                output,
                "PNG"
            )

            # -------------------------------------------------
            # Calculate file sizes
            # -------------------------------------------------

            cover_size = os.path.getsize(cover)

            stego_size = os.path.getsize(output)

            difference = stego_size - cover_size

            # -------------------------------------------------
            # Update status
            # -------------------------------------------------

            self.status.config(
                text=f"Status: Successfully created {output}"
            )

            messagebox.showinfo(
                "Success",
                "Secret file successfully hidden!\n\n"
                f"Secret file:\n{filename}\n\n"
                f"Stego image:\n{output}\n\n"
                f"Cover size: {self.format_size(cover_size)}\n"
                f"Stego size: {self.format_size(stego_size)}\n"
                f"Difference: {self.format_size(difference, signed=True)}"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Failed to hide the file:\n\n{error}"
            )

            self.status.config(
                text="Status: Failed to hide file"
            )

    # =========================================================
    # EXTRACT FILE
    # =========================================================

    def extract_file(self):

        stego = self.stego_path.get()

        if not stego:

            messagebox.showerror(
                "Error",
                "Please select a stego image."
            )

            return

        if not os.path.exists(stego):

            messagebox.showerror(
                "Error",
                "The selected stego image does not exist."
            )

            return

        try:

            self.status.config(
                text="Status: Reading stego image..."
            )

            self.root.update()

            # -------------------------------------------------
            # Open image
            # -------------------------------------------------

            image = Image.open(stego).convert("RGB")

            pixels = list(image.getdata())

            # -------------------------------------------------
            # Extract all LSBs
            # -------------------------------------------------

            bits = []

            for pixel in pixels:

                r, g, b = pixel

                bits.append(r & 1)
                bits.append(g & 1)
                bits.append(b & 1)

            # -------------------------------------------------
            # Convert first header bytes
            # -------------------------------------------------

            header_bits = bits[
                :self.HEADER_SIZE * 8
            ]

            header = self.bits_to_bytes(
                header_bits
            )

            # -------------------------------------------------
            # Check header
            # -------------------------------------------------

            magic, filename_length, secret_size = struct.unpack(
                self.HEADER_FORMAT,
                header
            )

            if magic != self.MAGIC:

                messagebox.showerror(
                    "Error",
                    "This image does not contain a valid hidden file."
                )

                return

            # -------------------------------------------------
            # Calculate positions
            # -------------------------------------------------

            filename_start = self.HEADER_SIZE * 8

            filename_end = (
                filename_start
                + filename_length * 8
            )

            data_start = filename_end

            data_end = (
                data_start
                + secret_size * 8
            )

            # Check enough data exists

            if data_end > len(bits):

                messagebox.showerror(
                    "Error",
                    "The stego image appears to be corrupted."
                )

                return

            # -------------------------------------------------
            # Extract filename
            # -------------------------------------------------

            filename_bits = bits[
                filename_start:filename_end
            ]

            filename_bytes = self.bits_to_bytes(
                filename_bits
            )

            filename = filename_bytes.decode(
                "utf-8"
            )

            # -------------------------------------------------
            # Extract secret file
            # -------------------------------------------------

            data_bits = bits[
                data_start:data_end
            ]

            secret_data = self.bits_to_bytes(
                data_bits
            )

            # -------------------------------------------------
            # Ask user where to save
            # -------------------------------------------------

            output_path = filedialog.asksaveasfilename(
                title="Save Extracted File",
                initialfile=filename
            )

            if not output_path:

                self.status.config(
                    text="Status: Extraction cancelled"
                )

                return

            # -------------------------------------------------
            # Write recovered file
            # -------------------------------------------------

            with open(output_path, "wb") as file:

                file.write(secret_data)

            # -------------------------------------------------
            # Update status
            # -------------------------------------------------

            self.status.config(
                text=f"Status: Successfully extracted {filename}"
            )

            messagebox.showinfo(
                "Success",
                "Secret file successfully extracted!\n\n"
                f"Original filename:\n{filename}\n\n"
                f"Saved to:\n{output_path}\n\n"
                f"File size:\n{self.format_size(len(secret_data))}"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Failed to extract the file:\n\n{error}"
            )

            self.status.config(
                text="Status: Failed to extract file"
            )

    # =========================================================
    # BITS → BYTES
    # =========================================================

    @staticmethod
    def bits_to_bytes(bits):

        output = bytearray()

        for i in range(
            0,
            len(bits),
            8
        ):

            byte_bits = bits[i:i + 8]

            if len(byte_bits) < 8:
                break

            value = 0

            for bit in byte_bits:

                value = (
                    value << 1
                ) | bit

            output.append(value)

        return bytes(output)

    # =========================================================
    # FILE SIZE FORMATTER
    # =========================================================

    @staticmethod
    def format_size(size, signed=False):

        sign = ""

        if signed:

            if size > 0:
                sign = "+"

            elif size < 0:
                sign = "-"

            size = abs(size)

        units = [
            "B",
            "KB",
            "MB",
            "GB"
        ]

        value = float(size)

        for unit in units:

            if value < 1024:

                return f"{sign}{value:.2f} {unit}"

            value /= 1024

        return f"{sign}{value:.2f} TB"


# =============================================================
# PROGRAM START
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SteganographyApp(root)

    root.mainloop()