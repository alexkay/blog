Title: Faster Fast Fourier Transform
Tags: spek

![Spek logo][logo]{: .right }
[Spek][spek] is already pretty fast at analyzing audio files and creating their
spectrograms. Apparently, it can be made even faster!

A sizable chunk of processing time is spent calculating discrete Fourier
transforms of audio samples. In this post I'm going to explore a few DFT
libraries and compare their performance to what Spek is currently using.

This won't be a comprehensive overview of all available libraries. I'm going to
benchmark only what Spek needs:

* Relatively small, power of 2 transform sizes. The default size in Spek is
  2^11^, this will be adjustable in the future, but not by much.

* Single precision floating point numbers. 24-bit significand is enough when
  working with audio samples.

* Only one-dimensional forward real transforms.

* Last but not least, the DFT library should be free software, actively
  maintained, fairly popular and multi-platform.

The list of candidates is surprisingly short:

* avfft, which is part of the [FFmpeg][ffmpeg] project. This is what Spek uses.

* [FFTW][fftw]. Probably the most respectable FFT library of all. Supports both
  in-place and out-of-place transforms.

* [djbfft][] by Dr. Bernstein of daemontools fame. It's not as performance tuned
  as the other two (e.g. it doesn't use SIMD instructions), but I want to see
  how it fares against them.

The test setup is straightforward (the code is on [GitHub][fft-bench] in case
you're curious):

* Generate pseudo-random single-precision floating point samples. The number of
  samples corresponds to 10 minutes of signal at standard 44.1 kHz sampling
  rate.

* For all libraries and for all transform sizes from 2^9^ to 2^13^ run
  non-overlapping FFTs for the entire signal.

* Measure wall clock time only for FFTs (exclude sample generation and library
  initialization), take 5 measurements for every combination, report the
  fastest.

Results:

![fft-bench-results][]{: .center }

As expected, djbfft is the slowest, using SIMD instructions does make things
faster. I am however surprised how fast the FFTW is compared to avfft
(approximately 60% faster!)

Conclusion: Next version of Spek will switch to FFTW.

  [logo]: |filename|/images/logo-spek.png
  [spek]: http://spek.cc/
  [ffmpeg]: http://ffmpeg.org/
  [fftw]: http://www.fftw.org/
  [djbfft]: http://cr.yp.to/djbfft.html
  [fft-bench]: https://github.com/alexkay/fft-bench
  [fft-bench-results]: |filename|/images/fft-bench-results.png
