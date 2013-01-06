Title: GStreamer, FFmpeg and Spek
Author: Alexander Kojevnikov
Tags: GNOME, Spek

Next version of [Spek][] will use [FFmpeg][] libraries to decode audio
files. There are several reasons for the switch from [GStreamer][]:

GStreamer is a fantastic framework for building complex multimedia
pipelines, however what Spek really needs is a simple decoder and
FFmpeg's libavformat and libavcodec do just that.

To handle some audio formats (e.g. APE and DTS), GStreamer relies on
FFmpeg anyway, so the switch will result in lesser dependencies. It
doesn't matter too much on GNU/Linux, but this will reduce the size of
the Windows and Mac OS X installers.

Spek used GStreamer's [spectrum][] plugin to perform the actual spectral
analysis, with FFmpeg I had to implement it myself. The code I ended up
with is very compact and gives room for a lot of experimentation, from
using different window functions (it's still Hamming) and working on
performance optimisations to switching to a faster FFT library.

The last bit is actually done, Spek now uses [FFTW][] which in my tests
is 1.5x to 2x faster than [Kiss FFT][] used by GStreamer. Apart from
that, FFTW can scale to multiple threads with near linear performance
increase, future versions of Spek will take advantage of this.

*UPDATE: As one of commenters pointed out, FFTs on small number of
samples are not very parallelisable and my benchmarks confirm this.
Also, I switched from FFTW to [avfft][] which is built into FFmpeg. It's
a little bit faster than FFTW for my particular use case. Lastly, 1.5x
to 2x speed up was actually caused by a faster decoder, not by a faster
FFT library.*

Another thing that would be hard with GStreamer is static
cross-compilation using [mingw-cross-env][] to produce a single Windows
executable. Because FFmpeg doesn't employ a plugin architecture, static
linking is not an issue.

Last, but not least, the whole experience was very educational. I now
remember why I loved C back in the days, the trick is to not even
attempt to write any GObject code with it, that's what Vala is for. Fast
Fourier Transform and the maths behind it is much fun, and [NR][] was
very helpful here.

For the curious, the code is merged to git master and pushed to
[Gitorious][]. The next version of Spek will be released sometime in
July.

  [Spek]: http://www.spek-project.org/
  [FFmpeg]: http://ffmpeg.org/
  [GStreamer]: http://gstreamer.freedesktop.org/
  [spectrum]: http://gstreamer.freedesktop.org/data/doc/gstreamer/head/gst-plugins-good-plugins/html/gst-plugins-good-plugins-spectrum.html
  [FFTW]: http://www.fftw.org/
  [Kiss FFT]: http://kissfft.sourceforge.net/
  [avfft]: http://cekirdek.pardus.org.tr/~ismail/ffmpeg-docs/avfft_8h-source.html
  [mingw-cross-env]: http://www.nongnu.org/mingw-cross-env/
  [NR]: http://www.nrbook.com/a/bookcpdf.php
  [Gitorious]: http://gitorious.org/spek
