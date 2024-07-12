import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def load_image():
    global img, img_array, encrypted_array, indices
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 400))
        img_array = np.array(img)
        encrypted_array = img_array.copy()  # Treat the loaded image as potentially encrypted
        img_tk = ImageTk.PhotoImage(img)
        label_img.configure(image=img_tk)
        label_img.image = img_tk
        indices = None  # Reset indices when a new image is loaded

def save_image(image_array):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        image = Image.fromarray(image_array)
        image.save(save_path)
        messagebox.showinfo("Save Image", "Image saved successfully!")

def shuffle_pixels(arr, key):
    np.random.seed(key)
    indices = np.arange(arr.size)
    np.random.shuffle(indices)
    return indices

def swap_pixels(arr, indices):
    flat_arr = arr.flatten()
    shuffled_arr = flat_arr[indices]
    return shuffled_arr.reshape(arr.shape)

def reverse_swap_pixels(arr, indices):
    flat_arr = arr.flatten()
    reverse_indices = np.argsort(indices)
    unshuffled_arr = flat_arr[reverse_indices]
    return unshuffled_arr.reshape(arr.shape)

def encrypt_image():
    global img_array, encrypted_array, indices
    if img_array is not None:
        try:
            key = int(entry_key.get())
            indices = shuffle_pixels(img_array, key)
            encrypted_array = swap_pixels(img_array, indices)
            encrypted_img = Image.fromarray(encrypted_array)
            encrypted_img_tk = ImageTk.PhotoImage(encrypted_img)
            label_img.configure(image=encrypted_img_tk)
            label_img.image = encrypted_img_tk
        except ValueError:
            messagebox.showerror("Invalid Input", "Key must be an integer")
    else:
        messagebox.showerror("No Image", "Please load an image first!")

def decrypt_image():
    global encrypted_array, img_array, indices
    if encrypted_array is not None:
        try:
            key = int(entry_key.get())
            if indices is None:
                indices = shuffle_pixels(encrypted_array, key)
            decrypted_array = reverse_swap_pixels(encrypted_array, indices)
            decrypted_img = Image.fromarray(decrypted_array)
            decrypted_img_tk = ImageTk.PhotoImage(decrypted_img)
            label_img.configure(image=decrypted_img_tk)
            label_img.image = decrypted_img_tk
        except ValueError:
            messagebox.showerror("Invalid Input", "Key must be an integer")
    elif img_array is not None:
        try:
            key = int(entry_key.get())
            indices = shuffle_pixels(img_array, key)
            decrypted_array = reverse_swap_pixels(img_array, indices)
            decrypted_img = Image.fromarray(decrypted_array)
            decrypted_img_tk = ImageTk.PhotoImage(decrypted_img)
            label_img.configure(image=decrypted_img_tk)
            label_img.image = decrypted_img_tk
        except ValueError:
            messagebox.showerror("Invalid Input", "Key must be an integer")
    else:
        messagebox.showerror("No Encrypted Image", "Please load an encrypted image first!")

def exit_program():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Initialize global variables
img = None
img_array = None
encrypted_array = None
indices = None

# Configure grid to make the window scalable and resizable
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=10)  # Give more weight to the row with the image

# Create and place the widgets
btn_load = tk.Button(root, text="Load Image", command=load_image)
btn_load.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

label_key = tk.Label(root, text="Enter Key:")
label_key.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_key = tk.Entry(root, width=10)
entry_key.grid(row=1, column=1, padx=10, pady=5, sticky="w")

btn_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_image)
btn_encrypt.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

btn_decrypt = tk.Button(root, text="Decrypt Image", command=decrypt_image)
btn_decrypt.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

btn_save = tk.Button(root, text="Save Image", command=lambda: save_image(encrypted_array))
btn_save.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

btn_exit = tk.Button(root, text="Exit", command=exit_program)
btn_exit.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

label_img = tk.Label(root)
label_img.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

# Run the main loop
root.mainloop()
