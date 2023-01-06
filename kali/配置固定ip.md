打开 /etc/network/interfaces

添加

auto eth0(网卡)

iface eth0 inet static 

netmask 255.255.255.0

address 内网IP

gateway 网关



service networking restart /重启network服务