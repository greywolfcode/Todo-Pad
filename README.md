# Todo Pad
Todo Pad (from the spanish "Todo" meaning all), is a macropad set up to type any Unicode charachter.
<img src=images/assembled_model.png alt="macro pad" width="600"/>

## CAD
The lid is designed to attach with a friction fit to allow it to be removed, and the case is angled at 5 degrees. 

Note that case.step has just the case models, whereas full_model.step is the assembled model with PCB.


<img src=images/exploded_view.png alt="exploded model" width="300"/>

## PCB
The PCB was designed in KiCad.
This is the schematic:


<img src=images/schematic.png alt="Schematic" width="600"/>


And here is the PCB:


<img src=images/pcb.png alt="PCB" width="600"/>

## Firmware
Todo pad is controlled using [KMK](https://github.com/KMKfw/kmk_firmware). It has functionality for Unicode and three seperate key layers. A keys.keyconfig file is used to store layouts.

### Layout Editor
The layout editor provides a way to create the keys.keyconfig files used to define the key layouts for the Todo Pad. It is not the most complicated program, but it works.


<img src=images/editor.png alt="Layout Editor" width="300"/>

## Bill of Materials
- XIAO RP2040: 1x
- Cherry MX Switches: 14x
- White DSA Keycaps: 14x
- 1N4148 Diodes: 14x
- SSD1306 0.91" 128x32 OLED Display: 1x
- PCB: 1x
- 3D Printed Case: 1x

