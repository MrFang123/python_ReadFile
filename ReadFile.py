import os

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        #print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
        #files = files.replace("'","")
        for file in files:
        	addr = "system_system_chip: require('"+root+"\\"+file+"'),"
        	addr = addr.replace('\\', '/')
        	addr = addr.replace('C:/Users/Admin/Documents/WeChat Files/wxid_sv5bs88uvbvm21/Files', '/img')
        	print(addr) #当前路径下所有非目录子文件  

if __name__ == '__main__':
	path=os.getcwd()
	print("当前目录:" + path)
	file_name(path)