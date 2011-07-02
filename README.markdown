# PyWy

Wireless Network information in python

## Overview

This set of classes and functions parses the output of iwlist:

 *   Network() objects hold information about a single node
 *   iwlist()  object holds all of the networks and define helper methods(singleton)


## Root privileges

PyWy can't read directly from iwlist wlan0 scan right now. This is partly due to
my inherent distrust of running scripts as root, and I'm passing that paranoia
to you. If you look at the code, PyWy reads network information from a file
passed in on the command line. 

## Invocation

I use 

<pre>
$ sudo iwlist wlan0 scan > derp; python pywy.py derp; rm derp
</pre>

This prevents the python code from being executed as root. 

and to be completely honest with you I do:

<pre>
$ alias pywy='sudo iwlist wlan0 scan > derp;python pywy.py derp; rm derp
$ pywy
</pre>

Source code
-----------

The source code for this module is available online at
    http://github.com/nibalizer/pywy.git

You can checkout the source code by installing the `git` distributed version
control system and running:

    git clone git://github.com/nibalizer/pywy.git

Authors
-------

 *   Spencer Krum <krum.spencer@gmail.com>
