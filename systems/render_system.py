from ..components.position import PositionComponent
from ..components.render import RenderComponent

class RenderSystem:
    def update(self, entity, screen):
        pos = entity.components[positionComponent]
        render = entity.components[RenderComponent]