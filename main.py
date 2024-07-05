import requests
from datetime import datetime
import smtplib

MY_LAT = 50.003578 # Your latitude
MY_LONG = 18.463779 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(datetime.now().hour)

def is_dark(current_time, sunrise_time, sunset_time):
    if current_time > sunset_time or current_time < sunrise_time:
        return True
    else:
        return False
my_email = "janojano122222@gmail.com"
password = "izcyvcpissrofarr"

if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5 and is_dark(current_time=time_now, sunset_time= sunset, sunrise_time= sunrise):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=('Subject:LOOK UP\n\nThe ISS is visible!')
        )




