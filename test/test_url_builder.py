from url_builder import UrlBuilder

""" 
    TEST CASE 1:
        url : http://orange.com
        dir name : voldemort
        expected result : http://orange.com/voldemort
"""
def test_add_dir():
    builder = UrlBuilder("http://orange.com")
    assert builder.add_dir("voldemort") == "http://orange.com/voldemort"
    
    
""" 
    TEST CASE 2:
        url : http://orange.com/
        dir name : voldemort
        expected result : http://orange.com/voldemort
"""
def test_url_slash():
    builder = UrlBuilder("http://orange.com/")
    assert builder.add_dir("voldemort") == "http://orange.com/voldemort"
    
"""
    TEST CASE 3:
        url : http://orange.com/
        dir names : voldemort,snep,magonigal
        expected result : http://orange.com/voldemort/snep/magonigal
"""
def test_url_many_dir():
    builder = UrlBuilder("http://orange.com/")
    assert builder.add_more_dir("voldemort","snep","magonigal") == "http://orange.com/voldemort/snep/magonigal"

