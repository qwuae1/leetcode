#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: Crifan Li
Version: v1.2 20190531
Function: Generate Gitbook's README.md from template_README.md and README_current.json
Note: should run this python file from single gitbook foler
        eg: /Users/crifan/dev/dev_root/gitbook/gitbook_src_root/books/gitbook_demo
"""

import os
import json
import codecs
import re

################################################################################
# Global Config
################################################################################

gReadmeTemplateFilename = "template_README.md"
gReadmeCurrentFilename = "README_current.json"
gReadmeOutputFilename = "README.md"
# # for debug
# gReadmeOutputFilename = "README_tmp_generated.md"

################################################################################
# Internal Function
################################################################################


def loadTextFromFile(fullFilename, fileEncoding="utf-8"):
    """load file text content from file"""
    with codecs.open(fullFilename, 'r', encoding=fileEncoding) as fp:
        allText = fp.read()
        # logging.debug("Complete load text from %s", fullFilename)
        return allText

def saveTextToFile(fullFilename, textData):
    """save text data info file"""
    with codecs.open(fullFilename, 'w', encoding="utf-8") as fp:
        fp.write(textData)
        fp.close()
        print("Complete save file %s" % fullFilename)

def loadJsonFromFile(fullFilename):
    """load and parse json dict from file"""
    jsonDict = {}
    with codecs.open(fullFilename, 'r', encoding="utf-8") as jsonFp:
        try:
            jsonDict = json.load(jsonFp)
            print("Complete load json from %s" % fullFilename)
        except json.decoder.JSONDecodeError as decodeError:
            print("JSONDecodeError %s for %s" % (decodeError, fullFilename))
            jsonDict = None

    return jsonDict

################################################################################
# Main Part
################################################################################

def generateReadmeMd():
    # run python in :
    # /Users/crifan/dev/dev_root/gitbook/gitbook_src_root/books/gitbook_demo
    curBookPath = os.getcwd()
    # print("curBookPath=%s" % curBookPath)
    # /Users/crifan/dev/dev_root/gitbook/gitbook_src_root/books/gitbook_demo
    curDirname = os.path.dirname(curBookPath)
    # print("curDirname=%s" % curDirname)
    curBasename = os.path.basename(curBookPath)
    # print("curBasename=%s" % curBasename)
    GitbookSrcRootBooks = os.path.abspath(os.path.join(curBookPath, ".."))
    # print("GitbookSrcRootBooks=%s" % GitbookSrcRootBooks)
    GitbookSrcRoot = os.path.abspath(os.path.join(GitbookSrcRootBooks, ".."))
    # print("GitbookSrcRoot=%s" % GitbookSrcRoot)

    readmeTemplateFulPath = os.path.join(GitbookSrcRoot, "common/config/template", gReadmeTemplateFilename)
    # print("readmeTemplateFulPath=%s" % readmeTemplateFulPath)
    readmeTemplateMdStr = loadTextFromFile(readmeTemplateFulPath)
    # print("readmeTemplateMdStr=%s" % readmeTemplateMdStr)

    readmeCurrentFullPath = os.path.join(curBookPath, gReadmeCurrentFilename)
    # print("readmeCurrentFullPath=%s" % readmeCurrentFullPath)
    readmeCurrentJson = loadJsonFromFile(readmeCurrentFullPath)
    # print("readmeCurrentJson=%s" % readmeCurrentJson)

    for eachKey in readmeCurrentJson.keys():
        # print("eachKey=%s" % eachKey)
        patternToReplace = "\{\{%s\}\}" % eachKey
        replacedStr = readmeCurrentJson[eachKey]
        # print("patternToReplace=%s -> replacedStr=%s" % (patternToReplace, replacedStr))
        readmeTemplateMdStr = re.sub(patternToReplace, replacedStr, readmeTemplateMdStr)
        # print("readmeTemplateMdStr=%s" % readmeTemplateMdStr)

    generatedReadmeFullPath = os.path.join(curBookPath, gReadmeOutputFilename)
    # print("generatedReadmeFullPath=%s" % generatedReadmeFullPath)
    saveTextToFile(generatedReadmeFullPath, readmeTemplateMdStr)

if __name__ == "__main__":
    generateReadmeMd()