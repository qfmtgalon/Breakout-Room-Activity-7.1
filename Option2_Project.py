import requests
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IP Address of the User": ip_address,
        "Current Internet Protocol Version": response.get("version"),
        "Current City": response.get("city"),
        "Current Region": response.get("region"),
        "Country": response.get("country_name"),
        "Internet Service Provider": response.get("org"),
        "Autonomous System Number": response.get("asn")
    } 
   
    return location_data
res = get_location() 
for x, y in res.items(): 
    print(f"{x}: {y}")