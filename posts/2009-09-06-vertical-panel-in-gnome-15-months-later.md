Title: Vertical panel in GNOME, 15 months later
Tags: gnome, linux

[![Fixed vertical panel][]][]

I'm happy to report that [the subject][] is mostly fixed.


**Window List**: [bgo\#86382][] has a working [patch][], it's not
perfect (read comments 140, 141 and 145) but fixes the problem.


**Notification Area**: [bgo\#531371][] also has [a patch][] which works
really well.


**Quick Launch**: My fix is included in version 2.12.6 of [the
applet][].


**Main Menu**: The ugly arrow ([bgo\#562247][] and [bgo\#564903][]) can
be removed by setting `"has-arrow"` to `FALSE` in
gnome-panel/panel-menu-button.c


**Keyboard Indicator**: [bgo\#591515][] is not yet fixed. A quick and
dirty hack is to comment out the entire switch statement in
`GSwitchitAppletUpdateAngle()` function from
gswitchit/gswitchit-applet.c


I'm using a GNOME desktop with all these fixes daily and I'm quite happy
with it. You can get my customizepkg files for [Arch Linux][] from
[GitHub][]; read how to use them in the [previous post][].


  [Fixed vertical panel]: http://versia.com/wp-content/uploads/2009/09/fixed-vertical-panel.png?w=40
    "Fixed vertical panel"
  [![Fixed vertical panel][]]: http://versia.com/wp-content/uploads/2009/09/fixed-vertical-panel.png
  [the subject]: http://versia.com/2008/06/08/vertical-panel-in-gnome/
  [bgo\#86382]: http://bugzilla.gnome.org/show_bug.cgi?id=86382
  [patch]: http://bugzilla-attachments.gnome.org/attachment.cgi?id=140334
  [bgo\#531371]: http://bugzilla.gnome.org/show_bug.cgi?id=531371
  [a patch]: http://bugzilla-attachments.gnome.org/attachment.cgi?id=140510
  [the applet]: http://quick-lounge.sourceforge.net/
  [bgo\#562247]: http://bugzilla.gnome.org/show_bug.cgi?id=562247
  [bgo\#564903]: http://bugzilla.gnome.org/show_bug.cgi?id=564903
  [bgo\#591515]: http://bugzilla.gnome.org/show_bug.cgi?id=591515
  [Arch Linux]: http://www.archlinux.org/
  [GitHub]: http://github.com/alexkay/arch/tree/master
  [previous post]: http://versia.com/2009/09/05/arch-linux-yaourt-customizepkg-beauty/
