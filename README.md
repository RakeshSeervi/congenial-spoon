# Weather Application

A simple weather app using flask framework and OpenWeatherMap API

### Steps to get the application running
1. Clone the repository
2. Inside the project directory, create a python virtual environment
    ```
    python3 -m venv venv
    ```
3. Activate the virtual environment
    - On windows
        ```
        venv\Scripts\activate.bat
        ```
    - On Unix or MacOS
        ```
        source venv/bin/activate
        ```
4. Install the dependencies
    ```
    pip install -r requirements.txt
    ```
5. Configuring environment variables
    - Get your free API key from [here](https://openweathermap.org/api)
    - Create a `.env` file in the project directory
    - Add the below line to the file
        ```
        API_KEY=YOUR_API_KEY
        ```
7. Run the application
    ```
    python main.py
    ```
6. Visit `localhost:8000` on your browser
