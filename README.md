# Apple-1 Mandelbrot

Mandelbrot fractal explorer for the Apple-1

<img src="mandelbrot.png" alt="Screenshot of Mandelbrot rendered on Apple-1" style="width:75%;" />

- `mandelbrot.bas` is the Mandelbrot program written in Applesoft BASIC.
- `mandelbrot.py` is a test version in Python.

This simple Mandelbrot program works with [Applesoft Lite](https://github.com/txgx42/applesoft-lite), a version of Applesoft BASIC modified to work on the Apple-1 by Tom Greene. The Apple-1 display is limited to displaying 40x24 characters from the [Signetics 2513 character ROM](https://www.applefritter.com/files/signetics2513.pdf), so each pixel of the Mandelbrot set is plotted as a text character. The pixels are considered to be 4-bit grayscale, mapping to the following characters with increasing intensity:  ` .:,;!-^+=/&*%#@` . (This is the same mapping used in the [Apple-I 30th birthday program](https://www.applefritter.com/node/17774) originally by Dave Schmenk. I referred to [this version](https://gist.github.com/jblang/5b9e9ba7e6bbfdc64ad2a55759e401d5#file-a2apple30th-asm-L125) ported to the Apple II by J.B. Langston.)

This version runs quite slowly, taking just over 5 minutes to plot the Mandelbrot shown above! This is because Applesoft BASIC treats all numeric variables as 40-bit floating point (a representation that is emulated by the 8-bit 6502 CPU.)

A few ways to emulate Applesoft BASIC programs for the Apple-1:

- [The Apple 1js emulator](https://www.scullinsteel.com/apple1/) by Will Scullin works well in a modern web browser. Select Load > Applesoft to load Applesoft Lite from a built-in virtual tape. This takes about a minute. (Watch the red loading bar.) After loading is complete, you should see the BASIC `]` prompt where you can paste the program listing.
- [OpenEmulator](https://openemulator.github.io/) is a nice Apple-1 and Apple II emulator for macOS. Select the Apple-1 system and enable the virtual R&D CFFA1 expansion card (which adds more RAM and allows for reading/writing from a CF card). You can then open a CF disk image such as `ULTIMATE APPLE1 CFFA 3.3.po` from this [Apple I Software Archive](https://www.applefritter.com/files/2022/06/13/Apple%20I%20SoftWare%20Archive.zip), which contains a variety of programs including Applesoft Lite. Start the CFFA1 menu by entering `9000R` at the WOZ Monitor prompt, select `P` then switch to the `ASOFT` directory, then select `L` to load `APPLESOFT` into to memory at address `$6000`. Then hit `Q` to quit the CFFA1 menu and return to the WOZ Monitor prompt. You can then run Applesoft BASIC by running `6000R`. Once you see the BASIC `]` prompt you can paste the program listing here.

