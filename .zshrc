# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  # source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi
eval "$(starship init zsh)"
setopt autocd

# If tty / no support for 256 bit colors then drop down to bash
if [ `tput colors` != "256" ]; then
  exec bash -l;
fi 
HISTFILE=~/.zsh_history
HISTSIZE=SAVEHIST=10000
setopt sharehistory
setopt extendedhistory
fpath=(~/.zsh/completion $fpath)
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

export LANG=en_US.UTF-8
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
# source ~/powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
# [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
source ~/.nvm/nvm.sh

# clear
# colorscript exec square
# figlet lohit -f mini
alias ls='exa --group-directories-first --icons'
alias ll='ls -la '
alias la='ls -a'
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
alias mkdir='mkdir -pv'
alias nvim="lvim"
alias v='lvim'
alias v.='lvim .'
alias r="ranger"
alias g='git'
alias gm='git commit -m'
alias gp="git add -p"
alias t="newtmux"
alias ta="tmux attach"
alias tl="tmux ls"
# alias tk="tmux kill-session"
alias cat="bat"
alias q="exit"
alias :q="exit"
alias python="python3"
alias lg="lazygit"
function crun {
  if [[ ! -d ./compiledcpp ]] mkdir ./compiledcpp
  clang++ ./$1.cpp -o ./compiledcpp/$1.out --std=c++20;
  ./compiledcpp/$1.out
}
function rrun {
  workingdir=$(pwd);
  if [[ $1 == "r" ]]
  then
    cargo build --release;
    ./target/release/"${workingdir##*/}"
  else
    cargo run;
  fi
}

# List tree from current directory
# lt list all file/folders in current directory
# `lt 2` goes 2 levels deep (ie all files/folder in current directory and the
# files/folder in each of those folders)
function lt {
  if [[ -z $1 ]]
  then
    ls -la -T -L=1 
  else
    ls -la -T -L=$1
  fi
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

bindkey -s ^f "newtmux\n"
bindkey -v

# pnpm
export PNPM_HOME="/Users/lohit244/Library/pnpm"
export PATH="$PNPM_HOME:$PATH"
# pnpm end

# Jump
eval "$(jump shell)"

# list tmux sessions if any exist
# echo "---  Running Sessions ---"
# if [[ $(tmux ls 2>/dev/null | wc -l) -gt 0 ]]; then
#   tmux ls
# else
#   # Start a new tmux session if none exist
#   # tmux new-session -s lohit244 -d
#   # tmux ls
# fi
# echo "--------------------------"

function starttile {
  yabai --start-service
  skhd --start-service
}

function stoptile {
  yabai --stop-service
  skhd --stop-service
}

function whyNode {
  rm -rf ./node_modules && rm -rf ./package-lock.json && npm i -D
}

export iclouddrive="/Users/lohit244/Library/Mobile Documents/com~apple~CloudDocs"

# Up or down in history based on what is aleready typed
autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search
bindkey "^[[A" up-line-or-beginning-search # Up
bindkey "^[[B" down-line-or-beginning-search # Down
export OPENAI_API_KEY=<HIDDEN>
# alias search="fzf --preview 'bat --color=always --style=numbers --line-range=:500 {}' | xargs nvim"

# function tmprev() {
#     session=$(tmux list-sessions -F "#{session_name}" 2>/dev/null |
#         fzf --exit-0 --preview='tmux_tree {} | bat --theme TwoDark --style plain')
#     echo "$session"
# }
