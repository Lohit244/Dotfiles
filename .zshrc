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
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
source ~/.nvm/nvm.sh
export PATH=$PATH:/Users/lohit244/.spicetify:/Users/lohit244/Library/Application\ Support/neovim/bin

# clear
# colorscript exec square
# figlet lohit -f mini
alias ls='exa --group-directories-first --icons'
alias ll='ls -la '
alias la='ls -a'
alias lt='ls -la -T -L=2 '
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
alias mkdir='mkdir -pv'
alias v='nvim'
alias v.='nvim .'
alias r="ranger"
alias g='git'
alias gm='git commit -m'
alias gp="git add -p"
alias t="tmux"
alias ta="tmux attach"
alias tl="tmux ls"
# alias tk="tmux kill-session"
alias cat="bat"
alias q="exit"
function crun {
  if [[ ! -d ./compiledcpp ]] mkdir ./compiledcpp
  g++-12 ./$1.cpp -o ./compiledcpp/$1.out;
  ./compiledcpp/$1.out
}
if [[ -f `where code` ]]; then
  alias c="code"
fi 
if [[ -f `where code-insiders` ]]; then
  alias c="code-insiders"
fi 
# tl
# echo "attach using ta -t [session name]"
# figlet -f mini "Lohit"|lolcat -f -S 156
function gac(){
  git add .
  git commit -m "$1"
}


# pnpm
export PNPM_HOME="/Users/lohit244/Library/pnpm"
export PATH="$PNPM_HOME:$PATH"
# pnpm end

# Jump
eval "$(jump shell)"

