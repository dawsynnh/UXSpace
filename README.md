# UXSpace
A lightweight webserver framework with SSL support running on Python3 [PHP support using PHP Builtin]

How to use? It depends on what you want to do with it!

The base requirements for this software though are:
1. Python
2. PhP
3. Mysql

You can do some tweaking to get everything set up correctly.
You can use PHP in either CGI mode, as well as this software will automatically start a PHP built-in service if you so desire!

I do recommend creating your own SSL files instead of using these publicly shared ones, but they are just a tool to help get you on your way!
Feel free to mod this program and publish your own version of it!

The folder setup is a bit different depending on the mode you choose.
If you use CGI the web root in / 
If you use PHP built-in the web root is in index/php
And lastly if you use Vanilla HTML with no scripts then the web root is in the index folder.

These folders are in github but don't fret if you lose them!
This program will auto-generate the required folders!

I mostly made this for fun but if someone finds use in its simplicity then great! :)
