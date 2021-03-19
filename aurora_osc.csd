<Cabbage>
form caption("Untitled") size(400, 300), colour(58, 110, 182), pluginid("def1")
keyboard bounds(8, 158, 381, 95)
</Cabbage>
<CsoundSynthesizer>
<CsOptions>
-n -d -+rtmidi=NULL -M0 -m0d --midi-key-cps=4 --midi-velocity-amp=5
</CsOptions>
<CsInstruments>
; Initialize the global variables. 


sr = 44100
ksmps = 100
nchnls = 2
0dbfs = 1

gilisten OSCinit 7000

;-------- instrument to receive OSC message from python -------;
        instr   1
        
            kamp1 init 0
            kamp2 init 0
            nxtmsg:
                kcheck  OSClisten gilisten, "/osc_message_from_python1", "f", kamp1
                kcheck  OSClisten gilisten, "/osc_message_from_python2", "f", kamp2
            if (kcheck == 0) goto ex
                printk 0,kamp1
                printk 0,kamp2
            ex:     
                endin

;-------- instrument to send osc message to python ----------;

;    instr  2
;        kosc oscil 0.1, 0.0001
;        OSCsend kosc, "127.0.0.1", 8000, "/osc_message_to_python", "f", kosc
;        printk 0, kosc
;        
;        
;    endin 
</CsInstruments>
<CsScore>
f0 z
;f 1 0 1024 10 1
i 1 0 [60*60*24*7]
;i 2 0 [60*60*24*7]
</CsScore>
</CsoundSynthesizer>

        