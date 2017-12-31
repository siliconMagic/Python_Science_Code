# -*- coding: utf-8 -*-
from traits.api import HasTraits, Int, Str, Array, List

class MetadataTest(HasTraits):
    i = Int(99, myinfo = "test my info")
    s = Str("test", label = u"字符串")
    a = Array
    list = List(Int)
    
test = MetadataTest()
print(test.traits())
print(test.trait("i"))