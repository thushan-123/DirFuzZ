from file_builder import FileUrlBuilder

""" 
    TEST CASE 1:
        url : http://orange.com
        dir name : voldemort
        file name: abc.html
        expected result : http://orange.com/voldemort
"""
def test_file_url():
    f = FileUrlBuilder("http://orange.com/voldemort/", ".html")
    assert f.fileUrlPathBuilder("abc") == "http://orange.com/voldemort/abc.html"