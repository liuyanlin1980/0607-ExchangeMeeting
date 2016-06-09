sudo python /home/pi/wendu-0218.py
curl --request POST --data-binary @“/home/pi/datafile.txt” --header “U-ApiKey:XXXXXXXXXXXXXXXX”http://api.yeelink.net/v1.0/device/xxxx/sensor/xxxx/datapoints