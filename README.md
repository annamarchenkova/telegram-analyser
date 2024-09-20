# Telegram Message Reader and Analyzer

This project is a Python-based tool that reads messages from a specific Telegram chat for a given day and performs basic analysis on the downloaded messages. It uses the Telethon library to interact with the Telegram API and allows for further expansion with a message analysis module.

## Project Structure

```plaintext
telegram_reader/
│
├── config/
│   └── .env                     # Environmental variables file
│
├── src/
│   ├── __init__.py              # (optional) To make `src` a Python package
│   ├── main.py                  # Main script
│   ├── telegram_reader.py       # Contains the TelegramReader class
│   └── message_analyzer.py      # Contains the MessageAnalyzer class
│
├── pyproject.toml               # Poetry project configuration
├── poetry.lock                  # Locked dependency versions
└── README.md                    # Project documentation
```

## Features
- **Telegram Message Reader**: Downloads messages from a specific Telegram chat for a given day.
- **Message Analyzer**: Contains placeholder methods for future message analysis and summarization.
  
## Requirements

- Python 3.7+
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Poetry](https://python-poetry.org/)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-reader-analyzer.git
cd telegram-reader-analyzer
```

### 2. Install Poetry

If you don't have Poetry installed, install it using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Initialize the Environment with Poetry

Inside the project directory, run:

```bash
poetry install
```

This will install all the necessary dependencies.

### 4. Set Up the `.env` File

You need to create a `.env` file inside the `config/` folder with the following content:

```plaintext
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
PHONE=your_phone_number
```

Replace the placeholders with your actual Telegram API credentials and phone number. You can obtain the `API_ID` and `API_HASH` by creating a new Telegram app [here](https://my.telegram.org/).

### 5. Run the Project

Activate the Poetry virtual environment:

```bash
poetry shell
```

Then, run the project using:

```bash
python src/main.py
```

## Usage

### TelegramReader

The `TelegramReader` class connects to the Telegram API and downloads messages from a specified chat for a given day. In the `main.py` script, you can specify the chat ID or username and the date for which you want to download the messages:

```python
chat_id = 'CHAT_ID_OR_USERNAME'  # Replace with the chat ID or username
target_date = '2024-09-19'  # Replace with the desired date (YYYY-MM-DD)
```

### MessageAnalyzer

The `MessageAnalyzer` class provides methods for analyzing and summarizing the downloaded messages. These methods are currently placeholders and will be expanded upon later.

- `analyze_messages()`: Analyze the downloaded messages.
- `summarize()`: Generate a summary of the messages.

## Project Structure

### config/.env

This file contains sensitive environmental variables like the Telegram API credentials.

### src/main.py

This is the main script that runs the project. It connects to the Telegram API, downloads messages, and passes them to the `MessageAnalyzer` for analysis.

### src/telegram_reader.py

This file contains the `TelegramReader` class, which handles connecting to Telegram and downloading messages from a specific chat and day.

### src/message_analyzer.py

This file contains the `MessageAnalyzer` class, which has placeholder methods for analyzing and summarizing the downloaded messages.

## Future Enhancements

- Implement detailed message analysis logic in the `MessageAnalyzer` class.
- Add support for different types of message filtering (e.g., filtering by keywords, media, or user).
- Extend summarization features to generate reports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
