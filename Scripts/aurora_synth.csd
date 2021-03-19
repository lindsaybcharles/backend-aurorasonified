<CsoundSynthesizer>
<CsOptions>
-odac0
-M 0
</CsOptions>
; ==============================================
<CsInstruments>

sr	=	44100
ksmps	=	1
nchnls	=	2
0dbfs	=	1

instr 1
iCps cpsmidi
k11     ctrl7 1, 11, 0, 127
k19     ctrl7 1, 19, 0, 127
printk2 k19
aTest oscil 0.1, iCps
outs aTest, aTest



endin

</CsInstruments>
; ==============================================
<CsScore>
;i1 0 60 ; Make sure to change to a high number
</CsScore>
</CsoundSynthesizer>

