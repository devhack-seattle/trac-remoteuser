Literally copy-pasted from here: https://trac.edgewall.org/wiki/TracStandalone#Authenticationfortracdbehindaproxy

To use, just install it. by default it reads REMOTE_USER. to change it you can
modify the `remote_user_header` variable to point to something different.
nneeds to be lowercase and with dashes though
