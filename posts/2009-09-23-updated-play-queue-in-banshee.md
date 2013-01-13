Title: Updated Play Queue In Banshee
Tags: banshee, gnome

[Banshee][] 1.6 will include an updated Play Queue extension. The changes are
already in [git master][], here are a few teaser screen-shots:

[![Play Queue in Banshee][banshee-playqueue]{: .center .shrink }][banshee-playqueue]

Played tracks are not removed from the queue but are shown as greyed out. You
can play them again if you want, drag and drop to the back of the queue, delete,
etc.

![Play Queue Preferences][banshee-playqueue-preferences]{: .center }

The number of played tracks to show can be changed from the preferences
dialogue.

![Fill By option][banshee-playqueue-fill-by]{: .center }

You can also ask Banshee to automatically update the queue using any shuffle
mode (including the new [by rating and by score][] modes). The number of
upcoming tracks can also be changed in the preferences.

![Fill From][banshee-playqueue-from]{: .center }

The tracks are taken from the entire library or from any play list.

![Refresh and Add More][banshee-playqueue-refresh]{: .center }

If you don't like what has been added, you can refresh the upcoming tracks. Or
you can add more of them (thanks [Sandy][]!)

![Manually added tracks][banshee-playqueue-added-tracks]{: .center }

Tracks added manually are treated differently from those that had been added
automatically. When adding, they are inserted to the front of the queue but
after other manually-added tracks.

![After refresh][banshee-playqueue-after-refresh]{: .center }

Also, they are preserved when you refresh the queue.

That's about it. If you like what you saw you can [try][] the git master
version. Otherwise just wait until 1.6 is out, it shouldn't take too long.

  [Banshee]: http://banshee-project.org/
  [git master]: http://git.gnome.org/cgit/banshee/
  [banshee-playqueue]: |filename|/images/banshee-playqueue.png
  [banshee-playqueue-preferences]: |filename|/images/banshee-playqueue-preferences.png
  [banshee-playqueue-fill-by]: |filename|/images/banshee-playqueue-fill-by.png
  [by rating and by score]: |filename|/2009-09-21-new-shuffle-modes-in-banshee.md
  [banshee-playqueue-from]: |filename|/images/banshee-playqueue-from.png
  [banshee-playqueue-refresh]: |filename|/images/banshee-playqueue-refresh.png
  [Sandy]: http://automorphic.blogspot.com/
  [banshee-playqueue-added-tracks]: |filename|/images/banshee-playqueue-added-tracks.png
  [banshee-playqueue-after-refresh]: |filename|/images/banshee-playqueue-after-refresh.png
  [try]: http://banshee-project.org/contribute/write-code/
