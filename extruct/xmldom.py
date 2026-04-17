# mypy: disallow_untyped_defs=False
from __future__ import annotations

from copy import copy, deepcopy
from xml.dom import Node
from xml.dom.minidom import Attr, NamedNodeMap

from lxml.etree import ElementBase, XPath, _ElementUnicodeResult, tostring
from lxml.html import HtmlElementClassLookup, HTMLParser

try:
    from lxml.etree import _ElementStringResult
except ImportError:

    class _ElementStringResult(bytes):  # type: ignore[no-redef]
        """
        _ElementStringResult is removed in lxml >= 5.1.1,
        so we define it here for compatibility.
        """

        def getparent(self):
            pass


class DomElementUnicodeResult:
    CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
    ELEMENT_NODE = Node.ELEMENT_NODE
    TEXT_NODE = Node.TEXT_NODE

    def __init__(self, text):
        self.text = text
        self.nodeType = Node.TEXT_NODE

    @property
    def data(self):
        pass


class DomTextNode:
    CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
    ELEMENT_NODE = Node.ELEMENT_NODE
    TEXT_NODE = Node.TEXT_NODE

    def __init__(self, text):
        self.data = text
        self.nodeType = Node.TEXT_NODE


def lxmlDomNodeType(node):
    pass


class DomHtmlMixin:
    CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
    ELEMENT_NODE = Node.ELEMENT_NODE
    TEXT_NODE = Node.TEXT_NODE

    _xp_childrennodes = XPath("child::node()")

    @property
    def documentElement(self):
        pass

    @property
    def nodeType(self):
        pass

    @property
    def nodeName(self):
        # FIXME: this is a simplification
        pass

    @property
    def tagName(self):
        pass

    @property
    def localName(self):
        pass

    def hasAttribute(self, name):
        pass

    def getAttribute(self, name):
        pass

    def setAttribute(self, name, value):
        pass

    def cloneNode(self, deep):
        pass

    @property
    def attributes(self):
        pass

    @property
    def parentNode(self):
        pass

    @property
    def childNodes_xpath(self):
        pass

    @property
    def childNodes(self):
        pass

    def getElementsByTagName(self, name):
        pass

    def getElementById(self, i):
        pass

    @property
    def data(self):
        pass

    def toxml(self, encoding=None):
        pass


class DomHtmlElementClassLookup(HtmlElementClassLookup):
    def __init__(self):
        super().__init__()
        self._lookups = {}

    def lookup(self, node_type, document, namespace, name):
        pass


class XmlDomHTMLParser(HTMLParser):
    """An HTML parser that is configured to return XmlDomHtmlElement
    objects, compatible with xml.dom API
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        parser_lookup = DomHtmlElementClassLookup()
        self.set_element_class_lookup(parser_lookup)
