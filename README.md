# GitHub Wiki to TXT Converter

A simple Python script that helps you convert all Markdown files from a GitHub wiki (or any folder containing `.md` files) into a single `.txt` file. The script recursively finds all Markdown files from the specified input folder and its subfolders, and concatenates them into one neat text file.

## Features

- **Multilingual Support**: Choose between English and Russian to interact with the script.
- **Rich UI**: Uses the `rich` library to display a sleek and beautiful terminal interface.
- **Automatic Setup**: Automatically installs required libraries if not already installed.
- **Folder Management**: Automatically creates input and output folders if they don't exist.
- **Recursive File Search**: Searches all subdirectories for `.md` files and concatenates their content into a single text file.
- **Content Concatenation**: The script adds each Markdown file's content, with clear file separation, into a single `.txt` file.
- **Customizable Input/Output Folders**: Easily manage input and output file locations in the script’s directory.

## How to Use

1. **Run the script**: Simply run the Python script, and it will handle everything for you.
2. **Select Language**: Upon first execution, you will be prompted to choose between English and Russian.
3. **Prepare Your Files**: Place all your `.md` files into the `input` folder (or its subfolders).
4. **Run the Script**: After setup, the script will automatically search the input folder for all `.md` files, then concatenate them into a single file named `wiki_content.txt` inside the `output` folder.
5. **Find Your Output**: The concatenated text file will be located in the `output` folder, ready for you to use!

## License

MIT License - See the LICENSE file for details.
