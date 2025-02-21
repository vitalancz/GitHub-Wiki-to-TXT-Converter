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


# GitHub Wiki в TXT Конвертер

Это простой Python скрипт, который помогает вам конвертировать все Markdown файлы из GitHub wiki (или любой папки, содержащей `.md` файлы) в один `.txt` файл. Скрипт рекурсивно находит все Markdown файлы в указанной папке и ее подпапках, а затем объединяет их в один аккуратный текстовый файл.

## Особенности

- **Многоязычная поддержка**: Вы можете выбрать между английским и русским языками для взаимодействия с скриптом.
- **Красивый интерфейс**: Использует библиотеку `rich` для отображения стильного и красивого интерфейса в терминале.
- **Автоматическая установка**: Если необходимые библиотеки еще не установлены, скрипт автоматически их установит.
- **Управление папками**: Скрипт автоматически создает папки для входных и выходных данных, если они не существуют.
- **Рекурсивный поиск файлов**: Скрипт рекурсивно ищет все `.md` файлы в папке и ее подпапках и объединяет их в один текстовый файл.
- **Объединение содержимого**: Скрипт добавляет содержимое каждого Markdown файла в один `.txt` файл с четким разделением между файлами.
- **Настройка папок ввода/вывода**: Легко управляйте папками для входных и выходных файлов в каталоге скрипта.

## Как использовать

1. **Запустите скрипт**: Просто запустите Python скрипт, и он сам все сделает.
2. **Выбор языка**: При первом запуске скрипт предложит выбрать между английским и русским языком.
3. **Подготовьте файлы**: Поместите все `.md` файлы в папку `input` (или в ее подпапки).
4. **Запустите скрипт**: После настройки скрипт автоматически найдет все `.md` файлы в папке `input`, объединит их в один файл под названием `wiki_content.txt` в папке `output`.
5. **Найдите вывод**: Объединенный текстовый файл будет находиться в папке `output` и готов к использованию!

## Лицензия

MIT Лицензия - см. файл LICENSE для подробностей.


# GitHub Wiki 轉換器 (TXT)

這是一個簡單的 Python 腳本，可以將所有來自 GitHub Wiki（或任何包含 `.md` 檔案的資料夾）中的 Markdown 檔案轉換為單一的 `.txt` 檔案。此腳本會遞迴搜尋指定的輸入資料夾及其子資料夾中的所有 Markdown 檔案，並將它們合併成一個乾淨的文字檔。

## 功能

- **多語言支援**：選擇英語或俄語來與腳本互動。
- **優雅的界面**：使用 `rich` 庫來顯示流暢且美觀的終端界面。
- **自動安裝**：如果所需的庫尚未安裝，腳本會自動安裝。
- **資料夾管理**：自動創建輸入和輸出資料夾（如果它們不存在的話）。
- **遞迴檔案搜尋**：遞迴搜尋所有子資料夾中的 `.md` 檔案，並將它們的內容合併成單一的文字檔案。
- **內容合併**：腳本會將每個 Markdown 檔案的內容與清晰的檔案分隔符添加到單一的 `.txt` 檔案中。
- **可自訂的輸入/輸出資料夾**：輕鬆管理腳本所在目錄中的輸入和輸出檔案位置。

## 如何使用

1. **執行腳本**：只需執行 Python 腳本，它將自動處理所有操作。
2. **選擇語言**：首次執行時，腳本會提示你選擇英語或俄語。
3. **準備檔案**：將所有 `.md` 檔案放入 `input` 資料夾（或其子資料夾中）。
4. **執行腳本**：設置完成後，腳本會自動搜尋 `input` 資料夾中的所有 `.md` 檔案，並將它們合併成名為 `wiki_content.txt` 的檔案，並保存在 `output` 資料夾中。
5. **查找輸出**：合併後的文字檔會保存在 `output` 資料夾中，隨時可以使用！

## 授權

MIT 授權 - 詳情請參見 LICENSE 檔案。
