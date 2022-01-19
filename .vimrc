set number
set termguicolors
set autoindent
set expandtab
set tabstop=4
set shiftwidth=4
set smartcase
set mouse=a
set nobackup
set linebreak
call plug#begin("~/.vim/plugged")
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
Plug 'junegunn/vim-easy-align'

Plug 'whatyouhide/vim-gotham'

Plug 'ap/vim-css-color'

Plug 'itchyny/lightline.vim'

" Initialize plugin system
call plug#end()

set laststatus=2
colorscheme gotham
let g:lightline = {
      \ 'colorscheme': 'gotham',
      \ }
let &t_ut=''
