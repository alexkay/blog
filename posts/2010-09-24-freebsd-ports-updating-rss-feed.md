Title: FreeBSD ports/UPDATING web feed
Author: Alexander Kojevnikov
Tags: FreeBSD, GNOME, Perl

Two things recently happened to me: I fell in love with FreeBSD and I
got a new job (and will be moving to Malaysia very soon!)

At the new job I will mostly be dealing with Perl and, considering it's
not the language I'm most familiar with, I was looking for a small
project to practice it.

Thus, [updating.versia.com][] was born. It's a web feed that keeps track
of the /usr/ports/UPDATING file. I personally find it much easier to use
a news reader than manually checking the file each time I want to update
my ports.

Like most Perl scripts, the one generating the feed is short, uses a lot
of CPAN modules, and is a bit ugly :) You can check it on [GitHub][].

*P.S. As requested on freebsd-ports@ I also added feeds to
head/UPDATING, stable-7/UPDATING and stable-8/UPDATING. Subscribe on
[updating.versia.com][]*

  [updating.versia.com]: http://updating.versia.com/
  [GitHub]: http://github.com/alexkay/freebsd-updating
