This is an incredibly crude yet effective solution to the kayak logic problem written in python.

The kayak logic problem is as follows:

<pre>
    k____

__k a k__

k a y a k

__k a k__

____k____
</pre>

With the following arragements of letters, how many unique ways can you spell the word "kayak" without reusing the same letter?

The code works by looping through every single letter, and progressively checking if it would fit those criteria by recursively checking the neighbors of the letters that, and checking the neighbors of the neighbors that would be a valid continuation, and so on.

There is undoubtedly a better way to do this; however, it also runs in under a second on my machine. Therefore, I see no reason to rewrite and potentially break it.