Title: New shuffle modes in Banshee
Author: Alexander Kojevnikov
Tags: Banshee, GNOME

![New shuffle modes][]Next version of [Banshee][] will introduce two new
shuffle modes: [by rating][] and [by score][]. In this post I will
explain how they work since the modes can be a bit confusing.

In the random shuffle mode (*aka* shuffle by song), every track has an
[equal probability][] to be selected. For example if our library
contains 1,000 tracks, each of them will be chosen with probability

<p>
> *P~t~ = 1 ÷ 1,000 = 0.001*

</p>

But what if we want some tracks to be played more often than others? Say
we have 100 favourite tracks and want to play each of them three times
as often as any other track? In probability terms this can be written as

<p>
> *P~s~ = 3 × P~t~*

</p>

where *s* are our favourite tracks and *t* – the other 900 tracks in the
library. Because the sum of all probabilities must be equal to one, we
have

<p>
> *100 × 3 × P~t~ + 900 × P~t~ = 1 → P~t~ = ^1^/~1,200~*

</p>

To chose the next track, we can pretend that our library contains 1,200
songs and pick one at random. If the track number is ≤ 100 × 3, we
randomly select one of the 100 favourite songs, otherwise we take one of
the 900 remaining songs.

If the library is partitioned into *n* slots, each containing *C~i~*
tracks, we will have

<p>
> *∑~i=1,n~ C~i~ ⋅ w~i~ ⋅ P~1~ = 1*

</p>

where *P~1~* is the probability of selecting a track from the first
partition, and *w~i~* tells how frequently tracks from the *i*-th
partition should be selected compared to the first one. That is *P~i~ =
w~i~ ⋅ P~1~*

Numbers *w~i~* are called [weights][] and by changing them we control
how often the songs from different slots are played. For example, we
could pick a number (lets call it *β*) and require that songs from the
second partition are played *β* times as often as the songs from the
first one, songs from the third *β* times as often as the songs from the
second, and so on. That is, *w~i~ = β^i-1^*

For ratings, we have 5 partitions – one for each rating. We could also
put all unrated songs into the 3-rd partition (to treat them as songs
with 3 stars) so that our entire library is partitioned. Now a good
question is what to use for *β*?

If we take *β=1*, all songs will have an equal probability to be
selected. Note that it's exactly the same as the shuffle by song mode.
If we take *β=2*, songs rated 5 will be played twice as often as songs
rated 4, and so on.

In Banshee we use *β = φ ≈ 1.61803*, also known as the [golden ratio][].
This number has an interesting property:

<p>
> *φ^n^ = φ^n-1^ + φ^n-2^*

</p>

In terms of ratings, it means that songs with 5 stars will be played as
often as songs with 4 and 3 stars combined, and so on.

In the shuffle by score mode, the songs are partitioned into 20 slots,
first slot for the songs scoring 1…5, second – for 6…10, and the last –
for scores 96…100. We also put songs with no score into the 10th slot
(46…50).

We cannot use *φ* for *β* because this time we have much more partitions
– the songs with low scores would be hardly ever played. To keep scores
behaving similar to ratings we need to scale the weights:

<p>
> *β = φ^¼^, w~i~ = φ^(i-1)/4^*

</p>

Hope that wasn't too tangled and I promise next post won't include a
single formula :)

  [New shuffle modes]: http://versia.com/wp-content/uploads/2009/09/new-shuffle-modes.png
    "New shuffle modes"
  [Banshee]: http://banshee-project.org/
  [by rating]: https://bugzilla.gnome.org/show_bug.cgi?id=544680
  [by score]: https://bugzilla.gnome.org/show_bug.cgi?id=585613
  [equal probability]: http://en.wikipedia.org/wiki/Uniform_distribution_(discrete)
  [weights]: http://en.wikipedia.org/wiki/Weight_function
  [golden ratio]: http://en.wikipedia.org/wiki/Golden_ratio
