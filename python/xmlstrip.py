#!/usr/bin python

import xml.dom.minidom as minidom

class XMLStrip:

    def __init__(self, src):
        self.srcDom = minidom.parse(src)
        self.dst = None
        self.stripped = False

    def removeAllSpace(self, s):
        s = s.strip()
        s = ''.join(s.split(' '))
        s = ''.join(s.split('\t'))
        s = ''.join(s.split('\n'))
        s = ''.join(s.split('\r'))
        if s == '':
            s = ' '

        return s

    def handleNode(self, parent, child):
        if child.nodeType == child.TEXT_NODE:
            child.data = self.removeAllSpace(child.data)
        elif child.nodeType == child.COMMENT_NODE:
            parent.removeChild(child)

    def travel(self, node):
        if not node.hasChildNodes():
            return
        child = node.firstChild
        while child:
            tmpChild = child.nextSibling
            self.handleNode(node, child)
            self.travel(child)
            child = tmpChild

    def strip(self):
        if not self.stripped:
            self.travel(self.srcDom)
            self.srcDom = minidom.parseString(self.srcDom.toxml())
            self.travel(self.srcDom)
            self.srcDom = minidom.parseString(self.srcDom.toxml())
        return self.srcDom.toxml()
