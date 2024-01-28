from abc import ABC, abstractmethod
from ...Domains.Entities.status import Status

class IStatusRepository(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def update(self, status: Status):
        pass
