Title: xmonad ⋙ metacity (mod GNOME)
Tags: gnome, haskell, xmonad

[xmonad][] is an elegantly minimalist and lightning fast window manager for
[X][] written in [Haskell][]. I wanted to play with it for a long time: I'm
using two 24" monitors and so have to spend a fair bit of time re-sizing windows
and moving them around. A [tiling window manager][] like xmonad takes care of
this; in addition you can control all aspects of window placement with the
keyboard alone.

The good news is: xmonad plays really well with GNOME. You can keep your GNOME
panels, themes, desktop backgrounds, etc – xmonad just replaces [Metacity][]
leaving everything else intact.

The bad news is: I should have tried it earlier.

A few notes about xmonad set up and usage:

*   [Recommended way][] to set up xmonad with GNOME is to `export
    WINDOW_MANAGER=xmonad` before starting gnome-session, but it didn't work for
    me. I tried every suggested place: `~/.gnomerc`, `~/.xsession`,
    `~/.profile`, `~/.xinitrc`; but none of them worked – GNOME always started
    with Metacity.

    What worked though is this:

*   Create a file in /usr/share/applications called xmonad.desktop:

```cfg
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Xmonad
Exec=/usr/bin/xmonad
NoDisplay=true
X-GNOME-WMName=Xmonad
X-GNOME-Bugzilla-Bugzilla=XMonad
X-GNOME-Bugzilla-Product=xmonad
X-GNOME-Bugzilla-Component=general
X-GNOME-Autostart-Phase=WindowManager
X-GNOME-Provides=windowmanager
X-GNOME-Autostart-Notify=true
```

*   Change this GConf key from 'metacity' to 'xmonad':

```text
/desktop/gnome/session/required_components/windowmanager
```

*   On startup, xmonad doesn't set the usual left-arrow cursor but inherits an
    ugly X cursor which looks like it was created in the eighties. To change it,
    add this line to your `~/.xinitrc` file just before you start gnome-session:

```text
xsetroot -cursor_name left_ptr
```

*   You need to create a config file in `~/.xmonad` called xmonad.hs and
    [add this][]:

```haskell
import XMonadimport XMonad.Config.Gnome main = xmonad gnomeConfig
```

*   That's right, the config file is a Haskell program that starts xmonad, which
    means it's extremely customisable.

    All keyboard short-cuts in xmonad are in the form Mod-X or Mod-Shift-X,
    where Mod is by default the Alt key. Line 7 tells xmonad to use the Win key
    – Alt is heavily used by GNOME applications:

```haskell
import XMonad
import XMonad.Config.Gnome

main = do
  xmonad $ gnomeConfig
    { terminal    = "gnome-terminal"
    , modMask     = mod4Mask
    , focusFollowsMouse = False
    , borderWidth = 2
    }
```

*   When touch-typing, some shortcuts are painful to use, Win-Shift-6 probably
    being the worst. What I wanted is to replace the Mod part with another
    shortcut, a bit in the Emacs fashion, so that instead of Win-Shift-6 I would
    have for example a sequence of Ctrl-m and Shift-6.

    mauke on \#xmonad was extremely helpful, he came up with this code which
    worked as advertised:

```haskell
import XMonad
import XMonad.Config.Gnome
import XMonad.Actions.Submap

import Control.Arrow
import Data.Bits
import qualified Data.Map as M

main :: IO ()
main = do
    xmonad $ gnomeConfig
         { terminal = "gnome-terminal"
         , focusFollowsMouse = False
         , borderWidth = 2
         , keys = addPrefix (controlMask, xK_m) (keys gnomeConfig)
         }

addPrefix p ms conf =
    M.singleton p . submap $ M.mapKeys (first chopMod) (ms conf)
    where
    mod = modMask conf
    chopMod = (.&. complement mod)
```

*   To re-load xmonad after you changed the config file just press Mod-q. It
    takes just a second to re-compile and leaves all open windows intact.

After using xmonad for 2 days I must say I'm a convert. The keyboard
[short-cuts][] feel very natural, it's not difficult to see the influence of
vi. Moving a window to another screen or to another workspace (did I mention
workspaces are per screen, which is a really neat feature), switching between
workspaces, switching windows, changing layouts, etc... is just a short-cut
away.

And as a bonus point, I now have a good reason to become more familiar with
Haskell – it's a very nice language.

  [xmonad]: http://xmonad.org/
  [X]: http://www.x.org/
  [Haskell]: http://haskell.org/
  [tiling window manager]: http://en.wikipedia.org/wiki/Tiling_window_manager
  [Metacity]: http://en.wikipedia.org/wiki/Metacity
  [Recommended way]: http://www.haskell.org/haskellwiki/Xmonad/Using_xmonad_in_Gnome
  [add this]: http://www.haskell.org/haskellwiki/Xmonad/Basic_Desktop_Environment_Integration
  [short-cuts]: http://haskell.org/haskellwiki/Image:Xmbindings.png
