set number relativenumber
set termguicolors
set autoindent
set incsearch
set expandtab
set tabstop=4
set shiftwidth=4
set ignorecase
set smartcase
set mouse=a
set nobackup
set linebreak
set smartindent
set wildmenu
set encoding=utf-8
set nocompatible
filetype plugin on
syntax on
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

Plug 'neoclide/coc.nvim'

Plug 'ap/vim-css-color'

Plug 'itchyny/lightline.vim'

" Initialize plugin system
call plug#end()
let mapleader= " "
set guifont="CaskaydiaCove Nerd Font"
set laststatus=2
map <leader>n ni

" ----------- Gotham Color Theme ------------
colorscheme gotham
let g:lightline = { 'colorscheme': 'gotham' }


" --------- Everforest Color Theme -----------
" colorscheme everforest
" set background=dark
" let g:everforest_better_performance = 1
" let g:lightline = {'colorscheme' : 'everforest'}
" let g:everforest_background = 'hard'
" let g:minimap_auto_start=1


" vim hardcodes background color erase even if the terminfo file does
" not contain bce (not to mention that libvte based terminals
" incorrectly contain bce in their terminfo files). This causes
" incorrect background rendering when using a color theme with a
" background color.
let &t_ut=''
