import markdown
from markdown import inlinepatterns
from markdown import util

class SuperscriptPattern(inlinepatterns.Pattern):
    def handleMatch(self, m):
        el = util.etree.Element("sup")
        el.text = util.AtomicString(m.group(3))
        return el

class SuperscriptExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['superscript'] = SuperscriptPattern(r'(\^)([^\^]*)\2', md)

def makeExtension(configs=None):
    return SuperscriptExtension(configs=configs)
