# INKOGNITO

1st lets start with configuring the NetworkManager in Linux Debian. 
This was tested on Parrot OS--> should also work on Kali Linux.

bash'''
$ chmod +x /path/to/the/main.py
$ crontab -e
select /bin/nano
add to the last line of the file:
0 * * * * /path/to/the/main.py
'''

-->hit ctrl + x --> press y --> press enter --> ready

INKOGNITO is know configured to store the proxy list into the /tmp/inkognito.pac. 
The NetworkManager configured by it self is now rotating a 3 server proxy chain every 5 minutes. 
The proxy list is updated every hour. 
You can access the proxy chain via Browser or any other App, because all route through the NetworkManager.
Tracing by IPv4 should be quiet difficult now.
Dont forget to change your MAC, turn off IPv6, turn off GPS geolocation of your browser(location guard addon). 
Delete your logs, cache, cockies regular via bleachbit in override mode, 
and maybe think about canvas, uuid, 50xetc... .
