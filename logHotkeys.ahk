#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force

; Variables ;
venv = ./toolbox-dublin/python.exe
script = logEvent.py
;  ;  ;  ;  ;

; Hotkey declarations ;
^+!q::
    run powershell.exe
    WinWait, ahk_exe powershell.exe
    Send & %venv% %script% 'Exercises' 'Stretch200' -d 400 -r -2 `; exit {Enter}
return