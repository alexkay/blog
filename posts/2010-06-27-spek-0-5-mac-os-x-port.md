Title: Spek 0.5 - Mac OS X port
Tags: GNOME, Spek

I'm happy to announce the release of version 0.5 of [Spek][], a
multi-platform acoustic spectrum analyser.

[![][]][]

Changes since the previous release:

-   Significantly speed up spectral analysis by using the optimal number
    of frequency bands.
-   DTS files support.
-   Distribute Windows version as a ZIP archive in addition to the MSI
    installer.[![Spek Logo][]][Spek]
-   Mac OS X installer.
-   Use Pango to render text.
-   Brand new icon.

</p>

This is the first version of Spek that features a Mac OS X port. All
binaries in the app bundle are compiled completely from scratch using a
[slightly modified][] version of [Aaron][]'s excellent [bockbuild][]
project (the same tool that is used to package [Banshee][] for OS X).

If your project uses the GNOME stack and you want to port it to Mac OS X
-- give bockbuild a try. Check Spek's [bundle script][] for gory
details.

  [Spek]: http://www.spek-project.org/
  []: http://versia.com/wp-content/uploads/2010/06/osx.png
    "Spek under Mac OS X"
  [![][]]: http://versia.com/wp-content/uploads/2010/06/osx.png
  [Spek Logo]: http://versia.com/wp-content/uploads/2010/06/spek-logo1.png
    "Spek Logo"
  [slightly modified]: http://github.com/alexkay/bockbuild/tree/spek
  [Aaron]: http://abock.org/
  [bockbuild]: http://github.com/abock/bockbuild
  [Banshee]: http://banshee.fm/
  [bundle script]: http://gitorious.org/spek/spek/blobs/master/bundle.sh
