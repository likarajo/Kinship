# Running using Docker (for Mac)
* This is a short guide explaining how to run GUI applications from within Docker on Mac.
* This uses XQuartz to enable to set the DISPLAY variable within the container.

1. Install XQuartz
```
$ brew cask install xquartz
```

2. Restart OS
 
3. Run XQuartz
```
$ open -a XQuartz
```

4. In the XQuartz preferences, go to the Security tab and make sure you’ve got Allow connections from network clients ticked

5. Set Host Machine IP
```
$ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
```
> If you’re on wifi you may want to use en1 instead of en0, check the value of the variable using echo $IP.<br>

6. Add the IP using Xhost
```
xhost + $IP
```
> /usr/X11/bin should be in your path.

7. Run as a container
```
$ docker run -i -e DISPLAY=$IP:0 -v /tmp/.X11-unix:/tmp/.X11-unix -t likarajo/kinship
```
