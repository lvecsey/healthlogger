*Overview*

This python3 program will query the ceph health detail every 60 seconds.
It writes the status to a data file, to use with plotting (gnuplot)
The program will flush the info to the output file, every 5 minutes.

*Dependencies*

```console
sudo apt-get install gnuplot
```

Make sure you also have the ceph command installed. You should also have a /var/log/ceph directory already.

*Data format*

The data file consists of a timestamp, and values such as 0.0, 1.0, etc depending on whether the health is showing as OK.

*Creating data file*

We store the data file in the /var/log/ceph directory area, which is owned by group ceph.

Decide on which user to use, in the permissions for the commands below:

```console
usermod --append --groups ceph user
touch /var/log/ceph/ceph_health.dat
```

*Running*

To test that the program can use ceph and log to the data file:

```console
python3 healthlogger.py
```

*Service file*

You don't need to leave the python program running from a console shell. Simply install a service file (sample provided) and have systemd keep it running for you.

Be sure to edit the *ExecStart* path(s) and the *User* setting in the service file.

You may need to adjust the location of your ceph.conf file, which is specified in the service file as well.

```console
cd ~/src/healthlogger
sudo cp healthlogger.service /usr/lib/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable healthlogger
sudo systemctl start healthlogger
```

Verify that you are getting "1.0" values in the ceph_health.dat file and you should be all set.

*Plotting*

```console
cd ~/src/healthlogger
gnuplot healthlogger.plot
feh healthlogger.png
```
