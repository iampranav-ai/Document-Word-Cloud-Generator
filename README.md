# Document Word Cloud Generator

This Streamlit application generates a word cloud and displays the most common words from various document types, including but not limited to resumes, source code files, configuration files, and more. It provides a visual representation of the most frequently used words in your document, helping you quickly identify key terms and assess the overall focus of your content.

## Features

- Supports a wide range of file formats, including:
  - Document files: PDF, DOCX, TXT
  - Source code files: C, CPP, CS, JAVA, PY, JS, HTML, CSS, PHP, RB, PL, SH, SWIFT, GO, RS, LUA
  - Configuration and data files: JSON, XML, YAML, YML, INI, CONF, CFG, ENV
  - Markdown and documentation: MD, RST
  - Log files: LOG
  - Structured data: CSV, TSV, SQL
  - Scripts: BAT, PS1
  - And more: RTF, TEX, TPL, XSLT, ASCIIDOC, VBS
- Generates a visually appealing word cloud
- Displays a table of the 20 most common words with their frequencies
- Easy-to-use web interface powered by Streamlit
- Automatic encoding detection for text-based files

## Screenshots

### Word Cloud Example
![image](https://github.com/user-attachments/assets/09b2659a-ba67-4307-8b84-dc0e7dc6b096)

### Most Common Words Table

![image](https://github.com/user-attachments/assets/480f76b7-a33f-437f-a33a-6440812584f5)


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/iampranav-ai/Document-Word-Cloud-Generator.git
   ```

2. Install the required dependencies:
- Python 3.7+
- Streamlit
- Matplotlib
- WordCloud
- PyPDF2
- python-docx
- chardet
## Usage

1. Run the Streamlit app:
   ```
   streamlit run wordCloudGeneratorStreamlit.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload your document file using the file uploader. The app supports a wide range of file formats.

4. The app will generate and display the word cloud and the table of most common words.


## How It Works

1. The app reads the uploaded file based on its extension.
2. For PDF and DOCX files, it uses specialized libraries (PyPDF2 and python-docx) to extract text.
3. For other text-based files, it uses the `chardet` library to detect the file encoding and read the content accordingly.
4. The text is preprocessed by removing special characters, converting to lowercase, and filtering out short words.
5. A word cloud is generated using the processed text.
6. The frequency of words is counted, and the top 20 most common words are displayed in a table.

## Limitations

- Binary files or files with non-textual content may not produce meaningful results.
- The quality of the word cloud depends on the content and format of the input file.
- Very large files may take longer to process.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [WordCloud](https://github.com/amueller/word_cloud) for the word cloud generation
- [PyPDF2](https://github.com/mstamy2/PyPDF2) for PDF file handling
- [python-docx](https://github.com/python-openxml/python-docx) for DOCX file handling
- [chardet](https://github.com/chardet/chardet) for character encoding detection

## Author

Pranav Verma

## Project Status

This project is currently in development. Future updates may include additional text processing features, improved visualization options, and support for more file formats.
