;===== date: 20231229 =====================
;Made by FactorianDesigns, please completely watch the related Youtube video before you try this out

G392 S0 ;turn off nozzle clog detect

M400 ; wait for buffer to clear
G92 E0 ; zero the extruder
G1 E-0.8 F1800 ; retract
G1 Z{max_layer_z + 0.5} F900 ; lower z a little
G1 X0 Y{first_layer_center_no_wipe_tower[1]} F18000 ; move to safe pos
G1 X-13.0 F3000 ; move to safe pos
{if !spiral_mode && print_sequence != "by object"}
M1002 judge_flag timelapse_record_flag
M622 J1
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M400 P100
M971 S11 C11 O0
M991 S0 P-1 ;end timelapse at safe pos
M623
{endif}

M140 S0 ; turn off bed
M106 S0 ; turn off fan
M106 P2 S0 ; turn off remote part cooling fan
M106 P3 S0 ; turn off chamber cooling fan

;G1 X27 F15000 ; wipe

; pull back filament to AMS
M620 S255
G1 X267 F15000
T255
G1 X-28.5 F18000
G1 X-48.2 F3000
G1 X-28.5 F18000
G1 X-48.2 F3000
M621 S255

M104 S0 ; turn off hotend

M400 ; wait all motion done
M17 S
M17 Z0.4 ; lower z motor current to reduce impact if there is something in the bottom
;{if (max_layer_z + 100.0) < 256}
;    G1 Z{max_layer_z + 100.0} F600
;    G1 Z{max_layer_z +98.0}
;{else}
;    G1 Z256 F600
;    G1 Z256
;{endif}
;M400 P100
;M17 R ; restore z current

M400				;wait for all print moves to be done

;===== Cool Down =======
G90   
G1 X-48 Y262 F3600 ; move to safe limit position on the left
			  
M190 S30	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here
M190 S18	;wait for bed temp, Enter your own target cooldown temperature here

M140 S0 ; turn off bed

				
;======= Cool Down Done, Start Push Off =============
; calculate a good z-pushoff height, BE CAREFUL this could be a little different for parts
; that are fragile in the top, parts below 32 mm heigth can't be pushed off using the gantry
; if your part is too small then use the extruder head for push off and comment out the line "G1 Y1 F300"
; Use the safety clear part as pushoff template and adjust the coordinates as you see fit for you part 

; Enable travel moves and look at the last layer to see what your printer is doing using this code
; YOU NEVER want any -Z values in this or the resulting sliced g-code

{if (max_layer_z ) > 41}
    G1 Z{max_layer_z - 40} F600
{else}
    G1 Z1 F600
{endif}

M400 P100											
G1 Y-0.5 F300		; very slow push off using the x gantry


;======== Push off complete, start safety clear / side push off ======
G1 Y262 F800	;move bed forward again
G1 Z1 F600		;move nozzle closer to the bed when using tall parts

G1 Y210 F2000	;move bed back a little
G1 X256 F800	;move to the right
G1 X-48	F2000	;move back to the left

G1 Y165 F2000	;move bed back a little
G1 X256 F800	;move to the right
G1 X-48	F2000	;move back to the left

G1 Y120 F2000	;move bed back a little
G1 X256 F800	;move to the right
G1 X-48	F2000	;move back to the left

G1 Y75 F2000	;move bed back a little
G1 X256 F800	;move to the right
G1 X-48	F2000	;move back to the left

G1 Y30 F2000	;move bed back a little
G1 X256 F800	;move to the right
G1 X-48	F2000	;move back to the left

G1 Y0 F2000		;move bed back a little
G1 X256 F800	;move to the right
G1 X-48	F2000	;move back to the left

G1 Y262 F2000	;push bed forward one last time

;====== Safety clear complete =======
																							
M17 R ; restore z current																											   
;G90
;G1 X-48 Y180 F3600

M220 S100  ; Reset feedrate magnitude
M201.2 K1.0 ; Reset acc magnitude
M73.2   R1.0 ;Reset left time magnitude
M1002 set_gcode_claim_speed_level : 0

;=====printer finish  sound=========
M17
M400 S1
M1006 S1
M1006 A0 B20 L100 C37 D20 M40 E42 F20 N60
M1006 A0 B10 L100 C44 D10 M60 E44 F10 N60
M1006 A0 B10 L100 C46 D10 M80 E46 F10 N80
M1006 A44 B20 L100 C39 D20 M60 E48 F20 N60
M1006 A0 B10 L100 C44 D10 M60 E44 F10 N60
M1006 A0 B10 L100 C0 D10 M60 E0 F10 N60
M1006 A0 B10 L100 C39 D10 M60 E39 F10 N60
M1006 A0 B10 L100 C0 D10 M60 E0 F10 N60
M1006 A0 B10 L100 C44 D10 M60 E44 F10 N60
M1006 A0 B10 L100 C0 D10 M60 E0 F10 N60
M1006 A0 B10 L100 C39 D10 M60 E39 F10 N60
M1006 A0 B10 L100 C0 D10 M60 E0 F10 N60
M1006 A0 B10 L100 C48 D10 M60 E44 F10 N80
M1006 A0 B10 L100 C0 D10 M60 E0 F10  N80
M1006 A44 B20 L100 C49 D20 M80 E41 F20 N80
M1006 A0 B20 L100 C0 D20 M60 E0 F20 N80
M1006 A0 B20 L100 C37 D20 M30 E37 F20 N60
M1006 W
;=====printer finish  sound=========

;M17 X0.8 Y0.8 Z0.5 ; lower motor current to 45% power
M400
M18 X Y Z

