
# Setting up the demonstrator


## Enabling SMB protocol in windows
___
**If SMB already activated this section can be skipped**

1.  Go to control panel
2. Navigate to `programs` in control panel
3. Below programs and features under control panel click `Turn windows features on and off` option
4. Navigate to `SMB1.0/CIFS File Sharring Support` box
5. Tick the box besides it and press OK 
## Connecting to samba using windows 
___
1.  Connect to the same network or wifi as the microcontroller
2.  Obtain the IP address of the samba server
* Use function `getIP()` fileTransfer to get the IP address
``` python
    getIP()
```
3. Go to network on file Explorer

![netowrk image](https://helpdeskgeek.com/wp-content/pictures/2020/04/Windows-Explorer-Network-Tab.png)

4. On the search bar where it has`>Netwrok` seacrch for samba server IP address
```
    \\:192.168,137.84
```
* replace `192.168,137.84` wirh IP address of your server

## Connecting to samba using a mobile device
___

* Demo works on IOS
1.  Connect to the same network or wifi as the microcontroller
2. Navigate to files
3. Click on the more option that is on the top right corner

![image](https://cdn.osxdaily.com/wp-content/uploads/2019/10/files-elipsis-menu.png)

4. tap on `Connect to Server` from the options provided
5. Enter the IP address of server 
6. Connect as guest when promted with connection method
7. When connected navigate to desired folder, use long press on to get options to copy a document

* On Android

1. Requires the download of a third party app.
    
    Example of such a an application is:
    
    An application called [X-plore file Manager](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore&hl=en_ZA&gl=US) 

## Running the demonstrator on a python script

* See docomentation of `driver.py` file