# 作业

1. 数7游戏，把一个随机100个数里面，含7和7的倍数的值提取出来。（提示:filter）
2. 为网站图片生成缩略图(提示：map 难度：考察灵活应用,安装模块sudo apt-get install python-imaging)
3. 写一个装饰器，能记录被装饰函数的访问时间和调用者。（调用者模拟传入,记录文件自己创建，追加操作）
4. 请在纸上手写一遍一个程序的执行过程，程序见课件上讲解的那个程序。


题目2参考代码
```python
#!/usr/bin/env python
#coding: utf-8
# 安装PIL模块  sudo apt-get install python-imaging
import Image, os

# 源目录
#myPath = './'
myPath = '/'
# 输出目录
#outPath = './'
outPath = './'

def processImage(filesource, destsource, name, imgtype):
    '''
    filesource是存放待转换图片的目录
    destsource是存放输出转换后图片的目录
    name是文件名
    imgtype是文件类型
    '''
    imgtype = 'jpeg' if imgtype == '.jpg' else 'png'
    #打开图片
    im = Image.open(filesource + name)
    # 缩放比例
    rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0, im.size[1]/1136.0 if im.size[1] > 1136 else 0)
    if rate:
        im.thumbnail((im.size[0]/rate, im.size[1]/rate))
    im.save(destsource + name, imgtype)

def run():
    # 切换到源目录，遍历源目录下所有图片
    os.chdir(myPath)
    for i in os.listdir(os.getcwd()):
        # 检查后缀
        postfix = os.path.splitext(i)[1]
        if postfix == '.jpg' or postfix == '.png':
            processImage(myPath, outPath, i, postfix)

if __name__ == '__main__':
    run()

```

