import pyowm

@frappe.whitelist
def get_current_weather():
    current_weather = pyowm.get_weather
    return