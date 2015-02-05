# pinguin

![A baby pinguin!](http://i.imgur.com/436P5JJ.jpg)

Tiny Pushbullet CLI utility. Requires 'click' and 'pushbullet.py'

    pip install click
    pip install pushbullet.py
    
For easy access, you can

    chmod +x pinguin.py
    sudo cp pinguin.py /usr/bin/pinguin
    
Pinguin looks for your [Pushbullet API token](http://pushbullet.com/account) in `~/.pb_token`. You can put it there yourself if you like; otherwise you'll be prompted for it when you first run the utility. The usage syntax is:

    pinguin [-t to set token] ["MESSAGE"] ["MESSAGE DETAIL"]

This is basically a useful tool for when you want to be notified about the end of some lengthy command line task, as in:

    # NEVER DO THIS
    rm -rf / --no-preserve-root; pinguin

Happy pinging!
    
