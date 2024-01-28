from .Interfaces.i_status_repository import IStatusRepository
from ..Domains.Entities.status import Status

class StatusRepository(IStatusRepository):
    def read(self):
        pass
    
    def update(self, status: Status):
        pass