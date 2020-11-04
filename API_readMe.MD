## Install
____

```
sudo apt update
sudo apt-get dist-upgrade
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
sudo apt-get install samba samba-common-bin
sudo apt install ntfs-3g
```

## Activate your virtual Environment and install requirements
---
```
python3 -m venv env
pip3 install requirements.txt 
```
*Note: requirements.txt file has to be in same directory when you run above commands*

## Mount USB to microntroller
* Get USB `UUID`
```
sudo blkid
```
*Copy UUID of your USB,` UUID` is alphanumeric value given after `UUID` and Label will be the name of your USB*

* Setting up USB to automount of boot up
```
sudo nano -Bw /etc/fastab
```
* Add the following line to the fstab file, save and then exit.  
```
UUID=1945-CB1E /mnt/usb auto defaults,user,nofail 0 2
```
*Note the 1945-CB1E should be replaced by the `UUID` of your USB device*

*/mnt/usb will be the directory of you usb on the PI*

## Setting up samba server
---
* Create a directory called files in your USB
* open samba configuration file

```
sudo nano /etc/samba/smb.conf
```
* Copy the followiing on the configuration file

```
[Files]
comment = Files
public = yes
writeable = yes
browsable = yes
path = /mnt/USB1/Files
create mask = 0777
directory mask = 0777
guest ok = yes
only guest = yes

```

* Getting the name of the samba server
```
hostname -I
```
*Note that this will change everytime the microcontroller is switched off and on again*

