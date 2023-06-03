"""
@Author: shubham shirke
@Date: 2022-06-02 21:45:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 21:45:30
@Title : calculate windchill using temperature and wind speed.
"""
def calculate_wind_chill(temperature, wind_speed):
    """
    Description: Calculates the wind chill factor using the National Weather Service formula.
    Parameters: temperature - temperature in Fahrenheit, wind_speed - wind speed in miles per hour.
    Returns: Wind chill factor in Fahrenheit.
    """
    if temperature > 50 or wind_speed < 3:
        return temperature  # No wind chill factor for temperatures above 50°F or when wind speed is less than 3 mph.

    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * wind_speed ** 0.16) + (0.4275 * temperature * wind_speed ** 0.16)
    return wind_chill


# Read temperature and wind speed as input
temperature = float(input("Enter the temperature in Fahrenheit: "))
wind_speed = float(input("Enter the wind speed in miles per hour: "))


wind_chill = calculate_wind_chill(temperature, wind_speed)

print("Wind chill factor:", wind_chill)


