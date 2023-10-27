from ..components.position import PositionComponent
from ..components.direction import DirectionComponentComponent

class MovementSystem:
    def update(self, entity):
        pos = entity.components[positionComponent]
        dir = entity.components.get(DirectionComponent)