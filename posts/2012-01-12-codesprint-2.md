Title: CodeSprint 2
Tags: code

Last weekend [Interviewstreet][] conducted a second [CodeSprint][]. The event
had a format similar to the Google's [CodeJam][]: they gave you a bunch of
problems and you had to program your way through as many of them as you
could. There were a few differences though: the number of problems and the time
given to solve them was higher (15 and 48h), they also ran solutions on their
servers instead of just checking the output.

I managed to solve 5 problems and to rank 145th out of 1890 contestants,
spending about 12h in total during the weekend. There were a few technical
quirks in the process, but all in all I really enjoyed the sprint and was
pleasantly surprised by the quality and the complexity of the problems.

In this post I will explain how I solved those 5 problems; it's mostly for
myself, to straighten the thoughts out, as it was a bit chaotic and stressful
during the contest.

If you are interested in solutions make sure to check out the official
[CodeSprint website][CodeSprint], they should have them available in a couple of
days.

### Picking Cards

Links: [problem][p1], [solution][s1]

Sort cards by their number, then take them one by one. On step *n* the number of
ways is multiplied by the number of cards at the beginning of the deck with
*c~i~ ≤ n*. If this number is 0, it's impossible to pick up all the cards.

The brute-force approach is *O(N^2^)* and could be too slow. To speed it up, we
keep track of the last *m : c~m~ ≤ n* and start from there. As *m* is never
decreased the overall complexity is *O(N)*.

### Coin Tosses

Links: [problem][p2], [solution][s2]

On each toss we either have a head or a tail, so the expected number of
remaining tosses *T(n, m) = 1 + ½ × [T(n, m+1) + T(n, 0)]*. We could try a
dynamic programming approach, but the formula is cyclic.

However, for *m = 0* the expected number of tosses can be expressed
analytically: *T(n, 0) = 2^n+1^ - 2* ([proof][]). Add the boundary condition
*T(n, n) = 0* and memoisation, and you have a solution.

### Fraud Prevention

Links: [problem][p3], [solution][s3]

One of the company-sponsored problems. We want to normalise email and street
addresses and to keep two hashes with the combination of the normalised values
and the deal IDs as keys. For each key we keep a list of credit cards along with
order IDs. Then we process orders one by one and check all possible cases (see
the source code comments).

I found this problem a bit uninteresting for a contest -- it's tedious and, uhm,
un-algorithmic. However it would probably make a decent interview questions with
all its practicalities.

### Subsequence Weighting

Links: [problem][p4], [solution][s4]

Generalisation of the [Longest increasing subsequence][] problem. The algorithm
is very similar: take each value one by one and maintain values (and cumulative
weights) of the last elements of subsequences of certain weight. After we
process all values, the last element will have the maximal weight.

One complication is that we need a data structure with efficient insertion,
deletion, search and traversal times. One possibility is to use a red-black tree
(as implemented by std::set) and augment it so that all nodes form a
doubly-linked list. Also, unlike with the LIS algorithm, each insertion can lead
to many deletions (see lines 74-82).

With such a data structure, the running time is still at *O(n log n)*.

That was my favourite question, and the one I spent the most time on, even
though in retrospect it doesn't look all that complex.

### Quora Nearby

Links: [problem][p5], [solution][s5]

Another company-sponsored problem. A pity *N* was quite small and the
brute-force approach actually worked. Higher limits would require a clever data
structure, such as the [k-d tree][] and would make the problem much harder and
more interesting.

First we read all topics and questions and create a vector of all topics (ID and
co-ordinates) and a map of topic IDs to the lists of question IDs.

Topic queries are straight-forward: we sort topics by distance (and IDs, in case
the distance is the same) and print the first *m* IDs.

For queries it's a bit more involving: again, we sort topics by distance, then
check all associated questions using our map. The complication is that we need
to check all questions for topics with the same distance, and include those with
higher IDs.

Please never mind the code for this problem, my solution was accepted literally
5 minutes before the contest ended, as you can imagine I was a bit in a hurry.

Big thanks to the Interviewstreet team for a great weekend!

  [Interviewstreet]: http://www.interviewstreet.com/
  [CodeSprint]: http://cs2.interviewstreet.com/
  [CodeJam]: http://code.google.com/codejam/
  [p1]: http://cs2.interviewstreet.com/recruit/challenges/solve/view/4f0a70674f380/4effeea14e3a7
  [s1]: https://gist.github.com/1600348
  [p2]: http://cs2.interviewstreet.com/recruit/challenges/solve/view/4f0a70674f380/4eff8af9879d1
  [s2]: https://gist.github.com/1600579
  [proof]: http://www.qbyte.org/puzzles/p082s.html
  [p3]: http://cs2.interviewstreet.com/recruit/challenges/solve/view/4f0a70674f380/4f00b1502c006
  [s3]: https://gist.github.com/1600704
  [p4]: http://cs2.interviewstreet.com/recruit/challenges/solve/view/4f0a70674f380/4f009cfd9c541
  [s4]: https://gist.github.com/1600725
  [Longest increasing subsequence]: http://en.wikipedia.org/wiki/Longest_increasing_subsequence
  [p5]: http://cs2.interviewstreet.com/recruit/challenges/solve/view/4f0a70674f380/4f05b1d07b989
  [s5]: https://gist.github.com/1600742
  [k-d tree]: http://en.wikipedia.org/wiki/K-d_tree
