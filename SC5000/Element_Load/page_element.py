"""
用来存放每个页面的元素，比如登录页面的用户、密码及登录按钮的元素
"""

# 登录页面元素
Password_element = "/html/body/div/div/section/form/div[1]/div/div[1]/input"  # 密码框
Login_button = "//button[./span[text()='登录 ']]"    # 登录按钮
#基础设置——WIFI页面元素
two_SSID = "/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/input"#2.4g ssid
two_conntect="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[4]/div/div/div[1]/input"#2.4g 连接数
two_status="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[1]/div/div/span[2]/span"#2.4g 状态
two_pwd = "/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[3]/div/div/input"#2.4g 密码
two_hide="/html/body/div[1]/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[2]/div/div[2]/div/div/label/span[1]/span"#2.4g 隐藏
five_SSID = "/html/body/div/section/section/section/main/div[1]/form/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/input"#5g ssid
five_conntect="/html/body/div/section/section/section/main/div[1]/form/div[3]/div[2]/div/div[1]/div/div/span[2]/span"#5g 连接数
five_status="/html/body/div/section/section/section/main/div[1]/form/div[3]/div[2]/div/div[1]/div/div/span[2]/span"#5g 状态
five_SSID="/html/body/div/section/section/section/main/div[1]/form/div[3]/div[2]/div/div[3]/div/div/input"  #5g 密码
five_hide="/html/body/div[1]/section/section/section/main/div[1]/form/div[3]/div[2]/div/div[2]/div/div[2]/div/div/label/span[1]/span"#5g 隐藏
basic_wifi_apply_button="/html/body/div[1]/section/section/section/footer/div/button[1]"#应用按钮
basic_wifi_cancel_button="/html/body/div/section/section/section/footer/div/button[2]"  #取消按钮
basic_wifi_confirm_button="/html/body/div[2]/div/div[3]/button[2]"#确定按钮
basic_wifi_cancel_button2="/html/body/div[2]/div/div[3]/button[1]"  #取消按钮
#基础设置-设备信息页面元素
basic_device="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[4]/li"#基本设备信息
WIFI="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[2]/li"#wifi
current_link="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[1]/div/div/input"#当前链路
network_status="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/div/div/input"#网络状态
wan_ipv4_address="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[3]/div/div/input"#ipv4地址
mobile_ipv4_address="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[4]/div[6]/div/div/input"#蜂窝ipv4地址
ISP_Name="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div/input"   #ISP Name
sim_status="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[4]/div[3]/div/div/input"   #sim状态
current_network="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[4]/div[1]/div/div/input"   #当前网络
MSISDN="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[4]/div[4]/div/div/input"   #MSISDN
ICCID="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[4]/div[5]/div/div/input"   #ICCID


traffic="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[1]/div/div/div/div[3]"#流量
system="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[1]/div/div/div/div[4]"#系统
upload="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/input"#上传
download="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/input"#下载
total="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/input"#总流量
MAC="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[1]/div/div/input"#MAC地址
SN="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[1]/div/div/input"#SN
imei="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[3]/div/div/input"#imei
Hardware_version="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[4]/div/div/input"#硬件版本
Firmware_version="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[5]/div/div/input"#固件版本
Product_Model="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[6]/div/div/input"#产品型号
Run_time="/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[3]/div/div[7]/div"#运行时间
client="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[3]/li"#客户端
#右上角的菜单元素
reboot="/html/body/div/section/header/div/div/div[2]/div[3]/div/span"#重启
Logout_button = "/html/body/div/section/header/div/div/div[2]/div[2]/div/span"    # 登录按钮
#高级设置
Advanced_settings="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[1]/li"#高级设置
NET="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[2]/li/div"#网络
SMS="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[3]/li/div"#短信
NAT="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[4]/li/div"#NAT
Diagonistic="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[5]/li"#诊断
security="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[6]/li/div"#安全
settings="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[7]/li/div"#设置
#高级设置-网络

current_link2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[1]/div[2]/div/div[1]/div/div/input"   #当前链路
network_status2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input"   #网络状态
wan_ipv4_address="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input"   #wan_ipv4地址
wan_Gateway="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div[2]/div/div/input"   #wan_网关
wan_dns1="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div[3]/div/div/input"   #wan_dns1
wan_dns2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[2]/div/div/input"   #wan_dns2
ISP_Name2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[1]/div/div/input"   #ISP Name
sim_status2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[2]/div/div/input"   #sim状态
Roaming_status="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[3]/div/div/input"   #漫游状态
current_network2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[3]/div/div/input"   #当前网络
mobile_ipv4_address2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[6]/div/div/input"   #蜂窝ipv4地址
mobile_ipv4_DNS1="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[7]/div/div/input"   #蜂窝ipv4DNS1
mobile_ipv4_DNS2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[8]/div/div/input"   #蜂窝ipv4DNS2
mobile_ipv6_address="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[9]/div/div/input"   #蜂窝ipv6地址
mobile_ipv6_DNS1="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[10]/div/div/input"   #蜂窝ipv6DNS1
mobile_ipv6_DNS2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div[11]/div/div/input"   #蜂窝ipv6DNS2
LAN_ip_address2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[4]/div[2]/div/div[1]/div/div/input"   #LAN ipv4地址
LAN_Subnet_mask2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[4]/div[2]/div/div[2]/div/div/input"   #LAN 子网掩码
DHCP_server_status="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[4]/div[2]/div/div[3]/div/div/input"   #DHCP服务器
five_SSID2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[6]/div[2]/div/div[1]/div/div/input"   #5g SSID
five_radio="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[6]/div[2]/div/div[2]/div/div/input"   #5g 开关
five_Mode="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[6]/div[2]/div/div[3]/div/div/input"   #5g 模式
five_Channel="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[6]/div[2]/div/div[4]/div/div/input"   #5g 信道
five_bandwith="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[6]/div[2]/div/div[5]/div/div/input"   #5g 带宽
five_guest_wifi="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[6]/div[2]/div/div[5]/div/div/input"   #5g 访客wifi
TWO_SSID2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[5]/div[2]/div/div[1]/div/div/input"   #2.4g SSID
TWO_radio="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[5]/div[2]/div/div[2]/div/div/input"   #2.4g 开关
TWO_Mode="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[5]/div[2]/div/div[3]/div/div/input"   #2.4g 模式
TWO_Channel="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[5]/div[2]/div/div[4]/div/div/input"   #2.4g 信道
TWO_bandwith="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[5]/div[2]/div/div[5]/div/div/input"   #2.4g 带宽
TWO_guest_wifi="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[5]/div[2]/div/div[6]/div/div/input"   #2.4g 访客wifi
IMEI2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[1]/div/div/input"   #设备状态IMEI
ICCID2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[2]/div/div/input"   #设备状态ICCID
IMSI2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[3]/div/div/input"   #设备状态IMSI
SN2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[4]/div/div/input"   #设备状态SN
MAC2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[5]/div/div/input"   #设备状态MAC
MSISDN2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[6]/div/div/input"   #设备状态MSISDN
Product_Model2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[7]/div/div/input"   #设备状态产品型号
connected_Devices="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[8]/div"   #已连接设备
Run_time2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[7]/div[2]/div/div[9]/div"   #设备状态运行时间
#高级设置-流量统计
traffic_statistics="/html/body/div/section/section/aside/div/div/div[1]/div/ul/div/label[2]/li/ul/li/ul/li[2]"#流量统计
upload2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input"   #上传
download2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[1]/div[2]/div/div[3]/div/div/input"   #下载
total2="/html/body/div/section/section/section/main/div[1]/form/div/div/div[2]/div/div[3]/div/div/input"   #总流量
#高级设置-局域网
LAN="/html/body/div[1]/section/section/aside/div/div/div[1]/div/ul/div/label[2]/li/ul/li/ul/li[3]"#局域网
LAN_ip_address="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[4]/div[2]/div/div[1]/div/div/input"#LAN ipv4地址
LAN_Subnet_mask="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input"#LAN 子网掩码
DHCP_server="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div[1]/div/div/span[2]/span"#DHCP服务器
Lease_time="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/input"#租约时间
IP_pool1="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/input"#IP池1
IP_pool2="/html/body/div/section/section/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div[3]/div/div[4]/div/div/div/input"#IP池2
LAN_apply_button="/html/body/div/section/section/section/footer/div/button[1]"#应用按钮
LAN_cancel_button="/html/body/div/section/section/section/footer/div/button[2]"#取消按钮

