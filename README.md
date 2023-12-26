# beepy
Beepy Utilties

A silly utility to read the battery percentage and feed it to cowsay. If the battery is at or above 30% the cow looks wired. As the battery drains it transistions to paranoid, tired and then dead.

```text
 _____________
< Battery 31% >
 -------------
        \   ^__^
         \  (OO)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

The script reads the file ```/sys/firmware/beepy/battery_percent```

A useful option is to change the script to an executable
```
$chmod +x battstat.py
```
Then copy the python script to ```/usr/bin```
```
$sudo cp battstat.py /usr/bin/battstat
```
Then you can run it from anywhere
```text
admin@beepy:~ $ battstat
 _____________
< Battery 28% >
 -------------
        \   ^__^
         \  (@@)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```




