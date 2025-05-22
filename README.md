# MutualCheck: Instagram Followers Checker

A tool to compare your Instagram followers and following lists to identify non-mutual connections.

## Building and Running
1. Install Python
    - Go to [python.org](https://www.python.org/) and download the latest version of Python
    - During installation, check **Add python.exe to PATH**, then select **Install Now** to get pip (Python's package installer)
    - After installation. check if Python and pip are installed:
        -   ```bash
            python --version
            ```
        ```bash
        pip --version
        ```

2. Download MutualCheck
    - If your not already on the repository page, go to [GitHub Repository Page](https://github.com/arhamislam/mutual-check)
    - Click the green **Code** button
    - Select **Download ZIP**
    - Extract the ZIP file to a folder on your computer

3. Setting up your Instagram credentials
    - Open a terminal (Windows PowerShell on Windows, Bash on Linux, Terminal on MacOS)
    - Navigate to the extracted folder:
        - On Windows: `cd path\to\your\folder`
        - On Linux/MacOS: `cd path/to/your/folder`
    - Copy the `.env.example` file to `.env`:
    ```bash
    cp .env.example .env
    ```
    - Open `.env` and fill in your Instagram credentials by replacing the placeholder values, then save the file
4. Install Dependecies
    - In your terminal, run:
    ```bash
    pip install -r requirements.txt
    ```
5. Run:
    ```bash
    python main.py
    ```

## Notes
- Never share your .env file or commit to version control
- This project is for personal use only. Use at your discretion as it may violate Instagram laws.

## Credits
Developed by [Arham Islam](https://github.com/arhamislam) on May XX, 2025.