import requests
import random
ips = {"http://182.88.134.205:8123",
       "http://61.135.217.7:80",
       "http://222.71.121.248:31288",
       "http://111.155.124.84:8123",
       "http://114.115.216.99:80",
       "http://182.88.14.122:8123",
       "http://120.25.164.134:8118",
       "http://183.128.124.152:42709",
       "http://113.121.20.147:808",
       "http://110.73.3.122:8123",
       "http://110.73.1.23:8123",
       "http://202.108.2.42:80",
       "http://118.187.58.34:53281",
       "http://123.163.137.56:808",
       "http://27.153.128.9:36609",
       "http://110.73.53.137:8123",
       "http://121.231.144.19:6666",
       "http://121.31.79.116:8123",
       "http://110.73.8.229:8123",
       "http://223.241.119.101:8010",
       "http://115.46.76.45:8123",
       "http://110.73.7.140:8123",
       "http://110.73.4.128:8123",
       "http://110.216.60.136:80",
       "http://171.36.62.101:8123",
       "http://121.31.100.191:8123",
       "http://171.36.62.154:8123",
       "http://118.114.77.47:8080",
       "http://112.114.98.40:8118",
       "http://180.167.46.22:53281",
       "http://221.10.159.234:1337",
       "http://119.127.17.162:808",
       "http://110.73.50.174:8123",
       "http://110.73.43.246:8123",
       "http://223.241.119.157:808",
       "http://171.36.63.234:8123",
       "http://116.30.233.134:8118",
       "http://171.38.90.246:8123",
       "http://110.73.9.53:8123",
       "http://110.72.28.153:8123",
       "http://121.231.147.209:6666",
       "http://39.69.15.245:53281",
       "http://171.39.10.184:8123",
       "http://223.241.116.73:8010",
       "http://110.73.1.110:8123",
       "http://60.185.128.111:21591",
       "http://121.31.102.243:8123",
       "http://113.121.181.139:20731",
       "http://60.17.233.47:48670",
       "http://180.123.171.167:37861",
       "http://59.38.241.83:46728",
       "http://117.25.190.11:37386",
       "http://1.199.195.7:20603",
       "http://112.114.98.197:8118",
       "http://219.138.58.245:3128",
       "http://121.31.84.41:8123",
       "http://182.88.44.116:8123",
       "http://110.73.40.211:8123",
       "http://111.155.116.210:8123",
       "http://110.73.12.86:8123",
       "http://110.73.12.219:8123",
       "http://110.72.26.253:8123",
       "http://171.39.42.27:8123",
       "http://112.114.99.84:8118",
       "http://223.241.117.122:8010",
       "http://110.73.48.225:8123",
       "http://112.114.93.184:8118",
       "http://27.40.141.100:61234",
       "http://111.155.116.245:8123",
       "http://182.88.134.253:8123",
       "http://171.39.236.124:8123",
       "http://223.241.118.77:8010",
       "http://110.73.49.54:8123",
       "http://110.72.20.102:8123",
       "http://121.31.70.185:8123",
       "http://125.112.194.167:40133",
       "http://221.233.86.170:3128",
       "http://182.90.105.86:8123",
       "http://112.114.99.16:8118",
       "http://183.135.252.245:23950",
       "http://202.141.161.30:8118",
       "http://182.90.101.75:8123",
       "http://182.88.161.169:8123",
       "http://101.68.73.54:53281",
       "http://182.88.167.194:8123",
       "http://61.178.238.122:63000",
       "http://223.241.79.34:8118",
       "http://123.161.157.105:29108",
       "http://124.237.130.46:9999",
       "http://219.138.58.144:3128",
       "http://182.90.30.156:8118",
       "http://121.31.174.145:8123",
       "http://223.241.117.2:8010",
       "http://220.170.241.16:808",
       "http://223.241.119.208:8010",
       "http://171.37.157.189:8123",
       "http://222.77.40.201:29019",
       "http://121.31.169.148:8123",
       "http://110.189.207.166:38748",
       "http://121.31.176.201:8123",
       "http://60.168.80.193:808",
       "http://59.63.178.203:53281",
       "http://223.241.78.218:8010",
       "http://112.114.92.10:8118",
       "http://182.90.106.250:8123",
       "http://115.46.75.119:8123",
       "http://120.43.62.63:20535",
       "http://112.114.92.184:8118",
       "http://112.114.98.125:8118",
       "http://112.114.92.246:8118",
       "http://180.213.192.104:8123",
       "http://223.241.116.52:8010",
       "http://124.228.239.178:808",
       "http://182.90.82.103:8123",
       "http://110.73.0.127:8123",
       "http://180.109.152.222:47519",
       "http://121.31.101.141:8123",
       "http://59.57.46.61:23161",
       "http://140.250.136.7:29134",
       "http://221.233.164.82:808",
       "http://218.73.136.193:41466",
       "http://121.31.70.133:8123",
       "http://111.155.116.206:8123",
       "http://110.73.54.226:8123",
       "http://221.233.86.127:3128",
       "http://122.4.41.116:20487",
       "http://110.72.23.44:8123",
       "http://111.155.116.217:8123",
       "http://121.31.101.86:8123",
       "http://121.31.195.49:8123",
       "http://182.88.179.98:8123",
       "http://223.241.117.124:8010",
       "http://121.31.177.192:8123",
       "http://121.31.101.38:8123",
       "http://110.73.4.88:8123",
       "http://115.46.67.100:8123",
       "http://115.46.76.90:8123",
       "http://182.88.212.96:8123",
       "http://120.37.164.86:37783",
       "http://110.73.54.169:8123",
       "http://49.82.247.186:35533",
       "http://221.233.86.114:3128",
       "http://27.40.137.91:61234",
       "http://110.73.13.236:8123",
       "http://223.241.119.127:8010",
       "http://121.31.70.108:8123",
       "http://27.150.119.54:45231",
       "http://112.114.99.50:8118",
       "http://121.31.81.102:8123",
       "http://110.73.50.177:8123",
       "http://110.72.38.241:8123",
       "http://110.73.43.83:8123",
       "http://27.40.142.50:61234",
       "http://110.73.35.51:8123",
       "http://110.72.45.159:8123",
       "http://183.172.66.208:8118",
       "http://110.72.25.130:8123",
       "http://223.241.78.102:8010",
       "http://222.208.83.108:9000",
       "http://121.232.144.35:9000",
       "http://162.105.86.202:8118",
       "http://223.223.203.30:8080",
       "http://121.232.199.17:9000",
       "http://49.70.209.29:9000",
       "http://221.230.7.60:9000",
       "http://220.173.47.13:8123",
       "http://121.232.144.65:9000",
       "http://111.155.116.236:8123",
       "http://118.193.107.115:80",
       "http://120.27.10.38:8090",
       "http://111.155.116.232:8123",
       "http://61.234.123.16:82",
       "http://218.3.75.149:9000",
       "http://121.232.144.86:9000",
       "http://106.39.179.118:80",
       "http://221.4.133.67:53281",
       "http://118.190.119.12:1080",
       "http://118.117.139.129:9000",
       "http://114.67.229.117:8118",
       "http://121.40.81.129:8118",
       "http://171.215.236.229:9000",
       "http://180.118.33.229:9000",
       "http://111.155.116.210:8123",
       "http://121.232.145.190:9000",
       "http://121.232.144.35:9000",
       "http://115.29.170.58:8118",
       "http://121.232.146.203:9000",
       "http://118.193.107.30:80",
       "http://121.232.146.104:9000",
       "http://223.241.119.129:8010",
       "http://117.79.87.165:80",
       "http://121.232.144.14:9000",
       "http://218.3.75.146:9000",
       "http://110.172.220.197:8080",
       "http://61.145.194.28:8080",
       "http://223.223.203.30:8080",
       "http://117.90.137.49:9000",
       "http://121.232.144.40:9000",
       "http://182.129.241.50:9000",
       "http://162.105.86.202:8118",
       "http://171.215.201.164:9000",
       "http://180.118.94.137:9000",
       "http://218.14.121.233:9000",
       "http://218.14.121.230:9000",
       "http://59.78.37.165:1080",
       "http://202.194.14.72:8118",
       "http://223.241.78.179:8010",
       "http://111.155.116.219:8123",
       "http://112.95.18.200:8118",
       "http://221.230.7.56:9000",
       "http://114.67.229.117:8118",
       "http://223.241.117.187:8010",
       "http://118.193.107.202:80",
       "http://122.96.59.100:82",
       "http://121.199.35.223:8123",
       "http://119.23.63.152:8118",
       "http://125.67.73.12:9000",
       "http://120.27.10.38:8090",
       "http://117.90.252.95:9000",
       "http://180.118.128.10:9000",
       "http://218.14.121.230:9000",
       "http://121.232.146.39:9000",
       "http://120.25.253.234:8118",
       "http://218.3.75.148:9000",
       "http://221.230.7.60:9000",
       "http://120.25.253.234:8118",
       "http://121.232.148.27:9000",
       "http://121.232.145.107:9000",
       "http://121.232.146.53:9000",
       "http://180.110.150.189:8118",
       "http://122.96.59.105:843",
       "http://121.232.145.245:9000",
       "http://180.118.128.89:9000",
       "http://218.14.121.233:9000",
       "http://121.232.147.175:9000",
       "http://222.73.68.144:8090",
       "http://180.118.32.203:9000",
       "http://114.215.192.135:8118",
       "http://120.26.199.103:8118",
       "http://222.208.83.108:9000",
       "http://120.25.164.134:8118",
       "http://218.3.75.154:9000",
       "http://219.150.189.212:9999",
       "http://117.90.252.191:9000",
       "http://223.241.118.84:8010",
       "http://118.117.136.224:9000",
       "http://182.88.135.10:8123",
       "http://118.193.107.54:80", }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
# }
# url_confirm = '//www.shixiseng.com'


# def get_ips():
#        ip = random.choice(ips)
#        try:
#               r = requests.get(url=url_confirm, headers=headers,
#                                proxies={'http': ip}, timeout=1)
#               r.raise_for_status()
#               return ip
#        except Exception as e:
#               get_ips()


# if __name__ == '__main__':
#        get_ips()
