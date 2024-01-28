from ..Domains.Entities.model import Model
from ..Domains.Entities.model_type import ModelType
from .Interfaces.i_model_repository import IModelRepository

class ModelRepository(IModelRepository):
    _humanoid_model: Model
    _accessory_model: Model
    
    def update(self, model: Model):
        model_type = model.get_model_type()
        
        if model_type is ModelType.HUMANOID:
            self._humanoid_model = model
        elif model_type is ModelType.ACCESSORY:
            self._accessory_model = model