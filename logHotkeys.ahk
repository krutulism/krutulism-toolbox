﻿#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force

; Variables ;

;  ;  ;  ;  ;

; Hotkey declarations ;
^+!Numpad1::
    run cmd.exe
    WinWait, ahk_exe cmd.exe
    Send python logEvent.py 'Exercises' 'Stretch4' -d 12 -r -1

