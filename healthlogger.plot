set terminal png size 1920,1080

set output "healthlogger.png"

set xdata time

set timefmt "%s."

set format x "%m/%d"

set yrange [-0.2 : 1.2 ]

plot "/var/log/ceph/ceph_health.dat" using 1:2 w l
