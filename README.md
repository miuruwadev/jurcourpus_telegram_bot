# JURCORPUS TELEGRAM BOT

A Telegram bot built with Python, `asyncio`, and `aiogram`.

## Features
- Responds to `/start` command
- Configured with `.env` for secure token storage

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

## Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Dublicate a `.env.example` as `.env` file in the project root:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

5. Run the bot:
   ```bash
   python main.py
   ```

## Usage
- Send `/start` to the bot in Telegram to receive a welcome message.

## Project Structure
- `main.py`: Main bot script
- `.env`: Environment variables (not tracked in git)
- `.gitignore`: Ignored files and directories
- `requirements.txt`: Project dependencies

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
MIT License