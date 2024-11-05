@echo off
cd /d "E:\Projects\Chess-Clock\"  # Navigate to your project directory
call "E:\Projects\Chess-Clock\venv_chess_clock\Scripts\activate"  # Activate the virtual environment
python main.py  # Run the main script
pause  # Keeps the window open to view any errors