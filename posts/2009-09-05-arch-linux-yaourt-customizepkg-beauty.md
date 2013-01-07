Title: Arch Linux + yaourt + customizepkg = beauty!
Tags: linux

I recently switched my main desktop from Ubuntu to [Arch Linux][],
mostly for its rolling release model. I really like Ubuntu but I got
tired of dealing with lots of custom [PPAs][]. Arch Linux not only
provides the latest stable version for all packages, it also has tools
to customise the packages to your liking and selectively build them from
source.

In this post I will explain how to do it, taking as an example my pet
peeve – [the vertical Gnome panel][]. [Carey Underwood][] has recently
posted a (mostly) working [patch][], let's get it into our box.

First thing you need is to install [yaourt][] and [customizepkg][], both
are available in [AUR][]. [ArchWiki][] has a great [tutorial][] on how
to do it. Actually you only need the tutorial to install yaourt,
afterwards installing packages from AUR is as simple as running:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
$ yaourt -S customizepkg
~~~~

</div>

customizepkg allows to tweak [PKGBUILDs][]. You just add a file to
/etc/customizepkg.d/ with the same name as the package you want to
change. The file format is not well documented, but it's [pretty
intuitive][].

In our case we need to create /etc/customizepkg.d/libwnck with the
following text (in one line):

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
replace#global#cd "${srcdir}\/${pkgname}-${pkgver}"#cd "${srcdir}\/${pkgname}-${pkgver}"\nwget -O vertical.patch http:\/\/bugzilla-attachments.gnome.org\/attachment.cgi?id=140334 || return 1\npatch -Np2 -i vertical.patch || return 1
~~~~

</div>

The file will tell customizepkg to add two lines to libwnck's PKGBUILD:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
 build() {   cd "${srcdir}/${pkgname}-${pkgver}"+wget -O vertical.patch http://bugzilla-attachments.gnome.org/attachment.cgi?id=140334 || return 1+patch -Np2 -i vertical.patch || return 1   ./configure --prefix=/usr --sysconfdir=/etc                --localstatedir=/var --disable-static || return 1   make || return 1
~~~~

</div>

Then you just install the package as you always do, but using yaourt
instead of pacman:

<!-- HTML generated using hilite.me -->

<div style="overflow:auto;width:auto;color:white;background:black;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
~~~~ {style="margin:0;"}
$ yaourt -S libwnck
~~~~

</div>

Et voilà, yaourt realises that you want to build libwnck from source,
gets its PKGBUILD, changes it, and builds. When building, the patch is
downloaded and applied to the source code of libwnck before it's made.

But wait, there's more to it! Next time you upgrade the system with
\`yaourt -Syu\`, if there is a new version of libwnck, it will be
automatically patched and built from source.

Hope you find this useful, and if you haven't tried Arch yet – do it
today, you won't be disappointed ;)

  [Arch Linux]: http://www.archlinux.org/
  [PPAs]: https://launchpad.net/ubuntu/+ppas
  [the vertical Gnome panel]: http://versia.com/2008/06/08/vertical-panel-in-gnome/
  [Carey Underwood]: http://cwillu.com/
  [patch]: http://bugzilla.gnome.org/show_bug.cgi?id=86382#c132
  [yaourt]: http://aur.archlinux.org/packages.php?ID=5863
  [customizepkg]: http://aur.archlinux.org/packages.php?ID=10314
  [AUR]: http://aur.archlinux.org/
  [ArchWiki]: http://wiki.archlinux.org/index.php/Main_Page
  [tutorial]: http://wiki.archlinux.org/index.php/AUR_User_Guidelines#Installing_Packages_from_the_AUR
  [PKGBUILDs]: http://wiki.archlinux.org/index.php/PKGBUILD
  [pretty intuitive]: http://bbs.archlinux.org/viewtopic.php?id=53280
