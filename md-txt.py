import os
import sys
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

# Initialize Rich console for sleek UI
console = Console()

# Language dictionaries
messages = {
    "en": {
        "title": "GitHub Wiki to TXT Converter",
        "installing_libs": "Installing required libraries...",
        "libs_installed": "Libraries installed successfully!",
        "lib_already_installed": "Library already installed.",
        "created_input_folder": "Created input folder: {}",
        "created_output_folder": "Created output folder: {}",
        "restart_prompt": "Libraries and/or folders were created. Please restart the script.",
        "press_enter": "Press Enter to exit...",
        "no_md_files": "No Markdown (.md) files found in the input folder or its subfolders!",
        "found_md_files": "Found {} Markdown files in the input folder and its subfolders.",
        "content_concatenated": "All wiki content has been concatenated into {}",
        "choose_language": "Choose language / Выберите язык:\n1. English\n2. Русский",
        "invalid_choice": "Invalid choice. Please select 1 or 2.",
    },
    "ru": {
        "title": "Конвертер GitHub Wiki в TXT",
        "installing_libs": "Установка необходимых библиотек...",
        "libs_installed": "Библиотеки успешно установлены!",
        "lib_already_installed": "Библиотека уже установлена.",
        "created_input_folder": "Создана папка для входных данных: {}",
        "created_output_folder": "Создана папка для выходных данных: {}",
        "restart_prompt": "Библиотеки и/или папки были созданы. Пожалуйста, перезапустите скрипт.",
        "press_enter": "Нажмите Enter для выхода...",
        "no_md_files": "В папке входных данных или её подпапках не найдено Markdown (.md) файлов!",
        "found_md_files": "Найдено {} Markdown файлов в папке входных данных и её подпапках.",
        "content_concatenated": "Весь контент вики был объединён в файл {}",
        "choose_language": "Выберите язык / Choose language:\n1. English\n2. Русский",
        "invalid_choice": "Неверный выбор. Пожалуйста, выберите 1 или 2.",
    }
}

# Global variable to store the selected language
selected_language = "en"

def install_required_libraries():
    """Automatically install required libraries if they are not already installed."""
    try:
        import rich
        # Only show "Library already installed" during setup phase
        if not os.path.exists("input") or not os.path.exists("output"):
            console.print(f"[bold green]{messages['en']['lib_already_installed']}[/bold green]")
            console.print(f"[bold green]{messages['ru']['lib_already_installed']}[/bold green]")
        return False  # Indicate that no installation was needed
    except ImportError:
        console.print(f"[bold yellow]{messages['en']['installing_libs']}[/bold yellow]")
        console.print(f"[bold yellow]{messages['ru']['installing_libs']}[/bold yellow]")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
        console.print(f"[bold green]{messages['en']['libs_installed']}[/bold green]")
        console.print(f"[bold green]{messages['ru']['libs_installed']}[/bold green]")
        return True  # Indicate that libraries were installed

def setup_folders():
    """Check for 'input' and 'output' folders in the script's directory, and create them if they don't exist."""
    script_dir = Path(__file__).parent  # Get the directory where the script is located
    input_folder = script_dir / "input"
    output_folder = script_dir / "output"

    folders_created = False

    # Create input folder if it doesn't exist
    if not input_folder.exists():
        input_folder.mkdir()
        console.print(f"[bold green]{messages['en']['created_input_folder'].format(input_folder)}[/bold green]")
        console.print(f"[bold green]{messages['ru']['created_input_folder'].format(input_folder)}[/bold green]")
        folders_created = True

    # Create output folder if it doesn't exist
    if not output_folder.exists():
        output_folder.mkdir()
        console.print(f"[bold green]{messages['en']['created_output_folder'].format(output_folder)}[/bold green]")
        console.print(f"[bold green]{messages['ru']['created_output_folder'].format(output_folder)}[/bold green]")
        folders_created = True

    return folders_created  # Indicate whether folders were created

def find_md_files(input_folder):
    """Recursively find all .md files in the input folder and its subfolders."""
    md_files = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def concatenate_wiki_to_txt(input_folder, output_folder):
    """Concatenate all Markdown files in the input folder and its subfolders into a single text file."""
    # Define the output file path
    output_file_path = output_folder / 'wiki_content.txt'

    # Find all .md files in the input folder and its subfolders
    md_files = find_md_files(input_folder)
    if not md_files:
        console.print(f"[bold red]{messages[selected_language]['no_md_files']}[/bold red]")
        return

    console.print(f"[bold green]{messages[selected_language]['found_md_files'].format(len(md_files))}[/bold green]")

    # Open the output file in write mode
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in md_files:
            with open(file_path, 'r', encoding='utf-8') as md_file:
                # Write the content of the Markdown file to the output file
                relative_path = os.path.relpath(file_path, input_folder)
                output_file.write(f"=== {relative_path} ===\n")
                output_file.write(md_file.read())
                output_file.write("\n\n")

    console.print(f"[bold green]{messages[selected_language]['content_concatenated'].format(output_file_path)}[/bold green]")

def choose_language():
    """Ask the user to choose a language."""
    global selected_language
    console.print(Panel.fit(messages["en"]["choose_language"], border_style="blue"))
    choice = input("> ")
    if choice == "1":
        selected_language = "en"
    elif choice == "2":
        selected_language = "ru"
    else:
        console.print(f"[bold red]{messages['en']['invalid_choice']}[/bold red]")
        choose_language()

def main():
    """Main function to run the script."""
    # Display a sleek header in English (default)
    console.print(Panel.fit(messages["en"]["title"], border_style="blue"))

    # Install required libraries
    libraries_installed = install_required_libraries()

    # Set up input and output folders
    folders_created = setup_folders()

    # If libraries were installed or folders were created, prompt the user to restart the script
    if libraries_installed or folders_created:
        console.print(f"[bold yellow]{messages['en']['restart_prompt']}[/bold yellow]")
        console.print(f"[bold yellow]{messages['ru']['restart_prompt']}[/bold yellow]")
        console.print(f"\n[bold yellow]{messages['en']['press_enter']}[/bold yellow]")
        console.print(f"[bold yellow]{messages['ru']['press_enter']}[/bold yellow]")
        input()
        return  # Exit the script

    # Ask the user to choose a language
    choose_language()

    # Get input and output folders
    script_dir = Path(__file__).parent
    input_folder = script_dir / "input"
    output_folder = script_dir / "output"

    # Call the function to concatenate the wiki
    concatenate_wiki_to_txt(input_folder, output_folder)

    # Pause before exiting (for double-click execution)
    console.print(f"\n[bold yellow]{messages[selected_language]['press_enter']}[/bold yellow]")
    input()

if __name__ == "__main__":
    main()