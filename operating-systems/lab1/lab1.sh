# Luka, Mamrikishvili

# Task 2
ls

#❯ ls
#dir0  dir1  dir2  dir3  lab1.sh

# Task 3
man ls

#NAME
#       ls - list directory contents
#
#SYNOPSIS
#       ls [OPTION]... [FILE]...

# Task 4
info ls

#Next: dir invocation,  Up: Directory listing
#
#10.1 ‘ls’: List directory contents
#==================================
#
#The ‘ls’ program lists information about files

# Task 5
pwd
# shows current working directory

#/home/styx/uni/operating-systems

# Task 6
cd test

#uni/operating-systems on  master [?]
#❯ mkdir test
#
#uni/operating-systems on  master [?]
#❯ cd test
#
#uni/operating-systems/test on  master [?]
#❯ pwd
#/home/styx/uni/operating-systems/test

# Task 7
cd ..
# moved to the parent directory

#❯ cd ..
#
#uni/operating-systems on  master [?]
#❯ pwd
#/home/styx/uni/operating-systems

# Task 8
cd /
# moved to the root directory
# running `cd ..` wouldn't change anything

#❯ ls
#bin  boot  dev  etc  home  lib  lib64  lost+found  mnt  opt  proc  root  run  sbin  srv  swapfile  sys  tmp  usr  var

# Task 9
cd
# we stay in the same folder

# Task 10
ls > file.txt
# file list does not appear on the screen

#❯ cat files.txt | xargs
#dir0 dir1 dir2 dir3 files.txt lab1.sh test

# Task 11
less files.txt
# yes; we can also navigate through the output

# Task 12
ls -a
# all the files, including hidden files starting with '.', `.` (current directory), and `..` (parent directory)
# because we used option `-a`, that lists all the files

# .  ..  dir0  dir1  dir2  dir3  files.txt  lab1.sh  test

# Task 13
ls -l
# `-l` option lists files/directories with detailed info, like permissions, size, mod time, etc.

# total 28
#drwxr-xr-x 2 styx styx 4096 Mar  2 08:16 dir0
#drwxr-xr-x 2 styx styx 4096 Mar  2 08:16 dir1

# Task 14
mkdir data

#data  dir0  dir1  dir2  dir3  files.txt  lab1.sh  test

# Task 15
mkdir test

# Task 16
cp files.txt test/

#❯ ls test
#files.txt

# Task 17
mv files.txt data/

#❯ ls data
#files.txt

#❯ ls
#data  dir0  dir1  dir2  dir3  lab1.sh  test
# yes, it disappeared

# Task 18
rmdir test

#rmdir: failed to remove 'test': Directory not empty
# can't remove non-empty directories with just `rmdir`

# Task 19
rm test
# rm: cannot remove 'test': Is a directory
# yes, we can remove directories and it's content with rm, using `-r` or `-R` option

# Task 20
ls -lh
# `ls` with `lh` option, outputs human readable detailed info. for example, instead of 4096 -> 4.0K

#drwxr-xr-x 2 styx styx 4.0K Mar  2 09:15 data
#drwxr-xr-x 2 styx styx 4.0K Mar  2 08:16 dir0

# Task 21
ls -R
# `-R` command lists directories/files and recursively goes down the folder, listing all dirs/files

#data  dir0  dir1  dir2  dir3  lab1.sh  test
#
#./data:
#files.txt

# Task 22
mkdir -p projects/linux/scripts
# three directories were created

#❯ ls -R projects | xargs
#projects: linux projects/linux: scripts projects/linux/scripts:

# Task 23
cd projects/linux
pwd

#/home/styx/uni/operating-systems/projects/linux

# Task 24
cd ../..

#❯ pwd
#/home/styx/uni/operating-systems

# Task 25
touch notes.txt

# creates a file `notes.txt`

# Task 26
echo "Linux is powerful" >> notes.txt
# the data was appended to `notes.txt`

# Task 27
cat notes.txt
#Linux is powerful

# yes, the text from previous step is in the `notes.txt`

# Task 28
cp notes.txt projects/linux/scripts/

#❯ ls projects/linux/scripts
#notes.txt

# Task 29
mv notes.txt linux_notes.txt

#❯ ls
#data  dir0  dir1  dir2  dir3  lab1.sh  linux_notes.txt  projects  test
# yes, the file is named `notes.txt` is no longer in the directory

# Task 30
mkdir old_files

# Task 31
mv linux_notes.txt old_files

#❯ ls old_files
#linux_notes.txt

# Task 32
rm -r old_files

#❯ ls
#data  dir0  dir1  dir2  dir3  lab1.sh  projects  test

# yes, old_files was removed successfully

# Task 33
rm -i linux_notes.txt
#rm: remove regular empty file 'linux_notes.txt'? y
# `i` option invokes an interactive mode, prompting us to confirm or reject the removal of the file

# Task 34
touch fil1.txt file2.txt file3.txt

#❯ ls
#data  dir0  dir1  dir2  dir3  file1  file2.txt  file3.txt  lab1.sh  projects  test

# Task 35
rm *.txt

#❯ ls
#data  dir0  dir1  dir2  dir3  file1  lab1.sh  projects  test

# all the files ending with `.txt` was removed from the current directory; `*` means all the characters
