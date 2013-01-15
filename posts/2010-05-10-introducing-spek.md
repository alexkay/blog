Title: Introducing Spek
Tags: gnome, spek

I just released version 0.1 of [Spek][] -- a little program that shows
[spectrograms][] of audio files. Spek is written in [Vala][] and uses the
standard GNOME stack: GLib, GTK+, Cairo and GStreamer.

[![Spectrogram of a FLAC file][sshot]{: .center .shrink }][sshot]

Spectrograms are used to analyse the quality of audio files, you can easily
detect lossy re-encodes, web-rips and other badness by just looking at the
spectrogram.

This version of Spek doesn't do much apart from showing the actual spectrogram
and allowing to save it as a PNG image. However, I plan to add a bunch of
features before releasing version 1.0:

* Windows port.
* Horizontal (time) and vertical (frequency) rulers.
* Zooming, scrolling and other adjustments.
* Associate Spek with audio files to use it as a viewer.
* Use multiple threads to speed-up processing.

You can download the tarball from the project's [website][Spek]. To build and
run:

```console
% tar -xjvf spek-0.1.tar.bz2
% cd spek-0.1
% ./configure
% make
% src/spek
```

Or `sudo make install` to have it installed.

### Contribute

The code is available on [Gitorious][]. I really need and will appreciate help
in these areas:

* Packaging
* Translations
* Review of autotools-related code

### Why Vala?

I initially wanted to write Spek in Haskell to practice the language after
reading [The Haskell School of Expression][] (generously sent to me by
[Jorge][]). However, after writing a bit of code I realised that all the
functional goodness of Haskell is not used at all because Spek is simply a bit
of glue between GTK+ and GStreamer, with very little code of its own. Also, the
prototype's executable size of 14+ MiB didn't help much in convincing myself
that Haskell was a good pick for this project.

I was left with C and C\#. The latter didn't feel like a good idea for the same
reasons: I wanted something lightweight for this small little app, C\# would
require a lot of dependencies. Also, while I *really* like C\# as a language and
Mono/.NET as a platform, I wanted to try something new for a change -- I already
use them full-time on my day job and when hacking [Banshee][].

I wrote very little C/C++ code since late 90's, now I know why I didn't miss it
much -- it's so incredibly verbose! After a few hours I gave up, decided to do
some research and found [Vala][] :)

The impression so far is hugely positive. Vala still has a few rough edges but
nothing too bad and not work-aroundable. If you are tired of using C for your
GTK+ applications, definitely give it a try!

  [Spek]: http://spek-project.org
  [spectrograms]: http://en.wikipedia.org/wiki/Spectrogram
  [Vala]: http://live.gnome.org/Vala
  [sshot]: |filename|/images/spek-0-1-flac.png
  [Gitorious]: http://gitorious.org/spek
  [The Haskell School of Expression]: http://www.haskell.org/soe/
  [Jorge]: http://castrojo.wordpress.com/
  [Banshee]: http://banshee-project.org/
