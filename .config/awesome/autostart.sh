#!/usr/bin/env bash 

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom --config ~/.config/picom/picom.conf --experimental-backends &
nm-applet &
blueman-applet &
/home/lohit244/mouse.sh &
dunst &
autorandr -c &
touchegg & disown
