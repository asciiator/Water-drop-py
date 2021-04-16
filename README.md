# Water Drop Photography

![](kleineKrone.jpg) 
![](SchwarzesLoch.jpg)

We will use a Raspberry Pi and a Lumix camera to take photos of waterdrops on a water surface.

## What did we use?

- Raspberry Pi 3
- Photo resistor module
- diode laser
- jumper wires
- Lumix FZ 1000
- bassin
- board of a bookshelf
- 2 small cartons
- syringe 

## Construction

![](construct.JPG) #picture

## Wiring

For the code the photo resistor module is connected to GPIO 23 (Pin 16). For the photo resistor and the laser you need a 3,3V power supply. Therefore you can connect it to Pin 1 (+3,3V) and 6 (Ground) and Pin 17 (+3,3V) and 20 (Ground).

![](wiring.png)


## Usage

Install the code on the Raspberry Pi and start it with 
```
sudo python waterdrop.py
```
You are asked how much time will be waited until the camera gets a capture command. A usfull period of time depends on the height of the light barrier and the size of the water drops.

