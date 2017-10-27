class DoubledItemsCounter():
    """
    simple decorator for counting occurance of doubled items
    """
    def __init__(self, f):
        self.f = f
        self.items_doubled = 0

    def __call__(self, *args):
        x = self.f(*args)
        if x:
            self.items_doubled += 1
        return x
