# sublime-text-3_LineByteSort
sublime 按行字节数排序
==========

  Windows: %APPDATA%Sublime Text 3
  OS X: ~/Library/Application Support/Sublime Text 3
  Linux: ~/.config/sublime-text-3

1、命令运行
--------
  将文件放在packages下面
  然后打开控制台【视图->显示控制台】 然后
```Python
view.run_command('linebytesort')
```
2、右键菜单
--------
  可以修改packages下Context.sublime-menu文件 添加 右键菜单
```Json
{ "command": "linebytesort", "caption": "按字节数排序" },
```

3、自行添加各种菜单已经快捷键
------
  


