call plug#begin('~/.vim/plugged')
Plug 'davidhalter/jedi-vim'
call plug#end()

let g:python3_host_prog = '/Library/Frameworks/Python.framework/Versions/3.12/bin/python3'
let g:jedi#completions_enabled = 1
let g:jedi#show_call_signatures = 1
let g:jedi#goto_command = "<leader>d"
let g:jedi#python_command = '/Library/Frameworks/Python.framework/Versions/3.12/bin/python3'

