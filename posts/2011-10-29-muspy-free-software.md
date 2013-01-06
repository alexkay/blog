Title: muspy is now free software
Tags: muspy

[![muspy][]][]

[muspy][![muspy][]] is an album release notification service, you give
it a list of your favourite artists and it sends you a notice (by email
or RSS) as soon as they have new releases.

</p>

I wrote muspy 3 years ago to scratch a personal itch -- I was spending
too much time online checking if bands I'm into have something new; but
was still missing many releases.

</p>

muspy was initially developed for Google App Engine, which was the hot
new thing back then. In retrospect, while working with App Engine was
extremely educational and a lot of fun, it wasn't a very good fit. The
recent [announcement][] on the price increase was the last straw -- I
decided to re-write it in vanilla [Django][] and to host it myself.

</p>

I'm also releasing the [source code][] under GNU AGPL in the hope that
it will be beneficial for the service and for its users.

</p>

Major changes since the previous version:

</p>

-   </p>

    Track [release groups][] instead of releases

    </p>

    This was the most frequently requested feature, there were too many
    duplicate releases for some artists, release groups make everything
    much cleaner. This change was also the reason why the new version is
    almost a complete rewrite.

    </p>
    <p>
-   </p>

    Stars are off by default for new releases

    </p>

    muspy allows to star individual releases, starred releases show up
    on top of the sorted list of releases. This feature wasn't used by
    many which resulted in all releases being starred for most users.
    Now stars are off for new releases, if you want to star, you have to
    do it manually on the website. I migrated stars only for users with
    *S \< min(R, 40) / 2*, where *S* is the number of starred releases
    and *R* is the total number of releases for all artists you follow.

    </p>
    <p>
-   </p>

    Speed

    </p>

    It used to take more than a week to check all artists for new
    releases, now the checking cycle is much shorter. Things like
    importing from Last.fm or adding a comma-separated list of artists
    should also be significantly faster.

    </p>
    <p>
-   </p>

    Blog

    </p>

    I will be blogging about muspy [here][] instead of on the website
    itself. Feel free to subscribe to the [full feed][] or just to the
    [muspy category][].

    </p>
    <p>

</p>

Other than that, muspy remains pretty much the same. I migrated all the
data but I encourage you to go the old site at [muspy.appspot.com][] and
to check if everything was migrated correctly. Please note that the old
site's background processes are not running and it will be taken down in
a month or two.

</p>

Now that muspy is free and open-source, don't hesitate to [look at the
code][source code], tweak it and suggest improvements. Git and GitHub
make it too damn easy!

</p>

And if you never used muspy before, [give it a try][![muspy][]]!

</p>

  [muspy]: http://versia.com/wp-content/uploads/2011/10/logo.gif "muspy"
  [![muspy][]]: http://muspy.com
  [announcement]: http://googleappengine.blogspot.com/2011/09/few-adjustments-to-app-engines-upcoming.html
  [Django]: https://www.djangoproject.com/
  [source code]: https://github.com/alexkay/muspy
  [release groups]: http://musicbrainz.org/doc/Release_Group
  [here]: http://versia.com
  [full feed]: http://versia.com/feed/atom/
  [muspy category]: http://versia.com/category/muspy/feed/atom/
  [muspy.appspot.com]: http://muspy.appspot.com