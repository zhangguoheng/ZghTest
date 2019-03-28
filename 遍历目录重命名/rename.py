# -*- coding:UTF-8 -*-
import os

class Rename():

    # 初始化
    def __init__(self, folder):
        self.folder = folder
        self.fileCount = 1
        self.folderCount = 1
    # 开始
    def begin(self):
        self.getAllfileAndDirPath(self.folder)
    # 遍历
    def getAllfileAndDirPath(self,sourcePath):
        if not os.path.exists(sourcePath):
            return
        listName = os.listdir(sourcePath)
        for name in listName:
            absPath = os.path.join(sourcePath, name)
            if os.path.isfile(absPath):
                filetype = os.path.splitext(name)[1]
                newname = '文件%d' % self.fileCount
                newDir = os.path.join(sourcePath, newname + filetype)
                print('文件序号：%d,Path:%s 命名后：%s' % (self.fileCount, absPath, newDir))
                os.rename(absPath, newDir)
                self.fileCount = self.fileCount+1
            if os.path.isdir(absPath):
                self.getAllfileAndDirPath(absPath)
                newname = '文件夹%d' % self.folderCount
                newDir = os.path.join(sourcePath, newname)
                print('文件夹序号：%d,Path:%s 命名后：' % (self.fileCount, absPath, newDir))
                os.rename(absPath, newDir)
                self.folderCount = self.folderCount+1


if __name__ == '__main__':
    folder = input('请输入目录:')
    msg = '请确认目录：%s下无重要文件或者已经备份,如操作失误开发者无责 Y/N：' % folder
    is_ok = input(msg)

    test = Rename(folder)  # 目录
    if is_ok == 'Y':
        test.begin();
    else:
        print('您很谨慎！')