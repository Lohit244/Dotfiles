# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
import os
import subprocess
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile
# from libqtile.utils import guess_terminal
from libqtile import hook
num_monitors = int(subprocess.run('xrandr|grep " connected"|wc -l', shell=True, stdout=subprocess.PIPE).stdout) -1
mod = "mod4"
terminal = "kitty"



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

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

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(),desc="Spawn a command using a prompt widget"),

    # Custom Keybinds for browser
    Key([mod], "e", lazy.spawn("firefox"), desc="Launches firefox"),
    
    # Spotify
    Key([mod],"s", lazy.spawn("spotify"), desc="Launches Spotify"),

    # VSCode binding
    Key([mod],"c", lazy.spawn('code'), desc="Launches VSCode"),
    # Steam
    Key([mod],"d", lazy.spawn('steam'), desc="Launch Steam"),
    # Ranger keybind and file manager (naultilus cause i use manjaro gnome)
    Key([mod],"p", lazy.spawn(terminal + " ranger"), desc="Launches Ranger"),
    Key([mod, "shift"],"p", lazy.spawn("nautilus"), desc="Launches Nautilus"),

    # keybinds to maximize and toggle floating mode
    Key([mod],"m", lazy.layout.maximize()),
    Key([mod],"f", lazy.window.toggle_floating()),

    # Dmenu Launch
    Key(['mod4'], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="Run: ",
        dmenu_font="CaskaydiaCove Nerd Font",
        dmenu_height=24,
        dmenu_lines=2,
        ))),

    # Brightness Keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-")),
    
    #Screenshot
    Key([mod,"shift"],"s", lazy.spawn("scrot -s"), desc="Takes screenshot and saves in home"),

]

# groups = [Group(i) for i in "123456789"]
groups = [Group("1", layout="monadtall"), Group("2", layout='monadtall'), Group("3", layout='monadtall'), Group("4", layout='monadtall'), Group("5", layout='monadtall'), Group("6", layout='monadtall'), Group("7", layout='monadtall'), Group("8")]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
layouts_defaults_lohit={"border_width": 4,"margin": 24,"border_focus": "#0066CB","border_normal": "#444444"}
layouts = [
    layout.Columns(**layouts_defaults_lohit),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layouts_defaults_lohit),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font='CaskaydiaCove Nerd Font',
    fontsize=14,
    padding=4,
    margin=2,
)
extension_defaults = widget_defaults.copy()
def barCreator(screenno):
    widget_list = [
    widget.GroupBox(),
    widget.Net(background="#00A676", interface="wlo1", format="{down} ↓↑ {up}", use_bits=True, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("cinnamon-settings network")}),
    widget.WindowName(),
    widget.Systray(),
    widget.Volume(),
    widget.CurrentLayoutIcon(background="#0077B6",padding = 0,scale = 0.7),
    widget.CurrentLayout(background='#0077B6'),
    widget.CheckUpdates(no_update_string="Updates: 0", background="#B24C63"),
    widget.Battery(background="#C879FF", format='Battery: {percent: 2.0%}', low_background='#FF8369'),
    widget.Clock(format='%d-%m %a %I:%M %p', background="#59313C"),
    widget.QuickExit(background="#444444"),
    ]
    if(screenno==1):
        widget_list.pop(3)
        widget_list.pop(1)
    default_bar_lohit=top=bar.Bar(
            widget_list,
            24,
            margin=2,
            background = "#001514",
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# Set hook to run autostart.sh on login
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/lohit244/.config/qtile/autostart.sh')
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
