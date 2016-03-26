# -*- coding: utf-8 -*-


import concierge.templater
import mako.template


class MakoTemplater(concierge.templater.Templater):

    name = "mako"

    def render(self, content):
        template = mako.template.Template(content)
        content = template.render_unicode()

        return content
