# NASA POWER API Weather Data Plot
# Andy Kieckhefer
# met-ak-news 
# This script fetches weather data from the NASA POWER API and generates plots for analysis.

# =========================================================
# NASA POWER API Weather Data Plot
# ---------------------------------------------------------
# This script:
#   • Pulls daily temperature data from NASA.gov
#   • Parses JSON data
#   • Plots the results with matplotlib
# ---------------------------------------------------------
# Run in VS Code with:  python nasa_weather_plot.py
# =========================================================

# === 0. Import libraries ===
import requests # For making HTTP requests
import matplotlib.pyplot as plt # For plotting data
from datetime import datetime # For handling date and time

# === 1. Define API parameters ===
# Location: Houston, TX
LAT, LON = 29.76, -95.37
START, END = "20250101", "20250131"  # Date range (YYYYMMDD)

# NASA POWER API endpoint
url = (
    f"https://power.larc.nasa.gov/api/temporal/daily/point?"
    f"parameters=T2M&start={START}&end={END}&latitude={LAT}&longitude={LON}"
    f"&format=JSON&community=RE"
) # Constructed API URL

# === 2. Fetch the data ===
print("Fetching data from NASA POWER API...")
response = requests.get(url) # Make GET request to the API
response.raise_for_status()
data = response.json()

# === 3. Extract temperature values ===
temps = data["properties"]["parameter"]["T2M"]  # Daily 2-meter air temp (°C)
dates = [datetime.strptime(d, "%Y%m%d") for d in temps.keys()] # Convert date strings to datetime objects
values = list(temps.values())

# === 4. Plot results ===
plt.figure(figsize=(10, 5)) # Create a new figure
plt.plot(dates, values, marker="o", linestyle="-") # Line plot with markers
plt.title("Daily Average Temperature - Houston, TX Andy Kieckhefer (NASA POWER Data)") # Plot title
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True) # Add grid for better readability
plt.tight_layout()
plt.show()

# === 5. Completion message ===
print("✅ Plot complete. Data successfully retrieved and visualized. Thank you for stopping by! @KieckheferA")
# =========================================================
# End of nasa_weather_plot.py
# =========================================================
# Constructed API URL
# =========================================================

