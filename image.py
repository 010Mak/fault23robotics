from colorama import Fore

def draw_dodecahedron():
    print(Fore.MAGENTA)  # Set color to purple
    print("""
%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&%%&%&&&&&&&&&&&&&&&&&&&&&&&&%%%&&%%%#%%&%&%&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%&%%%%%%%%%%&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%&%&%%%%%#%%%%%%&%&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&..**,.%&&%&&......%&%%%%%../*..&&&%&&&.&&&%..&&%&&&......&%%%%%..(%%%(.%%%%%%......#%%%%%%%(. %%%%##%%%%%&%%&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&./&&&&&&&&&&..&&&&&&&&&&.(&&&&.*&&&&&&.&&&&..&&&&&&.*&&&%%%&%%%./#.&%(.%&&&&%%%% .%%%%%%%%( #,.%%%%#%%%&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@.&&&&&&..&&&&&&&&&&.(&&&&.*&&&&&&.&&&&..&&&&&&.*&&%%%%%&&%.*&%. (.%&%%%&& .%%%%%%%%%#.  .. %%&&%&&&&&%&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&%&&&&&&&&&&.....(&%%&&%......%%%%%%%*....../%%%%%#.....%%%%%%%......%%%%%%.*%%&%..%%%%%%....../%%%%# %%%&& .&&&&%&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&%&&&%&&&%&&&%%&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&%&&&&%&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&
&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&%%%%&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%&&%&&&&%%%%&%%%%&%%%%%%&%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&@&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&#/@&&&&&@@@&@@@@&@@&&@&&&&&&&&&&&&&&%%%%%%%%%(**@@&&&&&&&&&&&&&&&&&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&//&&/*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/#@&&/&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*(&&&&&%*/&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&*/&&&&&/%&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&@&&&&&*#&&&&&&&&&*/&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&/*&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&/*%@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&(*&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/&&&&&&&&&&&&&&&&#*/&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&*@&&&&&&&&&&&/&&&&&@@%//***%@&@@&@&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&@#***(@&&/*@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&/%&&&&&&&&&&&@*&&&&&&&&&&&&&@@&@@&@@&(**//#&@@&&&&&&&&&&&*&&&/**/&&&&&&&&&&&&/*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*/@&&@&&&&&&&&&*&&&&&&&&&&&@&&@@@@@@@@@@@@@@@@@@@@@@#/&#****%&&&&&&&&&&&&&&&&&&&*(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&@&&***@&&&&&%/@&&&&&&&&&&&@@@@@@&@@@@@&@@@@@@@&///*&*@&&&&@*/&&&&&&&&&&&&&&&&&&&*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@*&&&&&&&@&&/*/(#&&&&&&&&&&&&@@&@&@@@@@@@@@#**/#@@@@@@@&*@@&&&&&(*&&&&&&&&&&&&&&&&&&&*%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&%*&&&&&&&&&&&&&/&@(**%&&&&&&&@@@@&&&&/*//&@@@&@@@@@@@@@@@*@&&&&&&&&*&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(*&&&&&&&&&&&&&*&&&&&&&&#//#&@#*/*(@@@@@@@@@@@@@@@@@&@@@@@/&&&&&&&&&&/#&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&**&&&&&&&&&&&&&/&&&&&&&&&&&&&/&@@@@@@@@@@@@&@&&@@&@@&@@@@@@(&&&&&&&&&&&*/&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*/&&&&&&&&&&&&&/&&&&&&&&&&&&&&*&&&&&@@&@&@@&&&&&&&&@&&@&&&@@##&&&&&&&&&&&%*&&&&&&&&&&&&&&&&&&*&&@&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&@&@@&*#@&&&&&&&&&&&@*&&&&&&&&&&&&&&&*&&&&&&&@@@&@&@&&&&&&&&&&@&&&&%#&&&&&&&&&&&&&/&&&&&&&&&&&&&&&&%%*&@&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&*&&&&@&&&&&&&&&&&&%&&&&&&&&&&&&/&&&&&&&&&&&&@@*(&&&&&&&&&&&&&&&%#*&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&#/&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/&&&&&&&&&&&&&&&/*&&&&&&&&&&&&&&&&(*&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&%*&&&&&&&&&@@%(/#&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&*/&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&(*#%&&&&&&&&&&&&&%/&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&(***(&&&&&(&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&*#&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&@&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&(@&*/&&&/***#@&&&@/&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&@&&&&&&&&&&&&&&&&&*(&&&&&&&&&&&&&&&&&*&&&&&&@&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&*@&&&&&&&&&&&*&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&*/&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&*%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&#*&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&@@@@@@&&@@@&&&&&&&&**&&&&&&&&&&&&&&&&&&/&@&&&&&&&&&*%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&&&&&&&&(*&&&&&&&&&&&&/&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&@@@@@@@@@@@@@@&&&&&&&%/*&&&&&&&&&&&@&&&&&@*%&&&&&&&&&*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/&&&&&&&&&&&&&&&&**&&&&&&&&&&&@/@&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&@@@@@@@@@@@@@@@&&&&&&%&&**&&&&&&&&&&&&&&&&&&&*&&&&&&&&*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&@/&&&&&&&&&&&&&&&//&&&&&&&&&&&&*&&&&&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&@@@@@@@@@@@@@@@&&&&&&&%%%%/*&&&&&&&&&&&&&&&&&&&/#&&&&&&*#&&&&&&&&&&&&&&&&&@@&(*//%@&&&&&&&**&&&&&&&&&*#&&&&&&&&&&&&*&&&&&&&&@&&&&&&&&&&&&&&&@&&&&&
&&&&@@&@@@@@@@@%&&&&&&&&&&%%%%&(/&&&&&&&&&&&&&&&&&&&@*&&&&&*#&&&&&&&&&&%*/*#@@&&&&&&&&&&&&&&&&&&&&&*/&&@*%&&&&&&&&&&&@*&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%&&#/&&&&&&&&&&&&&&&&&&&&((&&&*(%/**(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*/*#&&&&&&&&&@*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&%%&%&&&%*&&&&&&&&&&&&&&&&&&&&&/@&*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*&@&&&&(*#&&&&*&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&%/&&&&&&&&&&&&&&&@&&&****#%**/**#@&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%/&&&&&&&&&&&@/*@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&%&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&/@&&&&&&&&&(***(&&@*&&&&&&&&&&&&&&&(****/%@&&&&&&&&&&&&&&&&&&&@#*&&&&&&&&&&@**&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&*&%***/&&&&&&&&&&/&&&&&&&&&&&&&&&&&&&&&&&&&&%/*/**#&&&&&&&&&&/*&&&&&&&&&%*%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&(*%&&&&&&&&&&&&&/&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(**/***&&&&&&&&**&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/*&&&&&&&&&&%(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#*&&&&&&*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&%&%&&&&&&&&&&&&&&&*/&&&&&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*%&&**&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&**&&&&/&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&**(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/*/&&&&&&&&&&&&&&&&&&%#%%#(((////*****************(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(&/&&@/&(&&&*&*&&&*(&&&%#&@&&&&&&&&*((&&&*(&&&%@(&&&//&&&&#@/&&&((%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
""")
