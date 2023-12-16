# Your AI Assistant with Kivy

This project is a simple AI Assistant application built using the Kivy framework in Python. The AI Assistant can perform tasks such as searching on YouTube, Google, Instagram, fetching weather information, getting news headlines, and searching on Wikipedia.

## Features

- **Search on YouTube:** Allows the user to search for videos on YouTube.

- **Search on Google:** Performs a Google search based on the user's input.

- **Search on Instagram:** Opens the Instagram profile page based on the provided username.

- **Get Weather:** Fetches the current weather information for a specified city using the Weatherstack API.

- **Get News:** Retrieves top news headlines using the News API.

- **Search on Wikipedia:** Looks up information on Wikipedia based on the user's query.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Kivy
- Pyttsx3
- Requests
- Wikipedia API
- News API Key (optional, if you want to use the news feature)
- Weatherstack API Key (optional, if you want to use the weather feature)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Abhishekkr21/your-ai-assistant.git
    cd your-ai-assistant
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Configuration

- Set your Weatherstack API key in the `get_weather` function of `main.py`.
  
- Set your News API key in the `get_news` function of `main.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
