Title: xmonad-log-applet for GNOME and Xfce
Tags: gnome, haskell, xmonad, xla

[xmonad-log-applet][] is a handy panel applet/plugin for GNOME (and now Xfce)
users who use [Xmonad][] as an alternative window manager. The applet will show
the visible workspace(s), active window's title or anything you send its way
from your xmonad.hs.

I recently [took over][] xmonad-log-applet maintainership from Adam Wick, and
today I'm happy to announce the release of version 2.0.0.

[![xmonad-log-applet][sshot]{: .center .shrink }][sshot]

Changes since the previous release:

* Migrated the GNOME 2 applet from deprecated libbonobo API to the new
  [D-Bus based API][].
* GNOME 3 panel support (in fallback mode).
* Xfce 4 panel support.
* Revamped the build system.
* Dropped GConf dependency which was used to specify the applet width; instead
  fill all available space (like the window list applet) and ellipsise when
  necessary.
* Simplified background transparency handling.
* Fixed install locations.
* Updated sample xmonad.hs.

To install get and unpack [the tarball][] or clone
[the repo][xmonad-log-applet], then run:

```console
% ./configure --with-panel=gnome2
% make
% sudo make install
```

Substitute `gnome2` with `gnome3` or `xfce4` if that's what you use. If you
cloned the git repo, use `./autogen.sh` instead of `./configure`. After
restarting the panel you should be able to add the applet.

Use the provided [sample xmonad.hs][] file to bind it to Xmonad. It
depends on the [DBus package][], which currently doesn't compile with
GHC 7.x, but it's easy to work around:

```console
% cabal update
% cabal unpack DBus
% cd DBus-0.4
% $EDITOR DBus/Internal.hsc
```

Replace `import Control.Exception` with `import Control.OldException`, then:

```console
% cabal configure
% cabal build
% cabal install
```

After this, your xmonad.hs should compile.

EDIT: With GHC 7.4, you also need to edit `DBus/Message.hsc` and prepend
`Foreign.` to `unsafePerformIO`.

Happy Xmonading!

  [xmonad-log-applet]: https://github.com/alexkay/xmonad-log-applet
  [Xmonad]: http://xmonad.org/
  [took over]: http://uhsure.com/xmonad-log-applet.html
  [sshot]: |filename|/images/xmonad-log-applet.png
  [D-Bus based API]: http://live.gnome.org/GnomeGoals/AppletsDbusMigration
  [the tarball]: http://cloud.github.com/downloads/alexkay/xmonad-log-applet/xmonad-log-applet-2.0.0.tar.gz
  [sample xmonad.hs]: https://github.com/alexkay/xmonad-log-applet/blob/master/xmonad.hs
  [DBus package]: http://hackage.haskell.org/package/DBus
