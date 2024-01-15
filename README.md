# Robo CAR 

Create folder robo-car and copy the robo-car.py & bootup.sh

```bash
cd /home/pi/
git clone https://github.com/ivaddadi/robo-car.git -u <your_git_user"
chmod u+x bootup.sh
```

For lxd session to autostart the python script, check autostar file exits under user pi home directory or global xdg

`ls -l /home/pi/.config/lxsession/LXDE-pi/`

or

`/etc/xdg/lxsession/LXDE-pi/autostart`

edit the file autostart and add line `@lxterminal -e "/home/pi/robo-car/bootup.sh"`

reboot the pi and check terminal autosatrt on boot. To check via remote ssh session run 
```bash 
ps -aef | grep robo-car.py 
```
