if [ $# -eq 0 ]; then
    echo "Missing pi name! (0-9)"
    exit 1
fi

echo $1 > /home/pi/pi_name

cp wpa_supplicant.conf /etc/wpa_supplicant
cp interfaces /etc/network/interfaces
# cp rc.local /etc/rc.local

cp pigpiod /etc/init.d
chmod u+x /etc/init.d/pigpiod
update-rc.d pigpiod defaults
update-rc.d pigpiod enable
systemctl enable pigpiod.service


cp client.py /home/pi
chmod u+x /home/pi/client.py

cp patterns.py /home/pi
chmod u+x /home/pi/patterns.py

cp client.sh /home/pi
chmod u+x /home/pi/client.sh

mkdir /home/pi/logs
crontab /home/pi/makepi/crontab

echo "added files!"
