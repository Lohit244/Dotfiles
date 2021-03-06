# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

setopt autocd

# If tty / no support for 256 bit colors then drop down to bash
if [ `tput colors` != "256" ]; then
  exec bash -l;
fi 
HISTFILE=~/.zsh_history
HISTSIZE=SAVEHIST=10000
setopt sharehistory
setopt extendedhistory
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

export LANG=en_US.UTF-8
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
source /usr/share/nvm/init-nvm.sh
bindkey -e
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

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
alias r="ranger"
alias vweb="vim ~/dmenuscripts/websites"
crun(){ make "$1" && ./"$1" }
fork(){ fork|fork & }
