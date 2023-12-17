import requests


def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()
    return response['ip']

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IPv4 Address": ip_address,
        "City": response.get("city"),
        "Region": response.get("region"),
        "Country": response.get("country_name"),
        "ASN": response.get("asn"),
        "Provider (ISP)" : response.get("org"),
        "Latitude / Longitude": str(response.get("latitude")) + ", " + str(response.get("longitude")),
    }
    return location_data

ip_address = get_ip()
print(ip_address)

location_data = get_location()
print(location_data)
