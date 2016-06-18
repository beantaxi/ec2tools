from ._kernel import factory

def Instance (id):
    o = factory.Instance(id)
    return o


def KeyPair (name):
    o = factory.KeyPair(name)
    return o


def Volume (id):
    o = factory.Volume(id)
    return o
