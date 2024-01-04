import psutil
import json 
def get_ip_info():
    info  = psutil.net_if_addrs()
    interface_name = list(info.keys())[4] # Assuming you want the first interface
    interface_data = info[interface_name][1][1]
    json_representation = json.dumps({
        'InterFace':interface_name,
        'IP-addr': interface_data,
        },indent=4)
    return json_representation 



print(get_ip_info())
# g = {
#     "Wi-Fi": 
#         [
#             [-1, "4A-F2-CF-12-B0-A8", null, null, null],
#             [2, "192.168.1.9", "255.255.255.0", null, null], 
#             [23, "2401:4900:1f32:31b7:4cc3:5cbe:acac:cac1", null, null, null],
#             [23, "2401:4900:1f32:31b7:8d1c:ce6e:5212:7116", null, null, null],
#             [23, "fe80::4e93:8a22:d5c6:493b", null, null, null]
#             ]
#         }