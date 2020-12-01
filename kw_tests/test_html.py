
from kw_templates.html_element import TAttributes, TStyles, TCss
from kw_tests.common_class import CommonTestClass


class AttributeTest(CommonTestClass):
    """
     * How to check traits? Python in fact has nothing like that.
    """

    def test_simple(self):
        data = TAttributes()
        assert not data.get_attributes()
        assert not data.get_attribute('foo')
        data.set_attribute('foo', 'bar')
        assert 'bar' == data.get_attribute('foo')
        data.set_attribute('foo', 'baz')
        assert 'baz' == data.get_attribute('foo')
        data.remove_attribute('foo')
        assert not data.get_attribute('foo')
        assert not data.get_attributes()

    def test_extend(self):
        data = TAttributes()
        assert not data.get_attributes()
        data.set_attribute('foo', 'bar')
        data.set_attribute('ijn', 'ujm')
        data.add_attributes([
                ('ijn', 'zgv'),
                ('edc', 'rdx'),
            ])
        assert 'zgv' == data.get_attribute('ijn')
        data.add_attributes([(
                'ojv', [
                    'lkj',
                    'nbv',
                    'gfd',
                ],
            )])
        assert 'lkj;nbv;gfd' == data.get_attribute('ojv')

        data.set_attributes([])
        assert not data.get_attributes()

    def test_string_input(self):
        data = TAttributes()
        assert not data.get_attributes()
        data.add_attributes('avail="from:left;insecure:15em;"')
        assert 'from:left;insecure:15em;' == data.get_attribute('avail')
        data.set_attribute('avail', 'xrb')
        assert 'xrb' == data.get_attribute('avail')

    def test_render(self):
        data = TAttributes()
        assert not data.get_attributes()
        data.add_attributes('avail="from:left;insecure:15em;"')
        data.set_attribute('foo', 'bar')
        data.set_attribute('ijn', 'ujm')
        assert ' avail="from:left;insecure:15em;" foo="bar" ijn="ujm"' == data._render_attributes()


class StylesTest(CommonTestClass):
    """
     * How to check traits? Extend them.
    """

    def test_simple(self):
        data = TStyles()
        assert not data.get_attributes()
        assert not data.get_attribute('style')
        data.add_css('foo', 'snt')
        data.add_css('bar', 'fgs')
        data.add_css('baz', 'sdf')
        assert 'sdf' == data.get_css('baz')
        assert 'foo:snt;bar:fgs;baz:sdf;' == data.get_attribute('style')
        data.remove_css('bar')
        assert 'foo:snt;baz:sdf;' == data.get_attribute('style')


class CssTest(CommonTestClass):

    def test_simple(self):
        data = TCss()
        assert not data.get_attributes()
        assert not data.get_attribute('class')
        data.add_class('foo')
        data.add_class('bar')
        data.add_class('baz')
        assert 'foo bar baz' == data.get_attribute('class')
        data.remove_class('bar')
        assert 'foo baz' == data.get_attribute('class')


