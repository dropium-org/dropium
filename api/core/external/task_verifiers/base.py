from abc import abstractmethod


class TaskVerifier:
    def __init__(self):
        self._parameters = {}

    def verify(self, **kwargs) -> bool:
        self._parameters = self.populate_default_params(**kwargs);
        return self.handle_verify(**kwargs)
    
    @abstractmethod
    def populate_default_params(self)->dict:
        print("base.populate_default_params")
        pass

    @abstractmethod
    def handle_verify(self, **kwargs) -> bool:
        print("base.handle_verify")

class TaskVerifyException(Exception):
    def __init__(self, *args) :
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"TaskVerifyException - {self.message}"
        else:
            return "TaskVerifyException."