from you_get import (  # 需安装you-get这个轮子
    common
)
p = "完成!"
d = "开始下载"
print("欢迎使用视频下载器")
print("报告BUG：https://github.com/jiabingxian/download-bilibili/issues")
url = str(input("视频URL:"))
print(d)
common.any_download_playlist(url, output_dir=".\\video", merge=True, playlists=True)
print(p)
