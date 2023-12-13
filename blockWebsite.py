
def blockWebsite(blockList, unblockList):
    # site_block = ["www.gingersoftware.com", "gingersoftware.com", "google.com.vn"]
    # host_path = "C:/Windows/System32/drivers/etc/hosts"
    host_path = "C:/DoAnTotNghiep/hosts"
    redirect = "127.0.0.1"
    
    if len(blockList) != 0:
        print("Start Blocking!")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in blockList:
                if website not in content:
                    host_file.write(redirect + " "+ website + "\n")
                else:
                    pass
    if len(unblockList) != 0:
        print("Unblock Website!")
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in unblockList):
                    host_file.write(lines)
            host_file.truncate()
    return ''

# blockWebsite(blockList, unblockList)