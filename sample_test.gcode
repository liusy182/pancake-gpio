;PancakePainter v1.3.0-beta GCODE header start
;Originally generated @ Wed May 17 2017 18:05:51 GMT+0800 (SGT)
;Settings used to generate this file:
;----------------------------------------
;botSpeed: 4620
;flattenResolution: 2
;lineEndPreShutoff: 25
;startWait: 350
;endWait: 250
;shadeChangeWait: 15
;useLineFill: false
;useShortest: true
;shapeFillWidth: 3
;fillSpacing: 10
;fillAngle: 23
;fillGroupThreshold: 27
;useColorSpeed: false
;botColorSpeed: 6600,5280,5280,3300
;----------------------------------------
;W1 X42 Y210 L485 T0 ;Define Workspace of this file
G21 ;Set units to MM
;G1 F4620 ;Set Speed
M107 ;Pump off
G4 P1000 ;Pause for 1000 milliseconds
M84 ;Motors off
G00 X1 Y1 ;Help homing
G28 X0 Y0 ;Home All Axis
;PancakePainter header complete
;Starting stroke path #1/1, segments: 53, length: 2683, color #1
M106 ;Pump on
G4 P350 ;Pause for 350 milliseconds
G00 X20 Y0
G00 X50 Y0
G00 X200 Y0
G00 X200 Y20
G00 X200 Y100
G00 X200 Y120
;Nearing path end, moving to preshutoff position
M107 ;Pump off

G4 P250 ;Pause for 250 milliseconds
;Completed path #1/1 on color #1
;PancakePainter Footer Start
G4 P1000 ;Pause for 1000 milliseconds
G00 X1 Y1 ;Help homing
G28 X0 Y0 ;Home All Axis
M84 ;Motors off
;PancakePainter Footer Complete
