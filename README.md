
# PynodeMCU robot
This is the first robot I've ever built!. It's mainly based on a NodeMCU devkit board mounted on a well-known 2WD robot chassis. The following, are the complete list of components that I've used to build it: 
- A 2WD robot chassis kit.
- A NodeMCU devkit 1.0 board. 
- An L298N based module.
- A small protoboard, that holds the NodeMCU board.
- A USB portable charger. 

On the software side, the NodeMCU board runs the Micropython firmware, which executes a script that receives simple commands, using TCP sockets (basically, it acts as a small socket server). The client, is a small web page powered by the Bottle microframework, which includes a little bit of jQuery code to communicate wirelessly with the NodeMCU board.

As evidenced by the image included in the web page, the build is quite precarious, at best!. I'm fully aware of it, so I'm trying to make improvements on that!.

Hope you like it!.
