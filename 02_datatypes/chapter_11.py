# -----------------------------------
#  Working with Dates and Time (Arrow)
# -----------------------------------
# Arrow is a third-party library that simplifies working with dates and times.
# It is more user-friendly than the built-in datetime module.

import arrow

# Current time in UTC
utc_time = arrow.utcnow()
print(f"Current UTC time: {utc_time}")

# Current local time
local_time = arrow.now()
print(f"Current local time: {local_time}")

# -----------------------------------
#  Timezone Conversion
# -----------------------------------
# Convert UTC time to another timezone (e.g., Europe/Madrid)

brewing_time = arrow.utcnow()
madrid_time = brewing_time.to("Europe/Madrid")

print(f"Brewing time in Madrid: {madrid_time}")

# -----------------------------------
# ⏱ Time Differences (timedelta concept)
# -----------------------------------
# Arrow can also calculate differences between dates

future_time = brewing_time.shift(hours=2)
time_difference = future_time - brewing_time

print(f"Time difference: {time_difference}")

# -----------------------------------
#  Collections Mod
# -----------------------------------
# collections provides specialized container datatypes

from collections import namedtuple

# Define a namedtuple (like a lightweight class)
ChaiProfile = namedtuple("ChaiProfile", ["flavor", "aroma"])

# Create an instance
my_chai_profile = ChaiProfile(flavor="spicy", aroma="sweet")

# Access attributes
print(f"Flavor: {my_chai_profile.flavor}")
print(f"Aroma: {my_chai_profile.aroma}")