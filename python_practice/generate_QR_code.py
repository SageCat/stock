from MyQR import myqr
myqr.run("https://www.baidu.com")
with open("myqr",'b') as f:
    f.write(myqr.Image)