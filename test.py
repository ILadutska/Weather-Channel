# Hello from Ivan

import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
import json
import re


response = urlopen("https://api.weather.gov/points/34.031,-118.182")
json_data = response.read().decode("utf-8", "replace")
d = json.loads(json_data)
df = pd.json_normalize(d["properties"])

response = urlopen(df["forecastHourly"][0])
json_data = response.read().decode("utf-8", "replace")

d = json.loads(json_data)
df = pd.json_normalize(d["properties"])

df = pd.json_normalize(df["periods"][0])


df["day"] = 0
df["hour"] = 0

for i in range(df.shape[0]):
    # pattern to extract day
    pattern = r"(?=...........-).."
    df["day"][i] = re.search(pattern, df["startTime"][i])[0]

    # pattern to extract hour
    pattern = r"(?=........-).."
    df["hour"][i] = re.search(pattern, df["startTime"][i])[0]

df["day"] = df["day"].astype(int)
df["hour"] = df["hour"].astype(int)


df["day_hour"] = df["day"].astype(str) + "_" + df["hour"].astype(str)

df1 = df[df["day"] == 20]
fig, ax = plt.subplots()

# Step 3: Specify the x and y coordinates from the DataFrame
x = df1["hour"]
y = df1["temperature"]

# Step 4: Customize the plot (optional)
ax.plot(x, y, marker="o", linestyle="-.", color="b", label="Hour vs. Temp")
ax.set_xlabel("Hour")
ax.set_ylabel("Temperature")
ax.set_title("Hour vs. Temp Plot")
ax.legend()

# Step 5: Display the plot
plt.show()


df["shortForecast"].value_counts()


print(json_data)
