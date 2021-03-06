Title: Spek 0.3 Released
Tags: gnome, spek

[Spek 0.3][] is out, just 2 days after the previous release. This version
includes the following features and fixes:

![Rulers in Spek][sshot]{: .center }

* Horizontal (time) and vertical (frequency) rulers, auto-adjustable to the
  duration and sample rate of the audio file and to the window size.
* First take on the command line arguments parsing, for now Spek understands
  only `--help` and `--version` (in addition to the usual gtk+ and gst options.)
* Open the file passed as an argument. In the future Spek will also associate
  itself with common audio formats so that you could use it as a viewer.
* Fix a crash when the window width is very small.

Spek 0.3 source code tarball and the Windows installer can be downloaded
[here][].

  [Spek 0.3]: http://spek-project.org/
  [sshot]: |filename|/images/spek-0-3-rulers.png
  [here]: http://code.google.com/p/spek/downloads/list
