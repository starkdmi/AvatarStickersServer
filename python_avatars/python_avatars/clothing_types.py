from .base_enums import AvatarPart


class ClothingType(AvatarPart):
    """Clothing types"""

    __install__ = True
    __enum_path__ = 'clothing_types.py'
    __path__ = 'avatar_parts/clothes'

    NONE = ''
    BLAZER_SHIRT = 'blazer_shirt'
    BLAZER_SWEATER = 'blazer_sweater'
    COLLAR_SWEATER = 'collar_sweater'
    GRAPHIC_SHIRT = 'graphic_shirt'
    HOODIE = 'hoodie'
    OVERALL = 'overall'
    SHIRT_CREW_NECK = 'shirt_crew_neck'
    SHIRT_SCOOP_NECK = 'shirt_scoop_neck'
    SHIRT_V_NECK = 'shirt_v_neck'

    def fromString(str="hat"): 
       if str == "" or str == "none": return ClothingType.NONE
       if str == "blazer_shirt": return ClothingType.BLAZER_SHIRT
       if str == "blazer_sweater": return ClothingType.BLAZER_SWEATER
       if str == "collar_sweater": return ClothingType.COLLAR_SWEATER
       if str == "graphic_shirt": return ClothingType.GRAPHIC_SHIRT
       if str == "hoodie": return ClothingType.HOODIE
       if str == "overall": return ClothingType.OVERALL
       if str == "shirt_crew_neck": return ClothingType.SHIRT_CREW_NECK
       if str == "shirt_scoop_neck": return ClothingType.SHIRT_CREW_NECK
       if str == "shirt_v_neck": return ClothingType.SHIRT_V_NECK

       return ClothingType.GRAPHIC_SHIRT
