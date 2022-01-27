#!/usr/bin/env bash 

lxsession &
picom --config /home/lohit244/.config/picom/picom.conf &
nitrogen --restore &
nm-applet &
/home/lohit244/mouse.sh &
xfce4-power-manager &
xfce4-screensaver &
setxkbmap -option caps:swapescape
