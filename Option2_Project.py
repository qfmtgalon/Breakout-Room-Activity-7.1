import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IP Address of the User             ": ip_address,
        "Current Internet Protocol Version  ": response.get("version"),
        "Current City                       ": response.get("city"),
        "Postal Code                        ": response.get("postal"),
        "Current Region                     ": response.get("region"),
        "User Country                       ": response.get("country_name"),
        "Time Zone of the Country           ": response.get("timezone"),
        "Internet Service Provider          ": response.get("org"),
        "Autonomous System Number           ": response.get("asn")
    } 
   
    return location_data
res = get_location() 
for x, y in res.items(): 
    print(f"{x}: {y}")