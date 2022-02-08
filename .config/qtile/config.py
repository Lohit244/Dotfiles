from typing import List  # noqa: F401
import os
import subprocess
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile
from libqtile import hook
# ----------------->       Monitor and apps      <---------------------
num_monitors = int(subprocess.run('xrandr|grep " connected"|wc -l', shell=True, stdout=subprocess.PIPE).stdout) -1
mod = "mod4"
user = "lohit244"
terminal = "kitty"
if num_monitors == 2:
    monitor = os.path.expanduser('/home/{}/monitor-setup.sh'.format(user))
    subprocess.run([monitor]) 
elif num_monitors == 1:
    monitor = os.path.expanduser('/home/{}/laptop-setup.sh'.format(user))
    subprocess.run([monitor])
# ----------------->     Keys          <--------------------
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(),desc="Spawn a command using a prompt widget"), # The default qtile run prompt

    # Custom Keybinds for browser
    Key([mod], "w", lazy.spawn("/home/{}/dmenuscripts/websites".format(user)), desc="Launches Common Websites script"),
    Key([mod,"shift"], "w", lazy.spawn("qutebrowser"), desc="Launches Qutebrowser"),

    # Lock Screen
    Key([mod,"shift"],"g",lazy.spawn("xfce4-screensaver-command -l"), desc="Locks the screen"),

    # Spotify
    Key([mod],"s", lazy.spawn("spotify"), desc="Launches Spotify"),

    Key([mod],"c", lazy.spawn('code'), desc="Launches VSCode"),

    # Steam etc
    Key([mod, "shift"],"d", lazy.spawn('steam'), desc="Launch Steam"),
    
    Key([mod], 'e', lazy.spawn('emacsclient -c -a emacs'), desc="Launch emacs"),

    Key([mod, "shift"],"z", lazy.spawn('Discord'), desc="Launch Discord"),

    # Notes
    Key([mod],"x", lazy.spawn('notes'), desc="Launch Notes Script"),
    Key([mod, "shift"],"x", lazy.spawn('obsidian'), desc="Launch Obsidian"),


    # Ranger keybind and file manager (naultilus cause i use manjaro gnome)
    Key([mod],"p", lazy.spawn(terminal + " ranger"), desc="Launches Ranger"),
    Key([mod, "shift"],"p", lazy.spawn("thunar"), desc="Launches Thunar"),

    # keybinds to maximize and toggle floating mode
    # Key([mod],"m", lazy.layout.maximize()),
    Key([mod],"o", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod],"i", lazy.layout.grow(), desc="Grow window"),
    Key([mod],"f", lazy.window.toggle_floating(), desc="Toggle Floating Mode for selected window"),

    # Rofi
    Key([mod],"r",lazy.spawn("rofi -show run")),
    Key([mod,"shift"],"r",lazy.spawn("rofi -show window")),
    Key([mod],"m",lazy.spawn("rofi -show emoji")),

    # Brightness Keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-")),

    # Sound Keys
    Key([], 'XF86AudioRaiseVolume', lazy.spawn("amixer -q -D pulse set Master 5%+")),
    Key([], 'XF86AudioLowerVolume', lazy.spawn("amixer -q -D pulse set Master 5%-")), 

    # Screenshot
    Key([mod,"shift"],"s", lazy.spawn("scrot -s /home/{}/Pictures/Screenshots/%b%d%H%M%S.png".format(user)), desc="Takes screenshot"),

    # Dmenu Launch
#   Key([mod], "r", lazy.run_extension(extension.DmenuRun(command="-z",dmenu_prompt="Run: ",dmenu_font="CaskaydiaCove Nerd Font",dmenu_height=24,dmenu_lines=10,background="#001514",dmenu_ignorecase=True,selected_background="#5B5F97",))),
#   Key([mod, "shift"], "r", lazy.run_extension(extension.WindowList(command="-z",dmenu_prompt="Switch To: ",dmenu_font="CaskaydiaCove Nerd Font",dmenu_height=24,dmenu_lines=10,background="#001514",selected_background="#5B5F97",dmenu_ignorecase=True,))),
]
#-------------------->         colors             <------------------------
colors = [
    "#FCFAFA",  #White            |0
    "#B74F6F",  #Rose             |1
    "#2191FB",  #Blue             |2
    "#29335C",  #Dark-Blue        |3
    "#F3A712",  #Yellow           |4
    "#260C1A",  #Brown            |5
    "#3E000C",  #Lighter-Brown    |6
    "#0CCA4A",  #Green            |7
    "#080708",  #Black            |8
    "#114B5F",  #Greenish-Blue    |9
    "#AC3931",  #Bright Brown     |10
    "#9B5DE5",  #Purple           |11
    "#F15BB5",  #Pink             |12
    "#2F0147",  #Purple           |13
    "#2A4D14",  #Deep Green       |14

]
# ------------------------>             Groups               <-------------------------
groups = [Group("1", layout="monadtall"), Group("2", layout='monadtall'), Group("3", layout='monadtall'), Group("4", layout='monadtall'), Group("5", layout='monadtall'), Group("6", layout='monadtall'),
Group("7", layout='monadtall'), Group("8", layout="monadtall"),Group("9", layout="monadtall"),Group("0", layout="monadtall"),]

for i in range(0,10):
    keys.extend([
        Key([mod], str((i+1)%10), lazy.group[groups[i].name].toscreen(),
            desc="Switch to group {}".format(groups[i].name)),

        Key([mod, "shift"], str((i+1)%10), lazy.window.togroup(groups[i].name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(groups[i].name)),
    ])

# ---------------------------->           LAYOUTS            <---------------------

layouts_defaults_lohit={"border_width": 3,"margin": 5,"border_focus": colors[2],"border_normal":colors[3]}
layouts = [
    layout.Columns(**layouts_defaults_lohit),
    layout.Max(**layouts_defaults_lohit),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layouts_defaults_lohit),
    layout.MonadWide(**layouts_defaults_lohit),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(**layouts_defaults_lohit, font="CaskaydiaCove Nerd Font", active_bg=colors[2],place_right=True),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# ---------------------->           WIDGETS            <--------------------------

widget_defaults = dict(
    font='CaskaydiaCove Nerd Font',
    fontsize=14,
)
extension_defaults = widget_defaults.copy()
def barCreator(screenno):
    widget_list = [
    #0
    widget.CurrentLayout(background=colors[3]),
    #1
    widget.CurrentLayoutIcon(background=colors[3],padding = 0,scale = 0.7),
    #2
    widget.GroupBox(inactive=colors[6], active=colors[0], hide_unused=True,highlight_method="line",highlight_color=[colors[3],colors[2]]),
    #3
    widget.WindowName(empty_group_string="Hello Lohit"),
    #4
    widget.Systray(),
    #5
    widget.Volume(fmt="   {} ",mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")}, background=colors[10]),
    #6
    widget.CPU(mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal+" btop")}, background=colors[2], format=": {load_percent}%"),
    #7
    widget.Net(background=colors[4], interface="wlo1", format="↓{down}", use_bits=True, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("nm-connection-editor")}),
    #8
    widget.Memory(mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " btop")}, background=colors[7],format=':{MemUsed: .0f}{mm}',),
    #9
    widget.CheckUpdates(no_update_string=" ﮮ ", background=colors[1],display_format="{updates}: ﮮ " ,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " sudo pacman -Syu")}),
    #10 59313C
    widget.Battery(background=colors[14], format='Battery: {percent: 2.0%}', notify_below=20 , low_background='#FF8369'),
    #11
    widget.Clock(format='%a %d/%m %I:%M%p', background=colors[13]),
    ]
    if(screenno==1):
        widget_list.pop(9)
        widget_list.pop(4)
    default_bar_lohit=top=bar.Bar(
            widget_list,
            28,
            margin=0,
            # background = "#151514", # Darker Background
            # background = "#1e1e1e", # Gray Background
            background = "#000000", # Gray Background
            # background="#00000020",  # Transparent Background
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        )
    return default_bar_lohit
screens = [Screen(barCreator(i)) for i in range(0,num_monitors)]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# ------------------------>            FLOATING RULES             <------------------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='nitrogen'),  # Nitrogen - wallpaper setter
    Match(wm_class='galculator'),  # calculator
], **layouts_defaults_lohit)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# Set hook to run autostart.sh on login
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/{}/.config/qtile/autostart.sh'.format(user))
    subprocess.run([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
