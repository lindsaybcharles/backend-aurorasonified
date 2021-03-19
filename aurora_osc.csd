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

  instr   1
    kamp init 0
    kk  OSClisten gilisten, "/osc_message_sent", "f", kamp
    printk 0,kamp
    
  endin
</CsInstruments>
<CsScore>
f0 z
i 1 0 [60*60*24*7]
</CsScore>
</CsoundSynthesizer>



        