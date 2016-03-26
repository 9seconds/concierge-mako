# -*- coding: utf-8 -*-


import concierge_mako


TEMPLATE = """\
lalala

% for i in range(2):
i - ${i}
% endfor
"""

RESULT = """\
lalala

i - 0
i - 1
"""


def test_name():
    assert concierge_mako.MakoTemplater.name == "mako"


def test_render():
    tpl = concierge_mako.MakoTemplater()

    assert tpl.render(TEMPLATE) == RESULT
