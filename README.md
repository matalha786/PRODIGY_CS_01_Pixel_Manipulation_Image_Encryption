
# Pixel Manipulation Tool

This tool allows you to encrypt and decrypt images by shuffling and swapping their pixels based on a user-provided key. It provides a graphical user interface (GUI) to load, encrypt, decrypt, and save images.

## Features

- **Load Image**: Load an image from your file system.
- **Encrypt Image**: Encrypt the loaded image using a key.
- **Decrypt Image**: Decrypt the encrypted image using the same key used for encryption.
- **Save Image**: Save the encrypted or decrypted image to your file system.
- **Exit Program**: Close the application.

## Installation

To run this tool, you need to have Python installed on your system along with the required libraries. You can install the necessary libraries using the following command:

```bash
pip install tkinter pillow numpy
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/pixel-manipulation-tool.git
cd pixel-manipulation-tool
```

2. Run the script:

```bash
python pixel_manipulation_tool.py
```

3. Use the GUI to load an image, enter a key, and click the buttons to encrypt, decrypt, or save the image.

## How It Works

- **Loading an Image**: The tool allows you to load an image from your file system. The loaded image is displayed in the GUI.
- **Encrypting an Image**: When you provide a key and click the "Encrypt Image" button, the tool shuffles the pixels of the image based on the key and displays the encrypted image.
- **Decrypting an Image**: When you provide the same key used for encryption and click the "Decrypt Image" button, the tool reverses the shuffling of the pixels and displays the decrypted image.
- **Saving an Image**: You can save the encrypted or decrypted image to your file system by clicking the "Save Image" button.

## Code Overview

Here's a brief overview of the code:

- **load_image**: Loads an image from the file system and displays it in the GUI.
- **save_image**: Saves the provided image array to the file system.
- **shuffle_pixels**: Shuffles the pixels of the image based on the provided key.
- **swap_pixels**: Swaps the pixels of the image based on the shuffled indices.
- **reverse_swap_pixels**: Reverses the swapping of pixels to decrypt the image.
- **encrypt_image**: Encrypts the loaded image using the provided key.
- **decrypt_image**: Decrypts the encrypted image using the provided key.
- **exit_program**: Closes the application.



## License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for details.

## Author

Muhammad Ahmed Talha 


## Acknowledgements

This project uses the following libraries:
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.
- [NumPy](https://numpy.org/) for numerical operations.

```
