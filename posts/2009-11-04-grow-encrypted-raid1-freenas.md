Title: Growing mirrored and encrypted partitions in FreeNAS
Tags: FreeNAS

*UPDATE 2009-11-19: [this post][] explains how to do the same in
Debian.*

I'm building [a small][] [NAS][] for the household. It will run
[FreeNAS][] and will be used as a file, rsync, BitTorrent and printer
server. I want it to be reliable and secure so it will have two HDDs in
RAID 1 (AKA [mirroring][]) and their content will be encrypted.

But what if in the future I will want to upgrade the drives with larger
ones? A common scenario with RAID 1 is to replace one of the disks with
the bigger one, rebuild the mirror then replace the other one and
rebuild it again. In theory it sounds like an easy process that will
keep all your data intact.

In practice however it's not, Mike explains how to do it under FreeNAS
[in his blog][]. Growing mirrored *and* encrypted drives is a bit more
complicated.

Here is how, in case you might need it:

1.  After replacing the HDD, boot your box and log into the FreeNAS web
    interface

2.  Go to Disks/Management, edit the disk you have replaced and click
    "Save". This will read the new disk's size.

3.  Go to Disks/RAID, the status will be DEGRADED which is normal. In
    Tools select the new disk, "forget" and then "insert" it. Wait until
    the rebuild process is finished.

4.  Go to Disks/Encryption, attach the disk and make sure your data is
    fine.

5.  Go to Disks/Mount Point and delete the mount.

6.  Get to the NAS console, either directly or via SSH. Things will get
    more interesting now:

    </p>

    <!-- HTML generated using hilite.me -->

    <div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
    ~~~~ {style="margin:0;"}
    # geli backup /dev/mirror/raid1 bak# geli detach /dev/mirror/raid1# geli clear /dev/mirror/raid1
    ~~~~

    </div>
    </p>

    [geli][] is the command line tool to manage encrypted storage in
    FreeNAS. *raid1* is the volume name I used, yours might be
    different. The first line saves the encrypted volume's metadata to a
    file called "bak", we will need it later.

7.  Go to Disks/RAID again, delete and re-add the RAID. Use the same
    volume name and tick the "Create and initialize RAID" check box.

8.  Now back to the terminal:

    </p>

    <!-- HTML generated using hilite.me -->

    <div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
    ~~~~ {style="margin:0;"}
    # geli restore bak /dev/mirror/raid1# geli attach /dev/mirror/raid1
    ~~~~

    </div>
    </p>

    This will restore the metadata from our backup and re-attach the
    encrypted volume

9.  Fix [the partition table][], re-create and grow the partition to
    fill the entire disk:

    </p>

    <!-- HTML generated using hilite.me -->

    <div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
    ~~~~ {style="margin:0;"}
    # gpt recover /dev/mirror/raid1.eli# gpt remove -i 1 /dev/mirror/raid1.eli# gpt add -i 1 -t ufs /dev/mirror/raid1.eli# gpt label -i 1 -l data /dev/mirror/raid1.eli# growfs /dev/mirror/raid1.elip1
    ~~~~

    </div>
    </p>

    Note that the device name ends with ".eli" – it's our encrypted
    disk.

10. Finally go to Disks/Mount Point and mount the partition.

</p>

That's it, your encrypted partition should be functional now!

*NOTE: always do your backups, I can make no guarantees that it will
work for you.*

  [this post]: http://versia.com/2009/11/19/nas-debian-lenny/
  [a small]: http://www.via.com.tw/en/products/embedded/artigo/a2000/#10
  [NAS]: http://en.wikipedia.org/wiki/Network-attached_storage
  [FreeNAS]: http://www.freenas.org/
  [mirroring]: http://en.wikipedia.org/wiki/Disk_mirroring
  [in his blog]: http://rfandip.blogspot.com/2008/12/freenas-073953-raid-1-growfs-oh-my.html
  [geli]: http://www.freebsd.org/cgi/man.cgi?query=geli&sektion=8
  [the partition table]: http://en.wikipedia.org/wiki/GUID_Partition_Table
