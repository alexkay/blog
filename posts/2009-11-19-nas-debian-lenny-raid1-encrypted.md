Title: DIY NAS with Debian Lenny
Tags: linux

After [playing with FreeNAS][] I ended up using Debian for my server.
FreeNAS is a great distribution if you want an out of the box
experience, but I found it hard to customise, mostly because I'm not
very familiar with BSDs. Also, they are [switching to Debian][] for the
next version. So, Debian it is.

This post will explain how to set up a NAS server with Debian running
essential services such as ssh, samba, nfs, cups, rdiff-backup and
rtorrent with a web interface; and using two HDDs in RAID 1 mode with
everything encrypted. It took me awhile to research all bits and pieces,
hopefully it will save you time if you are going to do a similar set up.

### Table of contents

-   [Hardware][]
-   [Partition layout][]
-   [Finalising the installation and fixing GRUB][]
-   [SSH and sudo][]
-   [Padlock modules][]
-   [NFS][]
-   [Samba][]
-   [CUPS][]
-   [rTorrent + ruTorrent][]
-   [Backup with rdiff-backup][]
-   [Performance][]
-   [Growing partitions][]
-   [A2000 tweaks][]

### Hardware

I use a [VIA ARTiGO A2000][] barebone storage server. It's powered by a
VIA C7-D processor, which has a built-in encryption engine called
[Padlock][] — quite useful for our scenario. If you are unsure which
server to get, I can highly recommend A2000.

Some parts of this walk-through are specific to A2000 or C7, but most of
it will apply to any hardware as long as it includes two HDDs and is
compatible with Lenny.

### Partition layout

I assume that you know how to use the Debian installer, if not — check
the [documentation][]. Because A2000 doesn't have a CD-ROM, I booted the
installer from a [memory stick][], you might need to do the same.

The tricky part of the installation process is disk partitioning. I used
the following layout, though there are many ways to do the set up.

First we create RAID 1 partitions. We need a separate partition for
/boot, because it won't be encrypted; and for /tmp, because it will have
encryption settings different from the root partition. This means we
will have three partitions on each disk:

-   Select FREE SPACE on **hda** and create a new partition.
-   I used 512 MB for /boot, change it to what feels sane to you.
-   Make it a primary partition at the beginning of the disk.
-   Change "Use as" from "ext3" to "physical volume for RAID".
-   Set the bootable flag.
-   Create another RAID partition on **hda** for /tmp. I used 2 GB,
    again adapt it to your needs. Don't make it bootable.
-   Create yet another RAID partition on **hda** occupying the rest of
    the disk space.
-   Do the same for **hdb**.
-   In the main partitioning menu select "Configure software RAID".
    Write changes to the partition table when it asks you to.
-   Select "Create MD device" then "RAID1". Use defaults for the number
    of active and spare devices.
-   Choose **/dev/hda1** and **/dev/hdb1**.
-   Do the same for **/dev/hda2** and **/dev/hdb2**.
-   Do the same for **/dev/hda3** and **/dev/hdb3**.

Phew, that was quite a few steps! Now you will see three RAID1 devices
in the list, let's set them up:

-   Select device \#0, change "Use as" to "ext2". Set mount point as
    /boot.
-   Select device \#1, change "Use as" to "physical volume for
    encryption". Set "Encryption key" to "Random key".  
   \* *See below for other options*
-   Select device \#2, change "Use as" to "physical volume for
    encryption". Leave "Encryption key" as "Passphrase".
-   Select "Configure encrypted volumes" and enter a passphrase. Make
    sure you use a strong one but remember that there is no way to
    recover any of your encrypted data if you lose it.

\* When creating a physical volume for encryption, you can select the
encryption algorithm and the key size. I use [AES][], because C7
provides hardware support for it; and 128 bits instead of default 256,
because I'm not paranoid. Do your research and preferably select what
your hardware supports. Software encryption is likely to be slow unless
you have a very fast CPU.

You should see two encrypted volumes now: md1\_crypt is automatically
set up to be used as swap (do it manually if it's not); md2\_crypt
however needs more tweaking.

-   Edit it and change "Use as" to "physical volume for LVM".
-   Select "Configure the Logical Volume Manager" from the main menu.
-   Create a volume group, call it something (e.g. "MAIN").
-   Select /dev/mapper/md2\_crypt device for the created group.
-   Create a logical volume for the root partition. Change its size, I
    used 10GB.
-   Create another logical volume for the data partition. Use all
    remaining space.
-   In the main menu, select LV root. Change "Use as" to "ext3" and
    "Mount point" to "/".
-   Select LV data. I formatted it with [XFS][] file system because of
    [this benchmark][], but you can select ext3 if you want.
-   When mounting, select "Enter manually" and enter "/data".

That's it! With this scheme, data and root partitions sit on top of an
LVM group, which sits on top of an encrypted volume, which sits on top
of a multi-disk volume. [Some people][] prefer to have separate
encrypted partitions for root and for data, but then you will need to
enter passphrases for each of them on start up.

### Finalising the installation and fixing GRUB

The rest of the installation should be straight-forward. When you reach
the "Software selection" screen, make sure you choose "Standard system"
and "File server"; and unselect "Desktop environment" — you are not
going to need it on a headless server. Also tick off "Print server" if
you need (I do).

After everything is installed, boot your server, type your passphrase to
unlock the encrypted partition, and login as root. Now, because the
installer writes GRUB only to the first disk, we need to install it
manually to the second. Without this, if your first disk fails you won't
be able to boot:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# grubgrub> root (hd1,0)grub> setup (hd1)grub> quit
~~~~

</div>

### SSH and sudo

Let's install SSH, otherwise we will need a spare monitor and a keyboard
connected to the server:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# aptitude update# aptitude install ssh
~~~~

</div>

Edit /etc/ssh/sshd\_config, I suggest disabling PermitRootLogin and
PasswordAuthentication and enabling PubkeyAuthentication. If you decide
to use public key authentication, add your public key to
\~/ssh/authorized\_keys. Then restart sshd, install sudo, and edit the
list of sudoers:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# /etc/init.d/ssh restart# aptitude install sudo# visudo# Add this line under root, <user> is your non-root login:<user> ALL=(ALL) ALL
~~~~

</div>

### Padlock modules

This section is specific to VIA C7 CPU. As I mentioned, it includes the
hardware encryption engine called Padlock. The engine is supported by
the Linux kernel, but the support is not enabled by default.

First make sure you have it:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# modprobe padlock_aes# modprobe padlock_sha
~~~~

</div>

If the modules load fine, [these steps][] (thanks Google Translate!)
will auto-load them:


-   Edit /etc/modprobe.d/aliases and add this line:  
   alias aes padlock\_aes
-   Edit /etc/initramfs-tools/modules and add these two lines:  
   padlock-aes  
   padlock-sha
-   Run \`update-initramfs -u\`, it should backup the image in /boot for
    you, but it never hurts to back it up manually.

These steps are needed because Padlock modules must be loaded at boot,
to work with our encrypted partitions. If they are loaded at a later
stage, the software encryption modules will not be replaced because they
are already in use.

After rebooting, check if Padlock is used. If aes\_i586 is in use
instead of padlock\_aes, you did something wrong:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# lsmod | grep -i aes
~~~~

</div>

To enable hardware encryption for SSL, edit /etc/ssl/openssl.cnf and add
this before the [new\_oids] section:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
openssl_conf = openssl_def[openssl_def]engines = openssl_engines[openssl_engines]padlock = padlock_engine[padlock_engine]default_algorithms = ALL
~~~~

</div>

After the change, observe an enormous speed bump with:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# openssl speed -evp aes-128-cbc
~~~~

</div>

### NFS

If you selected "File server" during the installation, NFS should
already be up and running. To share the entire /data partition, edit
/etc/exports and add this line:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
/data   *(rw,sync,no_subtree_check)
~~~~

</div>

Check [NFS documentation][] if you want something different. After
changing your exports, reload them with:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# exportfs -a
~~~~

</div>

On the client computers, add this line to /etc/fstab, replacing
\<server\> with the IP of your NAS:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
<server>:/data /mnt/data nfs defaults 0 0
~~~~

</div>

Then mount with \`mount -a\`. Again, check [the docs][] if you need more
control over how the NFS share is mounted.

### Samba

As with NFS, Samba should already be running on your server. Append this
to /etc/samba/smb.conf, replacing \<user\> with a non-root login on your
server:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
[data]    path = /data    browseable = yes    available = yes    public = yes    writable = yes    force user = <user>    create mask = 0644    directory mask = 0755
~~~~

</div>

Then restart Samba and you are set:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# /etc/init.d/samba restart
~~~~

</div>

Check [Samba docs][] for more options.

### CUPS

The set up heavily depends on the printer model. I have a fairly common
Epson colour ink printer, its driver is included in the gutenprint
package which gets installed if you select "Print server" during the
installation.

You will need to edit /etc/cups/cupsd.conf to make the CUPS web
interface accessible from another machine, then just add your printer
from http://:631/. Also check /etc/samba/smb.conf, it should have these
sections:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
[printers]   comment = All Printers   browseable = yes   path = /var/spool/samba   printable = yes   guest ok = yes   read only = yes   create mask = 0700[print$]   comment = Printer Drivers   path = /var/lib/samba/printers   browseable = yes   read only = yes   guest ok = no
~~~~

</div>

Check [CUPS docs][] if it doesn't work or if you want to fine-tune
permissions.

### rTorrent + ruTorrent

FreeNAS comes with [Transmission][] BitTorrent client. It looks nice but
the web interface is too simple to my taste, it doesn't even support
labels. On the desktop I used to run [Deluge][], which is great but
probably a bit heavy for a small server. After a bit of research I ended
up using [rTorrent][], which is what most blogs recommend for a headless
server.

There are [quite a few][] frontends for rTorrent, the one I liked was
[ruTorrent][], its development also seems to be the most active at the
moment. It's an almost exact rip-off of a popular Windows-based
[μTorrent][] client, hence the name.

ruTorrent requires a recent version of rTorrent *compiled with* the
XML-RPC support. The bad news is that Lenny doesn't have all packages
required to build it. This can be circumvented by temporarily switching
to testing (*aka* Squeeze), installing rTorrent's build-deps, then
switching back to Lenny. Depending on your situation, switching to
testing may not be the best idea, do it only if you are comfortable
breaking your system.

After installing build-deps, get the latest tarball of rTorrent,
./configure it with \`--with-xmlrpc-c\` option, make and make install.
Afterwards, copy an example [.rtorrent.rc][] file to \~/ and edit it to
suit your needs. Also follow the steps in the [Starting rTorrent on
System Startup][] section.

ruTorrent can work with any web server supporting PHP 5.0, I went for
[lighttpd][]. Install it from the official repo, then follow ruTorrent
[set up guide][].

The tricky part is setting up XML-RPC, there are a few contradictions in
the the rTorrent and ruTorrent docs but the following works for me™.

Add to \~/.rtorrent.rc:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
scgi_port = localhost:5000encoding_list = UTF-8
~~~~

</div>

Edit /etc/lighttpd/lighttpd.conf as [described here][]. Ignore
[instructions][] from rTorrent, they won't work. Restart rTorrent and
the web server after you are done:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# /etc/init.d/rtorrent restart# /etc/init.d/lighttpd force-reload
~~~~

</div>

### Backup with rdiff-backup

[rdiff-backup][] is such a fantastic tool: it's available on all major
platforms, it's ultra fast and efficient, it performs backups
incrementally, it can work over SSH and also it allows to restore files
at any point of time. If you don't already use it to backup your home
directories — give it a try!

On the server, there's nothing special to be done to install it. Just
get it from Debian repos and add your public keys to
\~/ssh/authorized\_keys — we are going to use SSH.

On Linux clients, invoke it like this, replacing \<user\> with your
login and \<server\> with the IP of the NAS:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
$ rdiff-backup /home/<user> <server>::/data/Backup/<user>
~~~~

</div>

On Windows clients, install [Putty][] and follow [these steps][1] to
generate a compatible key. Then invoke rdiff-backup like this:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
rdiff-backup.exe --no-hard-links --remote-schema "plink.exe -i C:Users<WinUser>privatekey.ppk %s rdiff-backup --server" C:Users<WinUser> <user>@<server>::/data/Backup/<user>
~~~~

</div>

Check [rdiff-backup docs][] for more options, there are plenty!

### Performance

Extremely unscientific tests, but they give an idea:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# bonnie++ -d /data/tmpVersion 1.03d       ------Sequential Output------ --Sequential Input- --Random-                    -Per Chr- --Block-- -Rewrite- -Per Chr- --Block-- --Seeks--Machine        Size K/sec %CP K/sec %CP K/sec %CP K/sec %CP K/sec %CP  /sec %CPserver           2G 10862  91 63699  27 29931  12 11483  91 83455  22 196.7   0                    ------Sequential Create------ --------Random Create--------                    -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--              files  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP                 16  2693  67 +++++ +++  3467  37  2948  47 +++++ +++  3131  38server,2G,10862,91,63699,27,29931,12,11483,91,83455,22,196.7,0,16,2693,67,+++++,+++,3467,37,2948,47,+++++,+++,3131,38## sync# dd if=/dev/zero bs=16384 count=131072 of=/data/tmp131072+0 records in131072+0 records out2147483648 bytes (2.1 GB) copied, 40.7823 s, 52.7 MB/s## sync# dd if=/data/tmp bs=16384 count=131072 of=/dev/null131072+0 records in131072+0 records out2147483648 bytes (2.1 GB) copied, 23.5763 s, 91.1 MB/s# hdparm -tT /dev/mapper/md2_crypt /dev/mapper/md2_crypt: Timing cached reads:   584 MB in  2.01 seconds = 291.10 MB/sec Timing buffered disk reads:  222 MB in  3.03 seconds =  73.19 MB/sec
~~~~

</div>

**hda** is a 1TB [WD Caviar Green][], **hdb** is a 640GB [Seagate
Barracuda][]. I know, using different disk models is bad for RAID 1, but
that's what I had. At some point I will get a second 1TB WD, read the
next section to find out how to grow the mirror when upgrading drives.

NFS transfers are slower, but good enough for my needs: 49 MB/sec when
reading from a NFS share and 23 MB/sec when writing to it.

### Growing partitions

When your RAID 1 mirror is filled up you probably want to upgrade the
disks with bigger ones. This can be done by replacing the first disk,
syncing the mirror, then replacing the second one, and syncing again.
After that you need to grow your data partition.

So, shut down your NAS, replace one of the drives, boot up and SSH to
it. Check the status the mirror, notice that only one drive is used:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# watch -n 2 cat /proc/mdstatPersonalities : [raid1]md2 : active raid1 hda3[0]      622679296 blocks [2/1] [U_]md1 : active raid1 hda2[0]      1951808 blocks [2/1] [U_]md0 : active raid1 hda1[0]      497856 blocks [2/1] [U_]unused devices: <none>
~~~~

</div>

Here I assume that **hda** is used and **hdb** has been replaced, run
\`fdisk -l\` to check which is which in your case. Now copy the
partition table from **hda** to **hdb**:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# sfdisk -d /dev/hda | sfdisk /dev/hdb
~~~~

</div>

Adjust the last partition on **hdb**: run \`cfdisk /dev/hdb\`, select
**hdb3** and delete it, re-create **hdb3** to use the entire free space,
change the partition type to "FD Linux raid autodetect", and finally
write changes to disk and quit.

Add new partitions to the RAID array and wait until the sync is
finished:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# mdadm --add /dev/md0 /dev/hdb1# mdadm --add /dev/md1 /dev/hdb2# mdadm --add /dev/md2 /dev/hdb3# watch -n 2 cat /proc/mdstat
~~~~

</div>

Add grub to **hdb**:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# grubgrub> root (hd1,0)grub> setup (hd1)grub> quit
~~~~

</div>

If you replaced the drive with a bigger one, you need to grow the last
partition to take advantage of all available space. Here's how to do it
(the steps are borrowed from [here][]):

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# mdadm --grow /dev/md2 --size=max
~~~~

</div>

Reboot, then run this:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# pvresize /dev/mapper/md2_crypt# vgdisplay -A | grep -i free  Free  PE / Size       X / Y GB
~~~~

</div>

Note the number <span style="color:#fb660a;font-weight:bold;">X</span>,
we will use it in the next command. Also replace
<span style="color:#fb660a;font-weight:bold;">MAIN-data</span> with the
name you used for the **/data** partition:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# lvextend -l +X /dev/mapper/MAIN-data
~~~~

</div>

Finally, grow the filesystem:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
# xfs_growfs /data
~~~~

</div>

The previous command will only work for XFS, adapt it if you use ext3 or
another file system.

### A2000 tweaks

Inspired by [this][] forum post I replaced stock A2000 fans with [Scythe
Mini Kaze SY124010L][] 40mm fan on the CPU and [Noctua NF-R8][] 80mm fan
on the rear exhaust. This made A2000 even more quiet. Other than that, I
cannot think of any other mod I would like to do, A2000 is a [very
nice][] piece of hardware.

  [playing with FreeNAS]: http://versia.com/2009/11/04/grow-encrypted-raid1-freenas/
  [switching to Debian]: http://sourceforge.net/apps/phpbb/freenas/viewtopic.php?f=5&t=3966
  [Hardware]: #hardware
  [Partition layout]: #layout
  [Finalising the installation and fixing GRUB]: #grub
  [SSH and sudo]: #ssh
  [Padlock modules]: #padlock
  [NFS]: #nfs
  [Samba]: #samba
  [CUPS]: #cups
  [rTorrent + ruTorrent]: #torrent
  [Backup with rdiff-backup]: #backup
  [Performance]: #performance
  [Growing partitions]: #grow
  [A2000 tweaks]: #a2000
  [VIA ARTiGO A2000]: http://www.via.com.tw/en/products/embedded/artigo/a2000/
  [Padlock]: http://www.via.com.tw/en/initiatives/padlock/
  [documentation]: http://www.debian.org/releases/stable/i386/
  [memory stick]: http://www.debian.org/releases/stable/i386/ch04s03.html.en
  [AES]: http://en.wikipedia.org/wiki/Advanced_Encryption_Standard
  [XFS]: http://en.wikipedia.org/wiki/XFS
  [this benchmark]: http://www.debian-administration.org/articles/388
  [Some people]: http://www.howtoforge.com/set-up-a-fully-encrypted-raid1-lvm-system
  [these steps]: http://debianforum.de/forum/viewtopic.php?p=507901
  [NFS documentation]: http://nfs.sourceforge.net/nfs-howto/ar01s03.html
  [the docs]: http://nfs.sourceforge.net/nfs-howto/ar01s04.html
  [Samba docs]: http://www.samba.org/samba/docs/
  [CUPS docs]: http://www.cups.org/documentation.php
  [Transmission]: http://www.transmissionbt.com/
  [Deluge]: http://www.deluge-torrent.org/
  [rTorrent]: http://libtorrent.rakshasa.no/
  [quite a few]: http://libtorrent.rakshasa.no/wiki/UtilsList
  [ruTorrent]: http://code.google.com/p/rutorrent/
  [μTorrent]: http://www.utorrent.com/
  [.rtorrent.rc]: http://libtorrent.rakshasa.no/browser/trunk/rtorrent/doc/rtorrent.rc#latest
  [Starting rTorrent on System Startup]: http://libtorrent.rakshasa.no/wiki/RTorrentCommonTasks#StartingrTorrentonSystemStartup
  [lighttpd]: http://www.lighttpd.net/
  [set up guide]: http://code.google.com/p/rutorrent/wiki/Main
  [described here]: http://code.google.com/p/rutorrent/wiki/WebserverSetup
  [instructions]: http://libtorrent.rakshasa.no/wiki/RTorrentXMLRPCGuide
  [rdiff-backup]: http://rdiff-backup.nongnu.org/
  [Putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/
  [1]: http://www.andremolnar.com/how_to_set_up_ssh_keys_with_putty_and_not_get_server_refused_our_key
  [rdiff-backup docs]: http://rdiff-backup.nongnu.org/docs.html
  [WD Caviar Green]: http://www.wdc.com/en/products/Products.asp?DriveID=559
  [Seagate Barracuda]: http://www.seagate.com/ww/v/index.jsp?vgnextoid=c9fec8fcbe4c9110VgnVCM100000f5ee0a0aRCRD
  [here]: http://www.howtoforge.com/set-up-a-fully-encrypted-raid1-lvm-system-p7
  [this]: http://a2000-forum.viatech.com/posts/list/9001.page
  [Scythe Mini Kaze SY124010L]: http://www.scythe-usa.com/product/acc/016/sy124010l_detail.html
  [Noctua NF-R8]: http://www.noctua.at/main.php?show=productview&products_id=9&lng=en
  [very nice]: http://www.via.com.tw/en/images/products/embedded/artigo/a2000/a2000_14.jpg
