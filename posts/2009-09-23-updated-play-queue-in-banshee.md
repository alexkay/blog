Title: Updated Play Queue In Banshee
Tags: Banshee, GNOME

[Banshee][] 1.6 will include an updated Play Queue extension. The
changes are already in [git master][], here are a few teaser
screen-shots:

[![Play Queue in Banshee][]][]

Played tracks are not removed from the queue but are shown as greyed
out. You can play them again if you want, drag and drop to the back of
the queue, delete, etc.

[![Play Queue Preferences][]][]

The number of played tracks to show can be changed from the preferences
dialogue.

[![Fill By option][]][]

You can also ask Banshee to automatically update the queue using any
shuffle mode (including the new [by rating and by score][] modes). The
number of upcoming tracks can also be changed in the preferences.

[![Fill From][]][]

The tracks are taken from the entire library or from any play list.

[![Refresh and Add More][]][]

If you don't like what has been added, you can refresh the upcoming
tracks. Or you can add more of them (thanks [Sandy][]!)

[![Manually added tracks][]][]

Tracks added manually are treated differently from those that had been
added automatically. When adding, they are inserted to the front of the
queue but after other manually-added tracks.

[![After refresh][]][]

Also, they are preserved when you refresh the queue.

That's about it. If you like what you saw you can [try][] the git master
version. Otherwise just wait until 1.6 is out, it shouldn't take too
long.

  [Banshee]: http://banshee-project.org/
  [git master]: http://git.gnome.org/cgit/banshee/
  [Play Queue in Banshee]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue.png
    "Play Queue in Banshee"
  [![Play Queue in Banshee][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue.png
  [Play Queue Preferences]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-preferences.png
    "Play Queue Preferences"
  [![Play Queue Preferences][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-preferences.png
  [Fill By option]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-fill-by.png
    "Fill By option"
  [![Fill By option][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-fill-by.png
  [by rating and by score]: http://versia.com/2009/09/21/new-shuffle-modes-in-banshee/
  [Fill From]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-from.png
    "Fill From"
  [![Fill From][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-from.png
  [Refresh and Add More]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-refresh.png
    "Refresh and Add More"
  [![Refresh and Add More][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-refresh.png
  [Sandy]: http://automorphic.blogspot.com/
  [Manually added tracks]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-added-tracks.png
    "Manually added tracks"
  [![Manually added tracks][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-added-tracks.png
  [After refresh]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-after-refresh.png
    "After refresh"
  [![After refresh][]]: http://versia.com/wp-content/uploads/2009/09/banshee-playqueue-after-refresh.png
  [try]: http://banshee-project.org/contribute/write-code/
