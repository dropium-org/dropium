class ObjectFactory:
    def __init__(self):
        self._initiators = {}

    def register(self, key, builder):
        self._initiators[key] = builder

    def create(self, key, **kwargs):
        initiator = self._initiators.get(key)
        if not initiator:
            raise ValueError(key)

        return initiator(**kwargs)

