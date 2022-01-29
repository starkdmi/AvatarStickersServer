from .base_enums import AvatarPart


class HatType(AvatarPart):
    """Hat types"""

    __install__ = True
    __enum_path__ = 'hat_types.py'
    __path__ = 'avatar_parts/top/hat'

    HAT = 'hat'
    HIJAB = 'hijab'
    TURBAN = 'turban'
    WINTER_HAT_1 = 'winter_hat_1'
    WINTER_HAT_2 = 'winter_hat_2'
    WINTER_HAT_3 = 'winter_hat_3'
    WINTER_HAT_4 = 'winter_hat_4'

    def fromString(str="hat"): 
       if str == "hat": return HatType.HAT
       if str == "hijab": return HatType.HIJAB
       if str == "turban": return HatType.TURBAN
       if str == "winter_hat_1": return HatType.WINTER_HAT_1
       if str == "winter_hat_2": return HatType.WINTER_HAT_2
       if str == "winter_hat_3": return HatType.WINTER_HAT_3
       if str == "winter_hat_4": return HatType.WINTER_HAT_4

       return HatType.Hat
