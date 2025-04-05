# 参阅以下
    
    https://github.com/MemeCrafters/meme-generator/wiki/新表情编写指北
# 自用配置

    [meme]
    load_builtin_memes = true  # 是否加载内置表情包
    meme_dirs = ["/home/ubuntu/Desktop/memenew"]  # 加载其他位置的表情包，填写文件夹路径
    meme_disabled_list = ['dianzhongdian','flash_blind','shoot','symmetric']  # 禁用的表情包列表，填写表情的 `key`

    [resource]
    # 下载内置表情包图片时的资源链接，下载时选择最快的站点
    resource_urls = [
      "https://raw.githubusercontent.com/MemeCrafters/meme-generator/",
      "https://mirror.ghproxy.com/https://raw.githubusercontent.com/MemeCrafters/meme-generator/",
      "https://cdn.jsdelivr.net/gh/MemeCrafters/meme-generator@",
      "https://fastly.jsdelivr.net/gh/MemeCrafters/meme-generator@",
      "https://raw.gitmirror.com/MemeCrafters/meme-generator/",
    ]

    [gif]
    gif_max_size = 4.0  # 限制生成的 gif 文件大小，单位为 Mb
    gif_max_frames = 100  # 限制生成的 gif 文件帧数

    #[translate]
    #baidu_trans_appid = ""  # 百度翻译api相关，表情包 `dianzhongdian` 需要使用
    #baidu_trans_apikey = ""  # 可在 百度翻译开放平台 (http://api.fanyi.baidu.com) 申请

    [server]
    host = "127.0.0.1"  # web server 监听地址
    port = 2233  # web server 端口

    [log]
    log_level = "INFO"  # 日志等级
