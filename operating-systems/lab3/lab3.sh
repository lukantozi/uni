#!/usr/bin/env bash

# Task 1
echo "Task 1"
uname -r
# 6.19.6-arch1-1

# Task 2
echo "Task 2"
uname -a
# Linux flumenport 6.19.6-arch1-1 #1 SMP PREEMPT_DYNAMIC Wed, 04 Mar 2026 18:25:08 +0000 x86_64 GNU/Linux

# Task 3
echo "Task 3"
lsmod
# Module                  Size  Used by
# snd_seq_dummy          12288  0
# snd_hrtimer            12288  1
# snd_seq               135168  7 snd_seq_dummy

# Task 4
echo "Task 4"
sudo modprobe dummy
# command successful ->

# Task 5
echo "Task 5"
lsmod | grep "dummy"
# dummy                  16384  0
# snd_seq_dummy          12288  0
# snd_seq               135168  7 snd_seq_dummy



# Task 6
echo "Task 6"
sudo rmod dummy
# module successfully removed

# Task 7
echo "Task 7"
lsmod | grep "dummy"
# snd_seq_dummy          12288  0
# snd_seq               135168  7 snd_seq_dummy

# Task 8
echo "Task 8"
ps aux | head -n 3
# USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# root           1  0.0  0.1  23460 11684 ?        Ss   11:44   0:05 /sbin/init
# root           2  0.0  0.0      0     0 ?        S    11:44   0:00 [kthreadd]

# Task 9
echo "Task 9"
top
#     PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
#    1339 styx      20   0   12.0g 543704 154356 S   4.6   7.7   8:37.26 firefox
#  133514 styx      20   0   11508   7620   5436 R   4.6   0.1   0:00.03 top
#       1 root      20   0   23460  11684   8788 S   0.0   0.2   0:05.31 systemd
#

# Task 10
echo "Task 10"
sudo dmesg
# [    0.542396] xhci_hcd 0000:03:00.3: xHCI Host Controller
# [    0.542411] xhci_hcd 0000:03:00.3: new USB bus registered, assigned bus number 1
# [    0.542594] xhci_hcd 0000:03:00.3: hcc params 0x0270ffe5 hci version 0x110 quirks 0x0004000840000010
# [    0.543120] xhci_hcd 0000:03:00.3: xHCI Host Controller

# Task 11
echo "Task 11"
sudo dmesg | grep "USB"
# [    0.574011] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.19
# [    0.574015] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
# [    0.574231] hub 2-0:1.0: USB hub found

# Task 12
echo "Task 12"
less /var/log/syslog # journalctl on my system
# Sep 09 14:54:14 flumenport kernel: BIOS-e820: [mem 0x0000000000000000-0x0000000000086fff] usable
# Sep 09 14:54:14 flumenport kernel: BIOS-e820: [mem 0x0000000000087000-0x0000000000087fff] reserved
# Sep 09 14:54:14 flumenport kernel: BIOS-e820: [mem 0x0000000000088000-0x000000000009ffff] usable
# Sep 09 14:54:14 flumenport kernel: BIOS-e820: [mem 0x00000000000a0000-0x00000000000bffff] reserved

# Task 13
echo "Task 13"
less /var/log/syslog # journalctl on my system
# below are logs from when i set up my system
# Sep 09 14:54:14 flumenport kernel: Using GB pages for direct mapping
# Sep 09 14:54:14 flumenport kernel: Secure boot disabled
# Sep 09 14:54:14 flumenport kernel: RAMDISK: [mem 0x8ebdd000-0x91275fff]
# Sep 09 14:54:14 flumenport kernel: ACPI: Early table checksum verification disabled

# Task 14
echo "Task 14"
sudo dmesg -n 3
# command executed successfully

# Task 15
echo "Task 15"
free -h
#                total        used        free      shared  buff/cache   available
# Mem:           6.7Gi       1.4Gi       4.0Gi        55Mi       1.4Gi       5.3Gi
# Swap:          9.7Gi          0B       9.7Gi

# Task 16
echo "Task 16"
df -h
# Filesystem      Size  Used Avail Use% Mounted on
# dev             3.4G     0  3.4G   0% /dev
# run             3.4G  1.2M  3.4G   1% /run
# efivarfs        148K   95K   49K  67% /sys/firmware/efi/efivars

# Task 17
echo "Task 17"
sysctl vm.swappiness
# vm.swappiness = 60

# Task 18
echo "Task 18"
# initrd=\amd-ucode.img initrd=\initramfs-linux.img root=PARTUUID=3c19cea8-8cca-4cc8-8a52-602506723f79 rw resume=UUID=14af07e6-a3da-444c-95c6-87ce4d662525 resume_offset=1003520

# Task 19
echo "Task 19"
uptime
# 14:27:46 up 18 min,  1 user,  load average: 0.97, 0.52, 0.29

# Task 20
echo "Task 20"
uptime -p
# up 18 minutes

# Task 21
echo "Task 21"
lscpu
# Architecture:                x86_64
#   CPU op-mode(s):            32-bit, 64-bit
#   Address sizes:             43 bits physical, 48 bits virtual
#   Byte Order:                Little Endian

# Task 22
echo "Task 22"
sudo lshw
# flumenport
#     description: Notebook
#     product: NBLK-WAX9X (C178)
#     vendor: HUAWEI
#     version: M1020
#     serial: M6TPM20507000947
#     width: 64 bits
#     capabilities: smbios-3.11.1 dmi-3.11.1 smp vsyscall32

# Task 23
echo "Task 23"
iostat
# Linux 6.19.6-arch1-1 (flumenport) 	03/19/26 	_x86_64_	(8 CPU)
# 
# avg-cpu:  %user   %nice %system %iowait  %steal   %idle
#            1.69    0.00    1.69    0.09    0.00   96.54
# 
# Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
# nvme0n1          31.01      1114.86       210.98         0.00    1509953     285745          0
# zram0             0.06         1.06         0.00         0.00       1432          4          0

# Task 24
echo "Task 24"
journalctl -b
# Mar 19 14:09:48 flumenport kernel: Linux version 6.19.6-arch1-1 (linux@archlinux) (gcc (GCC) 15.2.1 20260209, GNU ld >
# Mar 19 14:09:48 flumenport kernel: Command line: initrd=\amd-ucode.img initrd=\initramfs-linux.img root=PARTUUID=3c19>
# Mar 19 14:09:48 flumenport kernel: BIOS-provided physical RAM map:
# Mar 19 14:09:48 flumenport kernel: BIOS-e820: [mem 0x0000000000000000-0x0000000000086fff] usable
