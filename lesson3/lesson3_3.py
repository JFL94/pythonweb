import tools

def main():
   try:
        data = tools.download_youbike_data()
        areas = tools.get_area(data)
        print("目前可以查詢的區域:\n")
        for area in areas:
            print(area,end=" ")
        print("\n")
        selected=input("請選擇一個區域:")
        sites_of_area=tools.get_sites_of_area(data,selected)
        # 格式化顯示站點資訊
        if sites_of_area:
            print(f"\n{selected} 區的 YouBike 站點如下：")
            for site in sites_of_area:
                # 顯示站點名稱與地址
                print(f"站名: {site['sna']}，地址: {site['ar']}")
        
   except Exception as e:
       print("發生錯誤\n{e}")


if __name__ == "__main__":
    main()


