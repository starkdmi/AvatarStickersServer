from .base_enums import AvatarPart


class ClothingGraphic(AvatarPart):
    """Clothing graphics. The graphics printed on the clothing if the selected
clothing type is ClothingType.GRAPHIC_SHIRT"""

    __install__ = True
    __enum_path__ = 'clothing_graphics.py'
    __path__ = 'avatar_parts/clothes/graphic'

    NONE = ''
    BAT = 'bat'
    BEAR = 'bear'
    CUMBIA = 'cumbia'
    CUSTOM_TEXT = 'custom_text'
    DEER = 'deer'
    DIAMOND = 'diamond'
    HOLA = 'hola'
    PIZZA = 'pizza'
    RESIST = 'resist'
    SELENA = 'selena'
    SKULL_OUTLINE = 'skull_outline'
    SKULL = 'skull'

    def fromString(str="hat"): 
       if str == "" or str == "none": return ClothingGraphic.NONE
       if str == "bat": return ClothingGraphic.BAT
       if str == "bear": return ClothingGraphic.BEAR
       if str == "cumbia": return ClothingGraphic.CUMBIA
       if str == "custom_text": return ClothingGraphic.CUSTOM_TEXT
       if str == "deer": return ClothingGraphic.DEER
       if str == "diamond": return ClothingGraphic.DIAMOND
       if str == "hola": return ClothingGraphic.HOLA
       if str == "pizza": return ClothingGraphic.PIZZA
       if str == "resist": return ClothingGraphic.RESIST
       if str == "selena": return ClothingGraphic.SELENA
       if str == "skull_outline": return ClothingGraphic.SKULL_OUTLINE
       if str == "skull": return ClothingGraphic.SKULL

       return ClothingGraphic.CUSTOM_TEXT
