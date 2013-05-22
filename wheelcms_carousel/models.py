from wheelcms_axle.templates import template_registry
from wheelcms_spokes.page import Page, PageType
from wheelcms_axle.content import ImageContent

def frontpage_context(handler, request, node):
    ## limit to images, visible
    datanode = node.child('data')
    if datanode is None:
        return dict(carousel=[])

    return dict(carousel=[n for n in node.child('data').children()
                          if isinstance(n.content(), ImageContent)
                          and n.content().spoke().workflow().is_visible()
                         ],
                slots=[s for s in node.child('data').children()
                          if isinstance(s.content(), Page)
                          and s.content().spoke().workflow().is_visible()
                         ],
               )


template_registry.register(PageType, "wheelsite_site/page_frontpage_view.html",
                           "Frontpage view", context=frontpage_context)

