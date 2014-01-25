Trapifier.py
============

This is a script for turning boring, regular sound files into CERTIFIED TRAP BANGERS by overdubbing a variety of samples.  Have you ever wished that boring old Sufjan Stevens track had about 500% more foghorn?  Consider your wish granted.

Example
-------

Original: https://www.youtube.com/watch?v=W6H8WcTPnWM

Trapified: https://soundcloud.com/japesinator/trapified  <- Temporarily taken down for "plagiarism"

Requirements
------------

This program uses python, so make sure you have that installed.  Pretty much any version should work.  It also uses [pydub](http://pydub.com/) for most of the audio processing.  `pip install pydub` works, and so does cloning the git repository.

I don't think this will work on Windows.  I do not actually have a Windows box to test on at this moment.  If you can confirm whether or not it works, please let me know.  If you can fork the repo and make it work for Windows, that would be really cool.

Installation
------------

Clone the repository and then run trapifier.py.

Usage
-----

Run trapifier.py <inputfile> <outputfile>, where <inputfile> is song to be converted, and <outputfile> is desired title of the created track.  You can also add --samples <directory> to use samples from that directory.

TODO
----

*   Make samples context-sensitive, so they sync up better than random with the music

*   Allow installation via pip

*   Make things work on Windows

Acknowledgements
----------------

This program was inspired by [this reddit thread](http://www.reddit.com/r/hiphopheads/comments/1vxdag/guys_i_need_a_favor/).  The samples used are from [this person on reddit](http://www.reddit.com/r/DJs/comments/1vhaez/sample_pack_not_sure_if_anyone_is_interested_but/).

License
-------

This program is MIT licensed.

Copyright (c) 2014, JP Smith, japesinator.github.io

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
