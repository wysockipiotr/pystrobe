def overrides(interface_class):
    def overrider(method):
        if method.__name__ not in dir(interface_class):
            raise TypeError('Override error')
        return method

    return overrider
