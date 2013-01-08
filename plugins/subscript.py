import markdown
from markdown import inlinepatterns
from markdown import util

class SubscriptPattern(inlinepatterns.Pattern):
    def handleMatch(self, m):
        el = util.etree.Element("sub")
        el.text = util.AtomicString(m.group(3))
        return el

class SubscriptExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['subscript'] = SubscriptPattern(r'(\~)([^\~]*)\2', md)

def makeExtension(configs=None):
    return SubscriptExtension(configs=configs)
