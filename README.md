# Weather App

A simple Python project that fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/api).

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Create a virtual environment
It’s a good idea to keep dependencies isolated:
```bash
python -m venv venv
```

Activate it:

- On Linux/Mac:
  ```bash
  source venv/bin/activate
  ```
- On Windows (PowerShell):
  ```powershell
  .\venv\Scripts\activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create an environment file
You’ll need an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

Create a `.env` file in the project root and add:
```env
OPENWEATHER_API_KEY=your_api_key_here
```

---

## Usage
Run the app (replace with the actual entrypoint if different):
```bash
python main.py
```

---

## Notes
- Keep your `.env` file out of version control (already in `.gitignore`).
- If you run into issues, double-check that your virtual environment is active and the API key is valid.
