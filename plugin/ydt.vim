let s:translator_file = expand('<sfile>:p:h') . "/../yd.py"
let s:translator = {'stdout_buffered': v:true, 'stderr_buffered': v:true}

function! s:translator.on_stdout(jobid, data, event)
    if !empty(a:data) | echo join(a:data) | endif
endfunction
let s:translator.on_stderr = function(s:translator.on_stdout)

function! s:translator.start(lines, multiline)
    let python_cmd = ydt#GetAvailablePythonCmd()
    if empty(python_cmd)
        echoerr "[YouDaoTranslator] [Error]: Python package neeeds to be installed!"
        return -1
    endif

    let cmd = printf("%s %s %s", python_cmd, s:translator_file, a:lines)
    if exists('*jobstart')
        return jobstart(cmd, self)
    elseif exists('*job_start') && ! has("gui_macvim")
        if a:multiline
          echo "\n"
        endif
        return job_start(cmd, {'out_cb': "ydt#VimOutCallback"})
    else
        echo system(cmd)
    endif
endfunction

function! s:YoudaoVisualTranslate()
    call s:translator.start(ydt#GetVisualSelection(), 0)
endfunction

function! s:YoudaoCursorTranslate()
    call s:translator.start(expand("<cword>"), 0)
endfunction
function! s:YoudaoCursorTranslateLine()
    call s:translator.start(getline("."), 1)
endfunction

function! s:YoudaoEnterTranslate()
    let word = input("Please enter the word: ")
    redraw!
    call s:translator.start(word, 0)
endfunction

command! Ydv call <SID>YoudaoVisualTranslate()
command! Yde call <SID>YoudaoEnterTranslate()
command! Ydc call <SID>YoudaoCursorTranslate()
command! Ydcline call <SID>YoudaoCursorTranslateLine()
