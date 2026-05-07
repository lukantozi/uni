task #3:
    yes, the apperance changes after running the command `:syntax on` in the normal mode. at start the text was grey/white and then keywords where highlighted, recognizing the language syntax

task #4:
    1) shift + g

    2) `b` to go back and `e` to go to the end of the word. We can also prepend these commands with the number, and the operation will be executed that many times. For example, 5b will result in jumping back 5 words

    3) shift + V to select the line, then press `d`, and then navigate to the line you want to paste the line, and press `p`

    4) select the text you want to copy, entering the visual mode with `v`, and then press `y` to yank it into buffer, move wherever you want to paste the saved text, and then press `p`

    5) `dd` will remove the line you are on. `dl` will remove the character to the left, `dh` to the right... 
    if in visual mode and some text selected, simply pressing `d` will delete the text

    you can undo changed by pressing `u` in normal mode and redo the changes by pressing `r` also in the normal mode

    6) in normal mode, press `/` and then write the pattern you want to search for. Press enter and then `n` to find the next instance of the pattern, press shift + `n` to find the previous instance of the pattern

    7) In normal mode, enter `:s/pattern/new_pattern` to replace the first occurance. `:s/pattern/new_pattern/n` to replace nth occurance of pattern. `:s/pattern/new_pattern/g` replace all occurances in the current line. `:%s/pattern/new_pattern/g` replace all occurances in the file

    8) yes, with `dd` command in normal mode

    9) select the text while in visual mode, press `y`, and move wherever you want to paste the text and press `p` in normal mode

    10) in normal mode enter `:tabnew` do whatever you want in the the file and you can navigate between files by entering `:bn` `:bp` in normal mode to switch between them 

    you can also open files like this: `vim file1 file2 file3` and navigate through them with same commands above

    11) `:vsplit` and `:split` in normal mode. you can exit those windows and open different ones as you wish

    12) edit `.vimrc` file and add `set autoindent`, or for the current session, simply write `:set autoindent` in the normal mode

    13) `:set number`

    14) mentioned in the answer to the question *12*

    15) `:qa!`

    16) `:syntax on` for the current session, or add `syntax on` line to `.vimrc`

    17) select the block you want to move, press `d`, go to where you want the block moved, and press `p` in normal mode

    18) `:<line_number>`

    19) give writing permissions to the file with `chmod +w file`
