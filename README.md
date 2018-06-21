# vim youdao translater

vim youdao translater 是一个利用 [有道词典在线版](http://dict.youdao.com/) 制作的vim插件，可以帮你在 vim 中翻译单词或语句

## 安装

### 普通安装:
把所有文件拷贝到 `~/.vim/` 目录下，就可以用了。


### pathogen 安装：
如果装有 pathogen 可以 :

	cd ~/.vim/bundle
	git clone git@github.com:ianva/vim-youdao-translater.git

### Vundle 安装:
  编辑 ~/.vimrc
  ```vim
    call vundle#begin()
    ...
    ...
    + Plugin 's97712/vim-youdao-translater'
    call vundle#end()
  ```
  运行vim命令
  ```
    :w
    :source %
    :PluginInstall
  ```

###  其他
编辑 `~/.vimrc` 文件：

```vim
nmap <leader>t :Ydc<CR>
#翻译光标在在文字
nmap <leader>T :Ydcline<CR>
#翻译光标所在行
vmap <leader>t :<C-U>Ydv<CR>
翻译选择文本
```

## 如何使用

###普通模式
引导键+t 翻译光标所在文字  
引导键+T 翻译光标所在行
###选择模式 
引导键+t 翻译选择文本(单行)  
~~引导键+T 翻译选择文本(多行)~~

译文将会在编辑器底部的命令栏显示。

## TODOS
- [ ] 翻译选择文本
- [ ] 增加google翻译

## License

The MIT License (MIT)

Copyright (c) ianva



