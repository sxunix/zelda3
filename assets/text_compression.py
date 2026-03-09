import util, sys

kTextAlphabet_US = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
  "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
  "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
  "-", ".", ",", 
  # 64 - 79
  "[...]", ">", "(", ")",
  "[Ankh]", "[Waves]", "[Snake]", "[LinkL]", "[LinkR]",
  "\"", "[Up]", "[Down]", "[Left]",
  # 80 - 95
  "[Right]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
  "[4HeartL]", "[4HeartR]", " ", "<", "[A]", "[B]", "[X]", "[Y]",
]

kTextAlphabet_DE = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
  "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
  "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
  # 64 - 79
  "-", ".", ",",  "[...]", ">", "(", ")",
  "[Ankh]", "[Waves]", "[Snake]", "[LinkL]", "[LinkR]",
  "\"", "[UpL]", "[UpR]", "[LeftL]",
  # 80 - 95
  "[LeftR]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
  "[4HeartL]", "[4HeartR]", " ", "ö", "[A]", "[B]", "[X]", "[Y]", "ü",
  # 96-111
  "ß", ":", "[DownL]", "[DownR]", "[RightL]", "[RightR]",
  "è", "é", "ê", "à", "ù", "ç", "Ä", "Ö", "Ü", "ä"
  # 112-
]

kTextAlphabet_FR = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
  "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
  "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
  # 64 - 79
  "-", ".", ",",  "[...]", ">", "(", ")",
  "[Ankh]", "[Waves]", "[Snake]", "[LinkL]", "[LinkR]",
  "\"", "[UpL]", "[UpR]", "[LeftL]",
  # 80 - 95
  "[LeftR]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
  "[4HeartL]", "[4HeartR]", " ", "ö", "[A]", "[B]", "[X]", "[Y]", "ü",
  # 96-111
  "ô", ":", "[DownL]", "[DownR]", "[RightL]", "[RightR]",
  "è", "é", "ê", "à", "ù", "ç", "â", "û", "î", "ä"
  # 112-
]

kText_CommandLengths_US = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, ]
kText_CommandNames_US = [
  "NextPic", "Choose", "Item", "Name", "Window", "Number",
  "Position","ScrollSpd", "Selchg", "Unused_Crash", "Choose3",
  "Choose2", "Scroll", "1", "2", "3", "Color",
  "Wait", "Sound", "Speed", "Unused_Mark", "Unused_Mark2", "Unused_Clear",
  "Waitkey"
]

kTextDictionary_US = [
'    ', '   ', '  ', "'s ", 'and ', 
'are ', 'all ', 'ain', 'and', 'at ', 
'ast', 'an', 'at', 'ble', 'ba', 
'be', 'bo', 'can ', 'che', 'com', 
'ck', 'des', 'di', 'do', 'en ', 
'er ', 'ear', 'ent', 'ed ', 'en', 
'er', 'ev', 'for', 'fro', 'give ', 
'get', 'go', 'have', 'has', 'her', 
'hi', 'ha', 'ight ', 'ing ', 'in', 
'is', 'it', 'just', 'know', 'ly ', 
'la', 'lo', 'man', 'ma', 'me', 
'mu', "n't ", 'non', 'not', 'open', 
'ound', 'out ', 'of', 'on', 'or', 
'per', 'ple', 'pow', 'pro', 're ', 
're', 'some', 'se', 'sh', 'so', 
'st', 'ter ', 'thin', 'ter', 'tha', 
'the', 'thi', 'to', 'tr', 'up', 
'ver', 'with', 'wa', 'we', 'wh', 
'wi', 'you', 'Her', 'Tha', 'The', 
'Thi', 'You', 
]


kText_CommandLengths_EU = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
kText_CommandNames_EU = [
  "Selchg", "Choose3", "Choose2", "Scroll", "1", "2", "3",
  "Color", "Wait", "Sound", "Speed", "Mark", "Mark2",
  "Clear", "Waitkey", "EndMessage", "NextPic", "Choose",
  "Item", "Name", "Window", "Number", "Position", "ScrollSpd",
]

kTextDictionary_DE = [
'    ', '   ', '                                          ', '-Knopf', ' ich ', 
' Sch', ' Ver', ' zu ', ' es ', 'aber', 
'alle', 'auch', 'ang', 'aus', 'auf', 
'an', 'bist', 'bin', 'bei', 'der ', 
'die ', 'das ', 'den ', 'dem ', 'daß', 
'der', 'die', 'das', 'den', 'da', 
'etwas', 'ein ', 'ein', 'en ', 'er ', 
'es ', 'en', 'er', 'es', 'ei', 
'für', 'fe', 'habe', 'hier', 'hast', 
'her', 'ich ', 'icht', 'ich', 'ist', 
'ie ', 'im', 'ie', 'kannst ', 'kannst', 
'kommen', 'kann ', 'll', 'mich', 'mein', 
'mit', 'mal', 'mir', 'nicht ', 'nicht', 
'nen', 'nn', 'och ', 'och', 'or', 
'schon', 'sich', 'sein', 'sch', 'sie', 
'st', 'tte', 'te ', 'te', 'und ', 
'und', 'ung', 'um', 'von', 'ver', 
'vor', 'wird', 'zu ', 'Amulett', 'Aber', 
'Deine', 'Dich ', 'Dir ', 'Dir', 'Der', 
'Die', 'Das', 'Du ', 'Du', 'Da', 
'Ein', 'Hyrule', 'Hier', 'Ich ', 'Master-Schwert', 
'Mach', 'Rubine', 'Sch', 'Sie', 'Ver', 
'Weisen', 'Zelda', 
]

kTextDictionary_FR = [
'                                          ', ' de ', ' la ', ' le ', ' ! ', 
' d', ' p', ' t', ' !', ", c'est moi, Sahasrahla", 
', ', 'ais ', 'as ', 'an', 'ai', 
'a ', 'che', 'ce', 'ch', 'dans ', 
'des ', 'de ', 'de', 'est ', 'ent', 
'en ', 'er ', 'es ', 'en', 'es', 
'et', 'eu', 'e,', 'e ', 'ique', 
'ien', 'is ', 'ie', 'in', 'ir', 
'is', 'i ', 'les ', 'la ', 'le ', 
'le', 'll', 'maintenant', 'magique', 'ment', 
'mon', 'mai', 'me', 'ne ', 'onne', 
'oir', 'our', 'ouv', 'oi', 'on', 
'ou', 'or', 'pouvoir', 'pour', 'peux', 
'pas', 'que ', 'qu', 'rubis', 're ', 
'ra', 're', 'r ', 'sorcier', 's l', 
's d', 'se', 'so', 's ', 'tro', 
'te ', 'tu ', 'te', 't ', 'un', 
'ur', 'u ', 'ver', 'Ah ! Ah ! Ah !', "C'est", 
'Ganon', 'Maintenant', 'Merci', 'Monde', 'Perle de Lune', 
'Tu as trouvé ', 'Ténèbres', 'Tu peux', 'Tu ',
]


# Uses the original format
def org_encoder(cmd, param):
    if cmd not in kText_CommandNames_US:
      raise Exception(f'Invalid cmd {cmd}')
    cmd_index = kText_CommandNames_US.index(cmd)
    if kText_CommandLengths_US[cmd_index] != (1 if param == None else 2):
      raise Exception(f'Invalid cmd params {cmd} {param}')
    if param == None:
      return [cmd_index + 0x67]
    return [cmd_index + 0x67, int(param)]

kCmdInfo = {
  "Scroll" : (0x80, ),
  "Waitkey" : (0x81, ),
  "1" : (0x82, ),
  "2" : (0x83, ),
  "3" : (0x84, ),
  "Name" : (0x85, ),
  "Wait" : (0x87, {i:i+0x00 for i in range(16)}),
  "Color" : (0x87, {i:i+0x10 for i in range(16)}),
  "Number" : (0x87, {i:i+0x20 for i in range(16)}),
  "Speed" : (0x87, {i:i+0x30 for i in range(16)}),
  "Sound" : (0x87, {45 : 0x40, 64 : None}), # pt uses 64 for some reason
  "Choose" : (0x87, 0x80),
  "Choose2" : (0x87, 0x81),
  "Choose3" : (0x87, 0x82),
  "Selchg" : (0x87, 0x83),
  "Item" : (0x87, 0x84),
  "NextPic" : (0x87, 0x85),
  "Window" : (0x87, {0 : None, 2 : 0x86}),
  "Position" : (0x87, {0: 0x87, 1: 0x88}),
  "ScrollSpd" : (0, {0 : None}),
}

# Uses another format where there's more bytes left for characters
def new_encoder(cmd, param):
  if cmd not in kCmdInfo:
    raise Exception(f'Invalid cmd {cmd}')
  info = kCmdInfo[cmd]
  if len(info) <= 1 or isinstance(info[1], int):
    if param != None:
      raise Exception(f'Invalid cmd params {cmd} {param}')
    return info
  else:
    if param == None or param not in info[1]:
      raise Exception(f'Invalid cmd params {cmd} {param}')
    r = info[1][param]
    return (info[0], r) if r != None else ()

def cn_encoder(cmd, param):
  return new_encoder(cmd, param)

kEncoders = {'org' : org_encoder, 'new' : new_encoder, 'cn' : cn_encoder}


class LangUS:
  alphabet = kTextAlphabet_US
  dictionary = kTextDictionary_US
  command_lengths = kText_CommandLengths_US
  command_names = kText_CommandNames_US
  rom_addrs = [0x9c8000, 0x8edf40]
  COMMAND_START = 0x67
  SWITCH_BANK = 0x80
  FINISH = 0xff
  DICT_BASE_ENC, DICT_BASE_DEC = 0x88, 0x88
  ESCAPE_CHARACTER = None
  encoder = 'org'

class LangEN(LangUS):
  alphabet = kTextAlphabet_DE
  dictionary = kTextDictionary_US
  rom_addrs = [0x9c8000, 0x8edf60]

class LangES(LangUS):
  alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
    "Q", "R", "S", "T", "U", "V", "W", "é", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
    "ó", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
    "[Waves]", ".", ",", 
    # 64 - 79
    "[...]", ">", "(", ")",
    "ñ", "ú", "á", "[LinkL]", "[LinkR]", "\"", "[Up]", "[Down]", "[Left]",
    # 80 - 95
    "[Right]", "í", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
    "[Ankh]", "[4HeartR]", " ", "[Snake]", "[A]", "[B]", "[X]", "[Y]", "[I]",
    "¡", "¿", "Ñ"
  ]
  # "[Ankh]", "[Waves]", "[Snake]"

  dictionary = [
    '    ', '   ', '  ', ' en', ' la ', ' el ', ' de ', 'ien', 'tra', ' de', 
    'te ', 'ar', 'a ', 'ada', 'es', 'as', 'o ', ' con', 'ero', 'ado', 
    'e ', 'que', 'en', 'al', 'os ', 'ora', 'nte', ' al', 'lo ', 'or', 
    'os', 'er', 'aci', 'res', ' que ', ' es', 'el', 'los ', 'tar', ' se', 
    ', ', 'ro', ' de l', ' est', 're', 'on', 'an', 'pued', ' del', 'ás ', 
    'la', 'ti', 'la ', 'Es', 'to', 'ta', 'para', 'uer', 'ier', ' un ', 
    ' por', 'oder', 'da', 'in', 'cu', ' ha', 'per', 'ano', ' ve', 'cer', 
    'lo', ' no ', 'ic', 'ra', 'ab', 'ir', ' una', 'undo', 'es ', 'as ', 
    'con', 'a, ', 'te', ' m', 'gu', ' tu', 'ando', ' p', 'de', 'le', 
    'ol', 'o, ', 'ten', 'lle', ' a ', 'aba', 'com', 
  ]
  rom_addrs = [0x9c8000, 0x8edf40]


class LangNL(LangUS):
  alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
    "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
    "-", ".", ",", "[...]", ">", "(", ")", "[Ankh]",
    "[Waves]", "[Snake]", "[LinkL]", "[LinkR]", "\"", "[Up]", "[Down]", "[Left]",
    # 80 - 95
    "[Right]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
    "[4HeartL]", "[4HeartR]", " ", "<", "[A]", "[B]", "[X]", "[Y]",
  ]

  dictionary = [
    '    ', '   ', '  ', "'s ", 'and ', 'are ', 'all ', 'ain', 'and', 'at ', 
    'ast', 'an', 'at', 'ble', 'ba', 'be', 'bo', 'can ', 'che', 'com', 
    'ck', 'des', 'di', 'do', 'en ', 'er ', 'ear', 'ent', 'ed ', 'en', 
    'er', 'ev', 'for', 'fro', 'give ', 'get', 'go', 'have', 'has', 'her', 
    'hi', 'ha', 'ight ', 'ing ', 'in', 'is', 'it', 'just', 'know', 'ly ', 
    'la', 'lo', 'man', 'ma', 'me', 'mu', "n't ", 'non', 'not', 'open', 
    'ound', 'out ', 'of', 'on', 'or', 'per', 'ple', 'pow', 'pro', 're ', 
    're', 'some', 'se', 'sh', 'so', 'st', 'ter ', 'thin', 'ter', 'tha', 
    'the', 'thi', 'to', 'tr', 'up', 'ver', 'with', 'wa', 'we', 'wh', 
    'wi', 'you', 'Her', 'Tha', 'The', 'Thi', 'You', 
  ]
  rom_addrs = [0x9c8000, 0x8edf40]



class LangSV(LangUS):
  alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ö", "P", # 0 - 15
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
    "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
    "å", ".", ",", "ä", ">", "(", ")","ö",
    "Å", "Ä", "[LinkL]", "[LinkR]", "\"", "[Up]", "[Down]", "[Left]",
    # 80 - 95
    "[Right]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
    "[4HeartL]", "[4HeartR]", " ", "<", "[Ankh]", "[Waves]", "[Snake]", "-", "[I]",
    "[i]", "…", " ",
  ]

  dictionary = [
    '    ', '   ', '  ', 'Du ', 'till', 'vill', 'bara', 'det', 'den', 'och', 
    'en ', 'r ', 'n ', 'ett', 'en', ' d', 'a ', 'Hjäl', 'har', 'ter', 
    't ', 'var', ' s', 'de', 'kan', 'med', 'som', 'för', 'att', 'ar', 
    ' h', 'er', 'jag', 'dig', 'öppna', 'mig', 'är', 'inte', 'hit', 'på ', 
    'an', 'e ', 'rupie', '0kej', ' m', 'et', ', ', 'gång', 'måst', 'ten', 
    ' f', 'u ', 'men', 'te', 'tt', 'ka', 'vara', 'ken', '0m ', 'från', 
    'myck', 'någo', 'in', ' k', ' i', 'vil', 'bar', 'ond', 'För', 'Jag', 
    'ra', 'tack', 'll', 'g ', 'ta', 'om', 'anna', 'alla', 'en,', 'ber', 
    'hem', 'han', 'st', 'ig', ' t', 'tro', 'kraf', 'ör', ' v', 'ag', 
    '… ', 'får', 'sin', 'mme', 'mma', 'en ', 'tat',
  ]
  rom_addrs = [0x9c8000, 0x8edf40]


class LangPL(LangUS):
  alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
    "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
    "-", ".", ",", "ć", "[Right]", "(", ")", "[Ankh]", 
    "[Waves]", "[Snake]", "[LinkL]", "[LinkR]","\"", "[Up]", "[Down]", "ę",

    "ł", "ń", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
    "ą", "[4HeartR]", " ", "[Left]", "ó", "ś", "ż", "ź", "Ł",
    "Ś", "Ż", "Ź",
  ] # 
  dictionary = ['Trój', '...', 'ść', 'Nie', ' nie', ' się', 'może', ' że', 'and', 'at ', 
    ' ty', 'an', 'at', 'kus', 'ba', 'be', 'bo', 'chce', 'che', 'ki ', 
    'za', 'des', 'di', 'do', 'en ', 'er ', 'sz ', 'ent', 'ed ', 'en', 
    'er', ' w', 'moc', 'zię', 'przez', 'ale', 'go', 'dzie', 'has', 'rze', 
    'hi', 'ha', 'który', 'aby ', 'in', 'is', 'it', 'twoj', 'Może', 'łeś', 
    'la', 'lo', 'czn', 'ma', 'me', 'mu', 'szcz', 'ska', 'śli', 'przy', 
    'znaj', 'iecz', 'of', 'on', 'or', '   ', 'ple', 'pow', 'pro', 're ', 
    're', 'mnie', 'se', ' z', 'so', 'st', 'któr', ' jak', 'ksz', 'sze', 
    'coś', ' je', 'to', 'tr', 'up', 'kie', 'praw', 'wa', 'we', 'mi', 
    'wi', 'szy', 'chc', 'pra', 'cie', ' i ', 'esz',
  ]

  rom_addrs = [0x9c8000, 0x8edf40]

class LangPT(LangUS):
  alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
    "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
    "-", ".", ",", "[...]", ">", "(", ")", "[Ankh]",
    "[Waves]", "[Snake]", "[LinkL]", "[LinkR]", "\"", "[Up]", "[Down]", "[Left]",
    # 80 - 95
    "[Right]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
    "[4HeartL]", "[4HeartR]", " ", "<", "[A]", "[B]", "[X]", "[Y]", "[I]",

    "¡", "[!]", "Á", "À", "Â", "Ã", "É", "Ê", "Í", "Ó", "Ô", "Õ", "Ú", "á", "à", "â", 
    "ã", "é", "ê", "í", "ó", "ô", "õ", "ú", "ç", 
  ]
  dictionary = [
    '     ', '    ', '   ', '                                          ', 'o ', 'a ', 'e ', '..', 'de', 'ar', 
    's ', 'ra', ' d', 'es', 'ocê ', 'do', ' a', ' p', 'er', ' e', 
    'que', 'r ', 'os', 'te', ', ', 'as', 'or', 'm ', 'en', ' o', 
    'nt', 're', ' s', 'co', 'da', 'se', 'st', ' c', ' m', 'em', 
    'ma', 'ta', ' n', 'ad', 'on', 'al', 'ro', 'an', 'u ', 'nd', 
    ' um', 'pa', 'ca', 'el', ' f', 'to', 'in', ' t', 'ou', 'ei', 
    'ss', 'ir', 'no', 'ri', 'tr', 'me', 'la', 'ia', 'le', 've', 
    'is', 'sa', 'eu', 'pe', 'a.', 'na', 'so', 'mo', 'ga', 'o.', 
    'á ', 'lo', 'ha', 'pr', 'ua', ' l', '! ', 'ui', 'am', 'ti', 
    'io', 'gu', 'i ', 'di', 'nh', ' i', 'id', 
  ]
  ESCAPE_CHARACTER = 0x62
  rom_addrs = [0x9c8000, 0x8edf40]
  encoder = 'new'

  def __init__(self):
    assert len(self.alphabet) == 121

class LangEU:
  command_lengths = kText_CommandLengths_EU
  command_names = kText_CommandNames_EU
  COMMAND_START = 0x70
  SWITCH_BANK = 0x88
  FINISH = 0x8f
  DICT_BASE_ENC, DICT_BASE_DEC = 0x88, 0x90
  ESCAPE_CHARACTER = None
  encoder = 'new'

class LangDE(LangEU):
  alphabet = kTextAlphabet_DE
  dictionary = kTextDictionary_DE
  rom_addrs = [0x9c8000, 0x8CEB00]

class LangFR(LangEU):
  alphabet = kTextAlphabet_FR
  dictionary = kTextDictionary_FR
  rom_addrs = [0x9c8000, 0x8CE800]

class LangFR_C(LangEU):
  alphabet = kTextAlphabet_FR
  dictionary = kTextDictionary_FR
  rom_addrs = [0x9c8000, 0x8CF150]

class LangCN(LangUS):
  # Chinese alphabet: US chars (0x00-0x5F) + CN punctuation (0x60-0x6F)
  alphabet = kTextAlphabet_US + [
    "，", "。", "！", "？", "…", "：", "、", "—", "（", "）", "《", "》", "\u201c", "\u201d", "\u2018", "\u2019",
  ]
  # 1118 unique CJK characters from dialogue_cn.txt, sorted by Unicode codepoint
  cjk_chars = list(
    '一七万三上下不与专且世东丢两个中丰临为主丽举久么义之乎乐也书买乱了予争事于亏互井亚些亡交产亮亲人什仇今仍从仔他付代令以们件价任份仿企伏伐休众优伙会伟传伤伴伸似但位住佐体何佛作你使供侬便保信倒候借值假做停健偷储像儿允充先光克免兔入全公六共关兴兵其具兹内再冒冰冲冷冻准减凝几凭凶出击刃分切划列则创利别刮到制刺刻前剑剧剩副劈力办功加务动助励劲劳势勇勉勾匙匠升午半单卖南卜占卡卢卦卫印危即厄厅历厚原去又及友双反发取受变口古另叨只叫召可右吃各合吉吊同名后向吗吞否吧听启吱吵吸吹呀呃告员呢呣周呱呼命和咒咔咕咳咻品哇哈响哟哥哦哪哼唠唤唯商啊啦喂喜喝嗝嗯嘛嘟嘿噜器噬囚四回因团围国图土圣在地场坏块坚坠坦型埋城堂堡塔塘塞墓墙增壁士声处备复外多够大天太夫失头夺奇奏奖套女她好如姆始姿婆子字存孙学孩它守安完官定宜宝实宠客室宫害家容寄密寒对寻封射将小少尔尝就尼尽局层居展属山岩巢工左巧巨差己已布师希带帮常干平年并幸广庄庆应底店座庭康建开弃弄式弓引弟张弥弱弹强当形影彻往征待很徊律得徘御德徽心必忘忙快怀态怎怕思怪总恐恢恭息恶情惊惑惜惠惫想惹意感愧愿慧慰憾懂懦戏成我或战房所扇手才打扔托扛扭扯扰找承技把抓投抚抢护报抱抵担拉拔拖招拜拥择拯拾拿持指按挑挖挡挥捕换捣据掉掘探接控推掩掷描提揭搜搞搬携摧摸撞擅操攀攒支收改攻放故敌救教敢散数整文斗料断斯新方旁旅旋族无既旧早时明易映是晕晚晨普晶智暖暗暴曦曲更曾替最月有朋服望期木未本机杀杆村杖束条来松林枚果枝架某查标树样根格桩梭棋棒森棵楼概模横次欢欲欺歉止正此步武死殿毁每比毛氏民气水永求池汪沉沙没河治沼沿泉泊法注泰泽洒洞活派流浪海消涌涡深混清游湖湛滚满漆漠漩漫潜澈激瀑灌火灭灯灵灾炎炸点炼烂烈烦热焰然照熬燃爆爪爱父爽片牌牢物牵特犯狂独猩献猴王玛玩环现珍珠球理瓦瓶甚甜生用由甲界留疑疲病痛登白百的皮益盖盗盛目直相盼盾看真眠眩眼着睛睡瞄瞌矗知石砍破砸确碍碎碑示礼祈祝神祭祷禁福离种科秒秘积称移稀稍穆穴空穿突窝立站竟章笛第笼等答策简算管箭箱篷类粉精糊糟系索紧繁红约级纪纳纵线细终经绑结绕给绝统继绩续绿缉缩缺罐网罩罪置美群老者而耗聊联聚肉股肯胖胜能脉脚脸腿臂自至致舒舞色节花英荡荣药获莽菇萨落蒙蓄蓝蔽蕴藏蘑虫蛋蛰蜂蜜血行衣表被裂装裔西要见观视觉角解触言计认让议记讲讶许论设访证识诉试诚话该语误说请诺读谁调谋谎谓谢负贤败贪购贵费贼资赏赐赚赢赫走赶起趁越趣足跑跟路跳踢蹦蹼身躲轻辈辉输边达过迎运近还这进远连述迷追退送逃选途通逛逝造遇遍道遗遭避那邦邪部都配酷释里重量金针钥钩钱铁铠铲银铺链锁错锤键锻镖镜长门闪闭问闯闲间闻阴阵阿附陈降院除险陪陶随隐难雄集雨雾需震非靠面靴音顶顺须顾预领颗题颜风飞饰香马驱骑骗骚骨骷髅高鬼魂魔鱼鲁鸟麻黄黑鼾齐龟'
  )
  dictionary = []
  rom_addrs = [0x9c8000, 0x8edf40]
  ESCAPE_CHARACTER = None
  encoder = 'cn'

  def __init__(self):
    assert len(self.alphabet) == 111, f'Expected 111, got {len(self.alphabet)}'
    assert len(self.cjk_chars) == 1118

kLanguages = {
  'us' : LangUS(),
  'de' : LangDE(),
  'fr' : LangFR(),
  'fr-c' : LangFR_C(),
  'en' : LangEN(),
  'es' : LangES(),
  'pl' : LangPL(),
  'pt' : LangPT(),
  'redux' : LangUS(),
  'nl' : LangNL(),
  'sv' : LangSV(),
  'cn' : LangCN(),
}

def dialogue_filename(s):
  if s == 'us': return 'dialogue.txt'
  return f"dialogue_{s.replace('-', '_')}.txt"

def uses_new_format(lang):
  return kLanguages[lang].encoder in ('new', 'cn')

dict_expansion = []

def decode_strings_generic(get_byte, lang):
  info = kLanguages[lang]
  p, rom_idx = info.rom_addrs[0], 1
  result = []
  while True:
    s, srcdata = '', []
    while True:
      c = get_byte(p)
      srcdata.append(c)
      l = info.command_lengths[c - info.COMMAND_START] if c >= info.COMMAND_START and c < info.SWITCH_BANK else 1

      p += l
      if c == 0x7f: # EndMessage
        break
      if c < info.COMMAND_START:
        if c == info.ESCAPE_CHARACTER:
          c = get_byte(p); p += 1
          srcdata.append(c)
        s += info.alphabet[c]
      elif c < info.SWITCH_BANK:
        if l == 2:
          srcdata.append(get_byte(p - 1))
          s += '[%s %.2d]' % (info.command_names[c - info.COMMAND_START], get_byte(p - 1))
        else:
          s += '[%s]' % info.command_names[c - info.COMMAND_START]
      elif c == info.FINISH:
        return result # done
      elif c == info.SWITCH_BANK:
        p = info.rom_addrs[rom_idx]; rom_idx += 1
        s, srcdata = '', []
      elif c < info.SWITCH_BANK + 8:
        if lang != 'pt':
          assert 0
      else:
        s += info.dictionary[c - info.DICT_BASE_DEC]
        dict_expansion.append(len(info.dictionary[c - info.DICT_BASE_DEC]))
    result.append((s, srcdata)) 
    if len(result) >= 397 and lang == 'pt':
      return result
#    print(len(result), s)   
#    if len(result) == 89:
#      print(s)
#      sys.exit(0)


  
def print_strings(rom, file = None):
  texts = decode_strings_generic(rom.get_byte, rom.language)
  if len(texts) == 396:
    extra_str = "[Speed 00]0- [Number 00]. 1- [Number 01][2]2- [Number 02]. 3- [Number 03]"
    texts = texts[:4] + [(extra_str, None)] + texts[4:]

  for i, s in enumerate(texts):
    print('%s: %s' % (i + 1, s[0]), file = file)


def encode_greedy_from_dict(s, i, rev, a2i, info):
  a = s[i:]
  if r := rev.get(a[0]):
    for k, v in r.items():
      if a.startswith(k):
        return [v + info.DICT_BASE_ENC], len(k)

  if a[0] == '[':
    cmd, param = a[1:a.index(']')], None
    cmdlen = len(cmd)
    if r := a2i.get(a[:cmdlen+2]):
      return [r], cmdlen+2
    if ' ' in cmd:
      cmd, param = cmd.split(' ', 1)
      param = int(param)
    return kEncoders[info.encoder](cmd, param), cmdlen + 2
  else:
    return [a2i[a[0]]], 1

  print('substr %s not found' % a)
  assert 0

def compress_strings(xs, lang = 'us'):
  info = kLanguages[lang]
  rev = {}
  for a,b in enumerate(info.dictionary):
    rev.setdefault(b[0], {})[b] = a
  #rev = {b:a for a,b in enumerate(info.dictionary)}
  a2i = {e:i for i,e in enumerate(info.alphabet)}

  # For Chinese, build a CJK char lookup
  cjk2i = {}
  if hasattr(info, 'cjk_chars'):
    cjk2i = {ch: idx for idx, ch in enumerate(info.cjk_chars)}

  def compress_string(s):
    i = 0
    r = bytearray()
    while i < len(s):
      # Check for CJK character first (Chinese mode)
      if cjk2i and s[i] in cjk2i:
        idx = cjk2i[s[i]]
        esc_base = len(info.alphabet)  # First escape prefix byte
        prefix = esc_base + (idx >> 8)
        r.extend([prefix, idx & 0xff])
        i += 1
      else:
        what, num = encode_greedy_from_dict(s, i, rev, a2i, info)
        r.extend(what)
        i += num
    return r
  return [compress_string(x) for x in xs]
  
def verify(get_byte):
  for i, (decoded, original) in enumerate(decode_strings_generic(get_byte, 'us')):
    c = compress_strings([decoded])[0]
    if c != original:
      print('String %s not match: %s, %s' % (decoded, c, original))
      break
    else:
      pass

def encode_dictionary(lang = 'us'):
  info = kLanguages[lang]
  rev = {b:a for a,b in enumerate(info.alphabet)}
  return [bytearray(rev[c] for c in line) for line in info.dictionary]

if __name__ == "__main__":
  ROM = util.load_rom(sys.argv[1] if len(sys.argv) >= 2 else None, True)

  decoded = decode_strings_generic(ROM.get_byte, 'de')
  print('Total bytes: %d' % sum(len(a[1]) for a in decoded))

  print('Dict tokens: %d' % len(dict_expansion))
  print('Dict save: %d' % (sum(dict_expansion) - len(dict_expansion)))

  print('US size ', len(kTextDictionary_US))
  print('DE size ', len(kTextDictionary_DE))

  texts = [a[0] for a in decoded]


  # Pal seems to have one string too little
  if len(texts) == 396:
    extra_str = "[Speed 00]0- [Number 00]. 1- [Number 01][2]2- [Number 02]. 3- [Number 03]"
    texts = texts[:4] + [extra_str] + texts[4:]

  #for i, s in enumerate(texts):
  #  print('%s: %s' % (i + 1, s), file = None)


  #encode_dictionary()
  compr = compress_strings(texts, 'de')
  print(f'Compressed size (excl eof): {sum(len(a) for a in compr)}')


