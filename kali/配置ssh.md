打开 /etc/ssh/ssh_config

:set nu 可显示行号

找到 PasswordAuthentication  去掉#注释 将后面的no改为yes



打开 /etc/ssh/sshd_config

将 # PermitRootLogin prohibit-paddword 改为 PermitRootLogin yes

将 #PasswordAuthentication 去掉注释 no改为yes

退出

启动ssh start

查看ssh状态 service ssh status

查看是否开启ssh服务（需要开启22端口） netstat lnt

