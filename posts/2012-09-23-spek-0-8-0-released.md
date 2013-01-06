Title: Spek 0.8.0 Released
Tags: spek

![Spek logo][logo]{: .right }
After more than a year in the baking, a [new version of Spek][Spek] is out!

This release is almost a complete rewrite driven by the switch from [GTK+][] to
[wxWidgets][] to simplify packaging and to improve integration on Windows and
Mac OS X. The switch also allowed to make a singe-exe version of Spek on
Windows, which was a frequently requested feature.

Spek now allows to change the spectral density range, which is essential when
trying to detect lossy transcodes. It also handles the low end of the density
better resulting in less noisy spectrograms.

There were also some infrastructure changes: downloads and issues have been
moved from Google Code to [GitHub][], and wiki pages with platform-specific
installation instructions have been moved to a single [INSTALL file][].

Read the [changelog][] for the full list of changes in this release.  Download
links and installation instructions are available on the [Spek homepage][Spek],
get it while it's hot!

  [logo]: |filename|/images/logo-spek.png
  [Spek]: http://spek-project.org
  [GTK+]: http://www.gtk.org/
  [wxWidgets]: http://www.wxwidgets.org/
  [GitHub]: https://github.com/alexkay/spek
  [INSTALL file]: https://github.com/alexkay/spek/blob/0.8.0/INSTALL.md
  [changelog]: https://github.com/alexkay/spek/blob/0.8.0/README.md
