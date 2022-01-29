from .base_enums import AvatarPart


class HairType(AvatarPart):
    """Hair types"""

    __install__ = True
    __enum_path__ = 'hair_types.py'
    __path__ = 'avatar_parts/top/hair'

    NONE = 'no_hair'
    BIG_HAIR = 'big_hair'
    BOB = 'bob'
    BUN = 'bun'
    CAESAR_SIDE_PART = 'caesar_side_part'
    CAESAR = 'caesar'
    CURLY = 'curly'
    CURVY = 'curvy'
    DREADS = 'dreads'
    FRIDA = 'frida'
    FRIZZLE = 'frizzle'
    FRO_BAND = 'fro_band'
    FRO = 'fro'
    LONG_NOT_TOO_LONG = 'long_not_too_long'
    MIA_WALLACE = 'mia_wallace'
    SHAGGY_MULLET = 'shaggy_mullet'
    SHAGGY = 'shaggy'
    SHAVED_SIDES = 'shaved_sides'
    SHORT_CURLY = 'short_curly'
    SHORT_DREADS_1 = 'short_dreads_1'
    SHORT_DREADS_2 = 'short_dreads_2'
    SHORT_FLAT = 'short_flat'
    SHORT_ROUND = 'short_round'
    SHORT_WAVED = 'short_waved'
    SIDES = 'sides'
    STRAIGHT_1 = 'straight_1'
    STRAIGHT_2 = 'straight_2'
    STRAIGHT_STRAND = 'straight_strand'

    def fromString(str="straight_2"):
      if str == "no_hair": return HairType.NONE
      if str == "big_hair": return HairType.BIG_HAIR
      if str == "bob": return HairType.BOB
      if str == "bun": return HairType.BUN
      if str == "caesar_side_part": return HairType.CAESAR_SIDE_PART
      if str == "caesar": return HairType.CAESAR

      if str == "curly": return HairType.CURLY
      if str == "curvy": return HairType.CURVY
      if str == "dreads": return HairType.DREADS
      if str == "frida": return HairType.FRIDA
      if str == "frizzle": return HairType.FRIZZLE

      if str == "fro_band": return HairType.FRO_BAND
      if str == "fro": return HairType.FRO
      if str == "long_not_too_long": return HairType.LONG_NOT_TOO_LONG
      if str == "mia_wallace": return HairType.MIA_WALLACE
      if str == "shaggy_mullet": return HairType.SHAGGY_MULLET
      if str == "shaggy": return HairType.SHAGGY

      if str == "shaved_sides": return HairType.SHAVED_SIDES
      if str == "short_curly": return HairType.SHORT_CURLY
      if str == "short_dreads_1": return HairType.SHORT_DREADS_1
      if str == "short_dreads_2": return HairType.SHORT_DREADS_2
      if str == "short_flat": return HairType.SHORT_FLAT

      if str == "short_round": return HairType.SHORT_ROUND
      if str == "short_waved": return HairType.SHORT_WAVED
      if str == "sides": return HairType.SIDES
      if str == "straight_1": return HairType.STRAIGHT_1
      if str == "straight_2": return HairType.STRAIGHT_2
      if str == "straight_strand": return HairType.STRAIGHT_STRAND

      return HairType.STRAIGHT_2