# Chess Clock App README

## Overview
This is a Chess Clock application developed using PyQt6. It serves as a tool for managing chess matches, featuring functionalities such as creating profiles, displaying profiles, viewing match history, and checking rankings. The application is integrated with a MySQL database for storing player information and match data.

## Features
- **Profile Management**: Users can create player profiles with their names and other relevant details.
- **Statistics**: Users can view their match history and performance statistics.
- **Ranking**: The application provides a ranking system based on players' performance.
- **Game Setup**: Players can choose the game type and enter their names before starting a match.
- **Match Timer**: The match timer starts running when players confirm their names and game type.
- **Game Controls**: During the match, players can use buttons for actions such as declaring checkmate, draw, or resignation.
- **Winner Declaration**: After the match ends, a window pops up to declare the winner.

## Usage
1. **Main Window**: 
   - Upon launching the application, the main window appears, featuring buttons for creating profiles, viewing statistics, and checking rankings. It also displays the application logo.
   
2. **Profile Creation**:
   - Click on the "Create Profile" button to create a new player profile. Fill in the necessary details and submit.
   
3. **Profile Display**:
   - Users can view their profile information by clicking on the "Stats" button.
   
4. **Match Setup**:
   - To start a match, select the game type and enter the players' names. If the names are registered in the database, the match window will open.
   
5. **Match Window**:
   - Once the match window opens, the timer for both players starts running. Players can use the provided buttons for actions during the match.
   
6. **Match Conclusion**:
   - After the match ends, a winner declaration window appears, announcing the winner based on the match outcome.

## Database Integration
- The application is integrated with a MySQL database for storing player profiles and match data.
- Ensure that the MySQL server is running and properly configured before using the application.

## Requirements
- Python 3.x
- PyQt6 library
- MySQL server

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Install PyQt6: `pip install PyQt6`
3. Set up the MySQL database and configure the connection settings in the application code.

## Running the Application
1. Navigate to the project directory.
2. Run the main Python script: `python main.py`

## Credits
This application was developed by Nasiful Alam.

## License
This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.
