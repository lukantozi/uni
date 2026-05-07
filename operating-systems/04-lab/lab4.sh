#!/bin/bash

# Task 1
echo "Task 1"
whoami
# styx

# Task 2
echo "Task 2"
vim &
# [1] 83670
# [1]  + suspended (tty output)  nvim

# Task 3
echo "Task 3"
ps
#    PID TTY          TIME CMD
#  81237 pts/2    00:00:00 zsh
#  83670 pts/2    00:00:00 nvim
#  84770 pts/2    00:00:00 ps

# Task 4
echo "Task 4"
ps -x | head
echo "'x' option shows processes without controlling terminal, like daemons or background services"
#    PID TTY      STAT   TIME COMMAND
#    622 ?        Ss     0:02 /usr/lib/systemd/systemd --user
#    624 ?        S      0:00 (sd-pam)
#    633 ?        Ss     0:00 /usr/bin/dbus-broker-launch --scope user
#    634 ?        S      0:00 dbus-broker --log 11 --controller 10 --machine-id 0c9cf16d2ad243058fa946cddf5545c0 --max-bytes 100000000000000 --max-fds 25000000000000 --max-matches 5000000000
ps -ax | head
#    PID TTY      STAT   TIME COMMAND
#      1 ?        Ss     0:04 /sbin/init
#      2 ?        S      0:00 [kthreadd]
#      3 ?        S      0:00 [pool_workqueue_release]
#      4 ?        I<     0:00 [kworker/R-rcu_gp]
echo "'a' is used to show processes associated with all users with terminals"
echo ""
echo "so basically 'ax' shows all the processes in the system"

# Task 5
ps -l
# F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
# 0 S  1000   81237    1308  0  80   0 -  2422 sigsus pts/2    00:00:00 zsh
# 0 T  1000   88242   81237  0  85   5 -  3704 do_sig pts/2    00:00:00 nvim
echo "'-l' option shows more detailed information of current processes"
ps -u $(whoami)
# USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# styx         705  0.0  0.0  16000  3968 tty1     Ssl+ 11:35   0:00 start-hyprland
# styx         733  1.4  0.7 2338148 49768 tty1    Sl+  11:35   1:23 Hyprland --watchdog-fd 4
# styx         790  0.0  0.2 1832384 15936 tty1    Sl+  11:36   0:00 hyprpaper -c /home/styx/.config/hypr/hyprpaper.conf
# styx         795  0.0  0.0  84096  6120 tty1     Sl+  11:36   0:00 hypridle
echo "'-u whoami' option shows all the processes connected to the user currenlty logged in"

# Task 6
echo "Task 6"
tty
# /dev/pts/2

# Task 7
echo "Task 7"
ps -f -p $(pgrep ps)
# UID          PID    PPID  C STIME TTY      STAT   TIME CMD
# root         370       2  0 11:35 ?        S      0:00 [psimon]
# root         390       2  0 11:35 ?        S      0:00 [psimon]
# root         600       2  0 11:35 ?        S      0:00 [psimon]

# Task 8
echo "Task 8"
ps -f -p 1
# UID          PID    PPID  C STIME TTY          TIME CMD
# root           1       0  0 11:35 ?        00:00:06 /sbin/init

# Task 9
echo "Task 9"
pstree
# systemd─┬─NetworkManager───3*[{NetworkManager}]
#         ├─atop
#         ├─bluetoothd
#         ├─crashhelper───{crashhelper}
#         ├─dbus-broker-lau───dbus-broker
#         ├─2*[hypridle───{hypridle}]
#         ├─hyprlock───24*[{hyprlock}]
#         ├─login───start-hyprland─┬─Hyprland─┬─Xwayland───12*[{Xwayland}]

# Task 10
echo "Task 10"
top
#     PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#    1387 styx      20   0   20.8g 598088 245356 S   5.3   8.5   5:40.94 firefox
#    1762 styx      20   0 3314356 292076  89060 S   2.0   4.2   2:36.67 WebExtensions
#     733 styx      20   0 2336252  51520  44152 S   1.7   0.7   1:36.52 Hyprland
#     797 styx      20   0 1351580  36304  31584 S   1.3   0.5   1:28.19 waybar
#  141915 styx      20   0 2053628  93412  67680 S   1.3   1.3   0:05.01 hyprlock
#  118644 styx      20   0 1351572  57452  43124 S   1.0   0.8   0:07.87 waybar
#      16 root      -2   0       0      0      0 I   0.3   0.0   0:07.73 rcu_preempt

# Task 11
echo "Task 11"
su -
cd /proc
# [root@flumenport proc]# ls 153543
# arch_status  coredump_filter	 io		    mountinfo	oom_score_adj  setgroups     task
# attr	     cpu_resctrl_groups  ksm_merging_pages  mounts	pagemap        smaps	     timens_offsets
# autogroup    cwd		 ksm_stat	    mountstats	personality    smaps_rollup  timers
# auxv	     environ		 limits		    net		projid_map     stack	     timerslack_ns
# cgroup	     exe		 loginuid	    ns		root	       stat	     uid_map
# clear_refs   fd			 map_files	    numa_maps	sched	       statm	     wchan
# cmdline      fdinfo		 maps		    oom_adj	schedstat      status
# comm	     gid_map		 mem		    oom_score	sessionid      syscall

# Task 12
echo "Task 12"
ps -f $(pgrep -x init)
# UID          PID    PPID  C STIME TTY          TIME CMD
# styx       81237    1308  0 12:52 pts/2    00:00:00 -zsh
# styx      161032  161030  0 13:44 pts/2    00:00:00 zsh
# styx      171660  161032  0 13:48 pts/2    00:00:00 ps -f

# Task 13
echo "Task 13"
ps -eo nlwp | awk '{sum += $1} END {print "Total threads:", sum}'
# Total threads: 1177

# Task 14
echo "Task 14"
ps -o nlwp -p $(pgrep -o firefox)
# NLWP
#  273

# Task 15
echo "Task 15"
top -H -p 81237
#     PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#   81237 styx      20   0    9688   7264   6376 S   0.0   0.1   0:00.28 zsh

# Task 16
echo "Task 16"
ls /proc/$(pgrep -o firefox)/task
# 100673  107473  114605  123639  135733  1407    1442    1466    1488    154091  1635    1731    181808  2044   98380
# 100674  108519  114606  123640  137804  1419    144370  1467    1489    154092  1636    1732    1821    2308   98381
# 100675  108520  114607  123641  137805  1420    144371  146720  1490    154093  1637    1734    1822    2449   98382

# Task 17
echo "Task 17"
(while true; do echo "Running"; sleep 1; done) & ps -T -p $!
# ps -T -p $!
# [1] 200070
# Running
#     PID    SPID TTY          TIME CMD
#  200070  200070 pts/2    00:00:00 zsh
# 
# uni/operating-systems/lab4 on  master [?] via  v15.2.1-gcc
# ✦ ❯ Running
# Running
# Running

# Task 18
echo "Task 18"
ls
# create_thread.c  lab4.sh  thread

# uni/operating-systems/lab4 on  master [?] via  v15.2.1-gcc
./thread
# Thread running: iteration 1
# Thread running: iteration 2
# Thread running: iteration 3
# Thread running: iteration 4
# Thread running: iteration 5

# Task 19
echo "Task 19"
ps -m -l $(pgrep firefox)
# F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY        TIME CMD
# 0 -  1000    1387     733  1   -   - - 3185531 -    tty1       2:12 /usr/lib/firefox/firefox
# 0 S  1000       -       -  1  80   0 -     - poll_s -          2:12 -
# 1 S  1000       -       -  0  80   0 -     - anon_p -          0:00 -
# 1 S  1000       -       -  0  80   0 -     - futex_ -          0:00 -

# Task 20
echo "Task 20"
htop
# presed H to toggle threadview
#  227279 styx        20   0  9916  7868  5616 R   3.5  0.1  0:00.93 htop
#       1 root        20   0 23460 11756  8876 S   0.0  0.2  0:07.62 /sbin/init
#     337 root        20   0 73800 16828 16240 S   0.0  0.2  0:02.49 /usr/lib/systemd/systemd-journald
#     352 root        20   0 14896  5552  4540 S   0.0  0.1  0:00.11 /usr/lib/systemd/systemd-userdbd
#     379 systemd-ti  20   0 89816  7476  6268 S   0.0  0.1  0:00.31 /usr/lib/systemd/systemd-timesyncd

# Task 21
echo "Task 21"
gcc -pthread create_three_threads.c -o threads
./threads
# Thread 0 running
# Thread 2 running
# Thread 1 running

# Task 22
echo "Task 22"
sudo pacman -S stress-ng
# looking for conflicting packages...
# 
# Packages (5) apparmor-4.1.7-1  judy-1.0.5-9  lksctp-tools-1.0.21-1  python-legacy-cgi-2.6.4-2  stress-ng-0.20.01-1
# 
# Total Download Size:    5.24 MiB
# Total Installed Size:  25.12 MiB
stress-ng --cpu 4 --timeout 10s
# stress-ng: info:  [239627] setting to a 10 secs run per stressor
# stress-ng: info:  [239627] dispatching hogs: 4 cpu
# stress-ng: info:  [239627] skipped: 0
# stress-ng: info:  [239627] passed: 4: cpu (4)
# stress-ng: info:  [239627] failed: 0
# stress-ng: info:  [239627] metrics untrustworthy: 0
# stress-ng: info:  [239627] successful run completed in 10.01 secs
#
# top results while running stress-ng
#
#    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#  241934 styx      20   0   46096  10080   5044 R 100.0   0.1   0:02.07 stress-ng-cpu
#  241935 styx      20   0   46096  10080   5044 R 100.0   0.1   0:02.07 stress-ng-cpu
#  241932 styx      20   0   46096  10080   5044 R  97.9   0.1   0:02.06 stress-ng-cpu
#  241933 styx      20   0   46096  10080   5044 R  97.9   0.1   0:02.06 stress-ng-cpu
