Title: Vertical panel in GNOME
Tags: GNOME, Linux

*UPDATE 2009-09-06: Read the [follow-up post][]*

I've been playing with various desktop [GNU/Linux][] distributions last
couple of months. I'm not exactly a newbie to Linux, I have been
administering a VPS box for my [hobby project][] for several years now,
but I never managed to play with it on a desktop.

So I did. And I must say I'm very impressed. Last time I checked
([FreeBSD][] 4 back in 2000), FLOSS desktop was mostly a geek toy, these
days it *is* ready for the average user.

I will spare the overview of the [distros][] [that][] [I][] [tried][],
as well as my take on the [KDE][] vs. [GNOME][] flame war for another
post, here I want to talk about one particular annoyance that I *really*
want to see fixed.

You see, these days it's hard not to have a wide-screen monitor sitting
on your desktop. They are great for watching films and playing games but
this comes at a cost -- you end up with fewer vertical pixels.

Vertical space is much more important for most other tasks I do on the
computer, be it browsing the web, coding or writing blog posts. And the
only way to maximise it is to move the everlasting task bar sitting on
the bottom of most operating systems to the left or right of the screen.

[![Vertical layout in Vista][]][][![Vertical layout in KDE][]][]This is
how it looks like in Vista and KDE. I know it takes some getting used
to, but it's worth a few days of slight disorientation. And I'm not
[the][] [only][] [one][] who thinks so.

The vertical layout works great in XP, Vista and KDE, but not in GNOME.
I want to list here all open issues along with the links to the GNOME
[bug database][]. I guess we have all these issues because not many
GNOME developers are using the vertical layout, or even aware of the
benefits it can give them. I hope this post will help it, even if only a
little bit.

[![Vertical layout in Gnome][]][]**Window List**: The list of open
windows is arguably the most important piece of information sitting on
the panel. And the most terribly behaving in vertical layout.

First of all, the height of the window list applet is fixed, meaning the
list doesn't occupy all available vertical space.

Second, the height of the buttons that represent the open windows,
stretches to fill the entire applet. The buttons should have a fixed
height that depends on the font used in the buttons.

Third, after you open a few windows, the list splits to two columns and
becomes irresponsible to mouse clicks. This is the most annoying bug of
the three.

These issues are documented in [bug 86382][] that was open back in 2002!
The bug has a patch, but it looks like it's not perfect either.

**Notificatioin Area**: In vertical layout the notification area wastes
a lot of space by placing one icon in a row. It also uses different
sizes for different icons, some are really huge, e.g. 128x128. It should
instead use a flow layout for icons and use the same size for all of
them. This is described in [bug 531371][].

**Quick Launch**: The quick-lounge applet had a bug that made it nearly
impossible to use on a vertical panel (see [bug 531358][]). It's fixed
now in the trunk, hopefully it will be integrated into the next GNOME
release.

There are other related annoyances (see [bug 428943][] and Ubuntu idea
[\#1906][]) but I can live with them if the above issues are resolved.

  [follow-up post]: http://versia.com/2009/09/06/vertical-panel-in-gnome-15-months-later/
  [GNU/Linux]: http://www.gnu.org/
  [hobby project]: http://metaltabs.com
  [FreeBSD]: http://www.freebsd.org/
  [distros]: http://www.ubuntu.com/
  [that]: http://www.opensuse.org/
  [I]: http://fedoraproject.org/
  [tried]: http://www.mandriva.com/
  [KDE]: http://www.kde.org/
  [GNOME]: http://www.gnome.org/
  [Vertical layout in Vista]: http://versia.com/wp-content/uploads/2009/09/vista.png?w=32
    "Vertical layout in Vista"
  [![Vertical layout in Vista][]]: http://versia.com/wp-content/uploads/2009/09/vista.png
  [Vertical layout in KDE]: http://versia.com/wp-content/uploads/2009/09/kde.png?w=30
    "Vertical layout in KDE"
  [![Vertical layout in KDE][]]: http://versia.com/wp-content/uploads/2009/09/kde.png
  [the]: http://greasypc.blogspot.com/2008/05/vertical-taskbar-for-more-efficient.html
  [only]: http://www.ghacks.net/2008/04/10/why-my-taskbar-is-on-the-right-side-of-the-screen/
  [one]: http://lifehacker.com/software/windows/geek-to-live--top-windows-tweaks-158144.php
  [bug database]: http://bugzilla.gnome.org/
  [Vertical layout in Gnome]: http://versia.com/wp-content/uploads/2009/09/gnome.png?w=29
    "Vertical layout in Gnome"
  [![Vertical layout in Gnome][]]: http://versia.com/wp-content/uploads/2009/09/gnome.png
  [bug 86382]: http://bugzilla.gnome.org/show_bug.cgi?id=86382
  [bug 531371]: http://bugzilla.gnome.org/show_bug.cgi?id=531371
  [bug 531358]: http://bugzilla.gnome.org/show_bug.cgi?id=531358
  [bug 428943]: http://bugzilla.gnome.org/show_bug.cgi?id=428943
  [\#1906]: http://brainstorm.ubuntu.com/idea/1906/
