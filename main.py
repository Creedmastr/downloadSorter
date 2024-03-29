import os
import json
import startup
import shutil

startup.startup()

CONFIG_FILE = open("config.json")
CONFIG_LOAD = json.loads(CONFIG_FILE.read())
CONFIG_PATH = CONFIG_LOAD["user_path_input"]

if CONFIG_PATH.endswith("/"):
    dlPath = CONFIG_PATH + "Downloads"
    documentsPath = CONFIG_PATH + "Documents"
    musicPath = CONFIG_PATH + "Music"
    imagePath = CONFIG_PATH + "Images"
    videoPath = CONFIG_PATH + "Videos"
else:
    dlPath = CONFIG_PATH + "/Downloads"
    documentsPath = CONFIG_PATH + "/Documents"
    musicPath = CONFIG_PATH + "/Music"
    imagePath = CONFIG_PATH + "/Images"
    videoPath = CONFIG_PATH + "/Videos"

dlFolder = os.listdir(dlPath)

for i in dlFolder:
    global itemPath
    itemPath = dlPath + "/" + str(i)

    if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith('.tiff') or i.endswith('.psd') or i.endswith('.ai') or i.endswith(".webp") or i.endswith(".gif"):

            if i.endswith(".psd"):
                psdPath = imagePath + "/Photoshop Files"
                try:
                    os.mkdir(psdPath)
                except OSError as error:
                    print(error)
                shutil.move(itemPath, psdPath)

            if i.endswith(".ai"):
                aiFilePath = imagePath + "/Illustrator Files"
                try:
                    os.mkdir(aiFilePath)
                except OSError as error:
                    print(error)
                shutil.move(itemPath, aiFilePath)

            shutil.move(itemPath, imagePath)
    if i.endswith(".mp3") or i.endswith(".ogg") or i.endswith(".flac") or i.endswith(".m4a") or i.endswith(".mpc") or i.endswith(".opus") or i.endswith(".wav") or i.endswith(".webm"):
        shutil.move(itemPath, musicPath)

    if i.endswith(".docx") or i.endswith(".doc") or i.endswith(".pdf") or i.endswith(".pptx") or i.endswith(".csv") or i.endswith(".xlsx") or i.endswith(".epf") or i.endswith(".xml"):
        if i.endswith(".docx") or i.endswith(".doc"):
            wordDocPath = documentsPath + "/Word Documents"
            try:
                os.mkdir(wordDocPath)
            except OSError as error:
                print(error)
            shutil.move(itemPath, wordDocPath)

        if i.endswith(".pptx"):
            powerpointDocPath = documentsPath + "/PowerPoint Documents"
            try:
                os.mkdir(powerpointDocPath)
            except OSError as error:
                print(error)
            shutil.move(itemPath, powerpointDocPath)

        if i.endswith(".pdf"):
            pdfDocPath = documentsPath + '/Adobe PDF Documents'
            try:
                os.mkdir(pdfDocPath)
            except OSError as error:
                print(error)
            shutil.move(itemPath, pdfDocPath)

        if i.endswith(".csv") or i.endswith(".xlsx"):
            excelFilePath = documentsPath + "/Excel Documents"
            try:
                os.mkdir(excelFilePath)
            except OSError as error:
                print(error)

            shutil.move(itemPath, excelFilePath)

        if i.endswith(".epf"):
            epfFilePath = documentsPath + "/Eclipse Theme"
            try:
                os.mkdir(epfFilePath)
            except OSError as error:
                print(error)

            shutil.move(itemPath, epfFilePath)

        shutil.move(itemPath, documentsPath)
    if i.endswith(".torrent") or i.endswith(".zip") or i.endswith(".rar") or i.endswith(".7z"):
        if i.endswith(".torrent"):
            torrentFilePath = dlPath + "/Torrent Files"
            try:
                os.mkdir(torrentFilePath)
            except OSError as error:
                print(error)

            shutil.move(itemPath, torrentFilePath)
        if i.endswith(".zip") or i.endswith('.rar') or i.endswith("7z"):
            zipFilePath = dlPath + "/Zipped Files"
            try:
                os.mkdir(zipFilePath)
            except OSError as error:
                print(error)

            shutil.move(itemPath, zipFilePath)
    if i.endswith(".msi") or i.endswith(".exe") or i.endswith(".pkg"):
        if i.endswith(".msi") or i.endswith(".pkg"):
            installerPath = dlPath + "/Installer - MSI - PKG Files"
            try:
                os.mkdir(installerPath)
            except OSError as error:
                print(error)
            shutil.move(itemPath, installerPath)

        if i.endswith(".exe"):
            executableFilePath = dlPath + "/Executable - EXE Files"
            try:
                os.mkdir(executableFilePath)
            except OSError as error:
                print(error)
            shutil.move(itemPath, executableFilePath)
    if i.endswith(".jar" or ".jar.log"):
        javaFilePath = dlPath + "/Java - JAR Files"
        try:
            os.mkdir(javaFilePath)
        except OSError as error:
            print(error)
        shutil.move(itemPath, javaFilePath)
    if i.endswith(".txt"):
        textFilePath = documentsPath + "/Text Files"
        try:
            os.mkdir(textFilePath)
        except OSError as error:
            print(error)

        shutil.move(itemPath, textFilePath)
    if i.endswith(".dll"):
        dllFilePath = documentsPath + "/DLL Files"
        try:
            os.mkdir(dllFilePath)
        except OSError as error:
            print(error)
        shutil.move(itemPath, dllFilePath)
    if i.endswith(".epub") or i.endswith(".mobi"):
        bookFilePath = documentsPath + "/MOBI - EPUB (Book) Files"
        try:
            os.mkdir(bookFilePath)
        except OSError as error:
            print(error)

        shutil.move(itemPath, bookFilePath)
    if i.endswith(".mov") or i.endswith(".mp4"):
        shutil.move(itemPath, videoPath)
    if i.endswith(".crdownload"):
        nonfinishedDownloadPath = dlPath + "/Unfinished Downloads"
        try:
            os.mkdir(nonfinishedDownloadPath)
        except OSError as error:
            print(error)

        shutil.move(itemPath, nonfinishedDownloadPath)
    if i.endswith(".iso"):
        isoFilePath = dlPath + "/ISO - System Files"
        try:
            os.mkdir(isoFilePath)
        except OSError as error:
            print(error)
        shutil.move(itemPath, isoFilePath)

    if i.endswith(".blend") or i.endswith(".blend1"):
        blendPath = documentsPath + "/BLEND - Blender Files"
        try:
            os.mkdir(blendPath)
        except OSError as error:
            print(error)

        shutil.move(itemPath, blendPath)

    if i.endswith(".ipa"):
        ipaPath = documentsPath + "/Apple IPAs"
        try:
            os.mkdir(ipaPath)
        except OSError as error:
            print(error)

        shutil.move(itemPath, ipaPath)