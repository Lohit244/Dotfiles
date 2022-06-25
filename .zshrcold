# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
 if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
   source /usr/share/zsh/manjaro-zsh-prompt
 fi

setopt autocd

# If tty / no support for 256 bit colors then drop down to bash
if [ `tput colors` != "256" ]; then
  exec bash -l;
fi 

export LANG=en_US.UTF-8
#bindkey -v

# clear
# colorscript exec square
# figlet lohit -f mini

alias ohmyzsh="mate ~/.oh-my-zsh"
alias ls='exa --group-directories-first'
alias la='exa -la --icons --group-directories-first'
alias ll='exa -l --icons --group-directories-first'
alias lt='exa -la -T -L=2 --icons --group-directories-first'
alias open='xdg-open'
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
alias g='git'
alias gs='git status'
alias gm='git commit -m'
alias mkdir='mkdir -pv'
alias v='vim'
alias sv='sudo -e'
alias xclip='xclip -sel clip'
#alias emacsserv='emacs --daemon'
#alias emac='emacsclient -c -a emacs'
alias vweb='vim $(where websites)'

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
