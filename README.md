# pinguin
Tiny Pushbullet CLI utility. Requires 'click' and 'pushbullet.py'

    pip install click
    pip install pushbullet.py
    
You'll also need to find your [Pushbullet API token](http://pushbullet.com/account). Then you can

    cp pinguin.py /usr/bin/pinguin
    
The usage syntax is:

    pinguin [-t to set token] "MESSAGE" ["MESSAGE DETAIL"]

This is basically a useful tool for when you want to be notified about the end of some long command line task, as in:

    # NEVER DO THIS
    rm -rf / --no-preserve-root; pinguin

Happy pinging!
    
