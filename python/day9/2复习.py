# 文件处理
    # 打开文件
        #open('路径'，'打开方式'，'指定编码方式')
        # 打开方式 r w a r+ w+ a+ b
            #r+ 打开文件直接写 和读完再写
        # 编码方式 —— utf-8
    # 操作文件
        # 读
            # read 一次性读
            # readlines 一次性读
            # readline 一行一行读
                #不知道在哪儿结束
                #视频 图片 rb bytes 按照字节读
            # for循环 —— 最好！！！
        # 写
            # write
        # 光标 —— 文件指针
            #seek _ 指定光标移动到某个位置
            #tell _ 获取光标当前的位置
            #truncate _ 截取文件
    # 关闭文件
        #close

# 修改文件
with open('小护士班主任',encoding='utf-8') as f,open('小护士班主任.bak','w',encoding='utf-8') as f2:
    for line in f:
        if '星儿' in line:  #班主任:星儿
            line = line.replace('星儿','啊娇')
        #写文件
        f2.write(line) #小护士:金老板

import os
os.remove('小护士班主任') #删除文件
os.rename('小护士班主任.bak','小护士班主任')  #重命名文件

