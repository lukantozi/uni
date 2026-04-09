#!/bin/bash

# Task 1
echo "Task 1"
whoami
# styx@devops:~$ whoami
# styx

# Task 2
echo "Task 2"
ps aux | head -n 5
# USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# root           1  0.3  0.3  22172 13416 ?        Ss   10:44   0:00 /sbin/init splash noprompt noshell automatic-ubiquity
# root           2  0.0  0.0      0     0 ?        S    10:44   0:00 [kthreadd]
# root           3  0.0  0.0      0     0 ?        S    10:44   0:00 [pool_workqueue_release]
# root           4  0.0  0.0      0     0 ?        I<   10:44   0:00 [kworker/R-rcu_g]

# Task 3
echo "Task 3"
ps -eo pid,comm,pri,ni --sort=-pri | head -n 5
#    PID COMMAND         PRI  NI
#     38 khugepaged        0  19
#     36 ksmd             14   5
#      1 systemd          19   0
#      2 kthreadd         19   0

# Task 4
echo "Task 4"
nice -n 10 firefox &
# [1]  + done       nice -n 10 firefox

# Task 5
echo "Task 5"
sudo renice -5 -p $(pgrep firefox)
# [sudo] password for styx:
# 3331 (process ID) old priority 0, new priority -5

# Task 6
echo "Task 6"
dd if=/dev/zero of=/home/styx/largefile bs=5M count=10
# 10+0 records in
# 10+0 records out
# 52428800 bytes (52 MB, 50 MiB) copied, 0.0414161 s, 1.3 GB/s
nice -n 5 find . > /dev/null &
# [1] 1835
sudo nice -n -10 gzip largefile &
#[2] 1836
#[1]   Done                    nice -n 5 find . > /dev/null
top
# top - 11:06:35 up 22 min,  1 user,  load average: 0.00, 0.00, 0.00
# Tasks: 116 total,   2 running, 114 sleeping,   0 stopped,   0 zombie
# ...
# ...
#      23 root      rt   0       0      0      0 S   0.0   0.0   0:00.17 migration/1
#      24 root      20   0       0      0      0 S   0.0   0.0   0:00.01 ksoftirqd/1
# [2]+  Done                    sudo nice -n -10 gzip largefile

# Task 7
echo "Task 7"
vi &
# [1] 1851
fg %1
# vi
bg %1
# bash: bg: %1: no such job

# Task 8
echo "Task 8"
htop
#   [Main] [I/O]
#     PID△USER       PRI  NI  VIRT   RES   SHR S  CPU% MEM%   TIME+  Command
#     405 root        RT   0  282M 27452  8760 S   0.0  0.7  0:00.07 │  ├─ /sbin/multipathd -d -s
#     406 root        RT   0  282M 27452  8760 S   0.0  0.7  0:00.00 │  └─ /sbin/multipathd -d -s
#     398 root        20   0 29216  8076  5092 S   0.0  0.2  0:00.10 ├─ /usr/lib/systemd/systemd-udevd
#     559 systemd-re  20   0 21584 13000 10700 S   0.0  0.3  0:00.06 ├─ /usr/lib/systemd/systemd-resolved
#     566 systemd-ti  20   0 91028  7952  6984 S   0.0  0.2  0:00.04 ├─ /usr/lib/systemd/systemd-timesyncd

# Task 9
echo "Task 9"
sha256sum /dev/zero &
# [1] 1895
renice 15 -p $(pgrep sha256sum)
# 1895 (process ID) old priority 0, new priority 15

# Task 10
echo "Task 10"
nice -n -5 dd if=/dev/zero of=/dev/null &
# [1] 1908
nice -n 10 dd if=/dev/zero of=/dev/null &
# [2] 1911
top
#    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#   1910 root      15  -5    5724   2084   1968 R  99.7   0.1   0:10.34 dd
#   1913 root      30  10    5724   2080   1964 R  99.0   0.1   0:05.09 dd
fg
sudo nice -n 10 dd if=/dev/zero of=/dev/null
# ^C75647420+0 records in
# 75647419+0 records out
# 38731478528 bytes (39 GB, 36 GiB) copied, 96.1244 s, 403 MB/s

# Task 11
echo "Task 11"
pstree -p
# systemd(1)─┬─ModemManager(781)─┬─{ModemManager}(787)
#            │                   ├─{ModemManager}(788)
#            │                   └─{ModemManager}(790)
#            ├─agetty(947)
#            ├─containerd(871)─┬─{containerd}(872)

# Task 12
echo "Task 12"
ps aux | egrep "Z|defunct"
# USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# styx        1995  0.0  0.0   6544  2324 pts/0    S+   11:25   0:00 grep -E --color=auto Z|defunct
ps -o ppid= -p 1995
# not applicable (returned nothing)

# Task 13
echo "Task 13"
top
# top - 11:27:40 up 43 min,  1 user,  load average: 1.00, 0.96, 0.60
# Tasks: 122 total,   2 running, 120 sleeping,   0 stopped,   0 zombie
# %Cpu(s): 24.2 us, 26.2 sy,  0.0 ni, 49.4 id,  0.2 wa,  0.0 hi,  0.0 si,  0.0 st
# MiB Mem :   3916.0 total,   3047.9 free,    546.1 used,    560.9 buff/cache
# MiB Swap:    768.0 total,    768.0 free,      0.0 used.   3369.9 avail Mem
# 
#     PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#    1910 root      15  -5    5724   2084   1968 R 100.0   0.1  10:11.87 dd
#    1584 root      20   0       0      0      0 I   0.3   0.0   0:01.03 kworker/0:3-events
htop
#     0[|                                                             0.7%] Tasks: 31, 47 thr, 91 kthr; 2 running
#     1[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||100.0%] Load average: 1.00 0.96 0.61
#   Mem[||||||||||||||||||                                      308M/3.82G] Uptime: 00:44:02
#   Swp[                                                           0K/768M]
# 
#   [Main] [I/O]
#     PID△USER       PRI  NI  VIRT   RES   SHR S  CPU% MEM%   TIME+  Command
#       1 root        20   0 22172 13420  9540 S   0.0  0.3  0:00.77 /sbin/init splash noprompt noshell automatic-ubiquity
#     337 root        19  -1 66880 17364 16172 S   0.0  0.4  0:00.16 ├─ /usr/lib/systemd/systemd-journald
#     389 root        RT   0  282M 27452  8760 S   0.0  0.7  0:00.08 ├─ /sbin/multipathd -d -s
#     400 root        20   0  282M 27452  8760 S   0.0  0.7  0:00.00 │  ├─ /sbin/multipathd -d -s

# Task 14
echo 'Task 14'
ls /proc/$(pgrep firefox)
# arch_status  cmdline             exe                ksm_stat   mountinfo   oom_adj        root       smaps_rollup  task
# attr         comm                fd                 limits     mounts      oom_score      sched      stack         timens_offsets
cat /proc/$(pgrep firefox)/status
# Name:	firefox
# Umask:	0022
# State:	S (sleeping)
# Tgid:	3331

# Task 15
echo "Task 15"
vi &
# [2] 2029

# Task 16
echo "Task 16"
vim
pkill -HUP vi
# [1]+  Stopped                 vi
pkill -QUIT vi
# Hangup
# Vim: Caught deadly signal QUIT
# Vim: Finished.
# Quit (core dumped)
pkill -STOP vi
# [2]+  Stopped                 vi

# Task 17
echo "Task 17"
pkill -u $USER
# would log me out

# Task 18
echo "Task 18"
sleep 600 &
# [1] 2120
ps aux | grep sleep
# styx        2120  0.0  0.0   5684  2108 pts/0    S    11:37   0:00 sleep 600
# styx        2122  0.0  0.0   6544  2332 pts/0    S+   11:37   0:00 grep --color=auto sleep
kill -TERM 2120
ps aux | grep sleep
# styx        2124  0.0  0.0   6544  2328 pts/0    S+   11:38   0:00 grep --color=auto sleep
# [1]+  Terminated              sleep 600

# Task 19
echo "Task 19"
sleep 200 &
# [1] 2210
fg %1
# sleep 200
vi
^Z
# [1]+  Stopped                 vi
# $
vi
^Z
# [2]+  Stopped                 vi
# $
jobs
# [1]-  Stopped                 vi
# [2]+  Stopped                 vi
fg %1
# vi
jobs
# [2]+  Stopped                 vi
fg %2
# vi
^Z
# [2]+  Stopped                 vi

# Task 20
echo "Task 20"
top
#   PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#    1792 styx      20   0   14996   7108   5144 S   0.7   0.2   0:02.27 sshd
#    2222 styx      20   0   11916   5956   3756 R   0.3   0.1   0:00.04 top
kill -9  2222

# Task 21
echo "Task 21"
sleep 600 &
# [1] 2224
kill -STOP 2224
jobs
# [1]+  Stopped                 sleep 600
kill -CONT 2224
jobs
# [1]+  Running                 sleep 600 &

# Task 22
echo "Task 22"
nohup ./long_running_script.sh &
# [1] 2419
# styx@devops:~$ nohup: ignoring input and appending output to 'nohup.out'

# Task 23
echo "Task 23"
ps aux | grep long_running_script.sh
# styx        2419  0.0  0.0   7340  3620 pts/0    S    11:57   0:00 /bin/bash ./long_running_script.sh
# styx        2423  0.0  0.0   6684  2340 pts/1    S+   11:57   0:00 grep --color=auto long_running_script.sh
kill -9 2419
ps aux | grep long_running_script.sh
# styx        2425  0.0  0.0   6684  2340 pts/1    S+   11:58   0:00 grep --color=auto long_running_script.sh

# Task 24
timeout 10s sleep 600
# exits after 10s
