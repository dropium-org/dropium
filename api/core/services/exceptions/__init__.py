

class ResourceExistedException(Exception):
    def __init__(self, *args):
        super(Exception).__init__(*args)


class ResourceNotFoundException(Exception):
    def __init__(self, *args, **kwargs):

        # Call super constructor
        super().__init__(*args, **kwargs)
