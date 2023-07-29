# coding: utf-8
Version = '██▓▓▒▒░░ Elementary Cellular Automaton v2.3.5 (2018) ░░▒▒▓▓██'
# Written by Lucas W. in Python 3.7.0

"""Initialisation"""
try:
    from PIL import Image
    PILimported = 'successfully imported'
except ImportError:
    PILimported = 'unavailable'
    print(" - ERROR: could not import 'Image' from 'PIL'. Please view 'help image' - ")
from random import randint, choice
from time import time, sleep
scale = 32
cmd = 'none'
cmd2 = 'none'
printpattern = 1
rulenum = 110
ruletable = {"111":'0',"110":'1',"101":'1',"100":'0',"011":'1',"010":'1',"001":'1',"000":'0'}
array = '0'*scale + '1' + scale*'0'
hiddenarray = array
lastarray = 'none'
secondlastarray = 'none'
historytype = '0'
history_1 = len(array)*'0'
boundary = 'wrap'
iterations = scale
order = 0 #0 = first order, 1 = second order
displayether = 1
shift = 0
linenumbers = 10
probabilitypool = '10' #50% 1s and 50% 0s
probabilitypoolplus = ['00','11']
seedlength = len(array)
terminaldisplaylimit = 40000
printdict_presets = {
'standard' : {'1':'█', '0':'░', '3':'▓', '2':'▒', '�':'�'},
'2' : {'1':'██', '0':'░░', '3':'▓▓', '2':'▒▒', '�':'��'},
'light' : {'1':'█', '0':' ', '3':'▒', '2':'░', '�':'?'},
'light2' : {'1':'██', '0':'  ', '3':'▒▒', '2':'░░', '�':'??'},
'literal' : {'1':'1', '0':'0', '3':'3', '2':'2', '�':'�'},
'new' : {'1':'█', '0':' ', '3':'▓', '2':'▒', '�':'�'},
}
printdict = printdict_presets['standard'].copy()
if int(choice(9999*'1'+'0')): elcome = 'elcome'
else: elcome = 'halecum'
imagepath = '' # --> img.save(imagepath + imagename)
noneimage = [
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0',
'0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0',
'0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0',
'0', '1', '0', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '1', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
]
imagedata = [noneimage, 17, 6, 'none.png']
previmagedata = imagedata #previmagedata is used only for merging patterns
infotext = [
"""¦
¦    The Elementary Cellular Automaton (ECA) is the simplest kind of
¦    automaton, because every generation can expressed as an array of bits,
¦    which makes it possible to visualise the development of a system as
¦    two-dimensional pattern.
¦
¦    Based on given rules it can be determined what state
¦    (for a binary automaton: 1 = 'alive' and 0 = 'dead')
¦    a bit (a 'cell') is going to have in the next generation.
¦    An example:
¦
¦        ... 1 0 1 1 1 ... (gen1)
¦        ... 1 1 1 0 1 ... (gen2)
¦
¦    We can see that, from gen1, the second cell (0) changes into a 1 (it is 'born')
¦    and that the fourth cell (1) turns back into a 0 (it 'dies').
¦    Note how the middle cell (1) does not change its state.
¦    The corresponding rulebits look like this:
¦
¦        [1 0 1] -> 1 and [1 1 1] -> 0 and [0 1 1] -> 1
¦
¦    An ECA rule is defined by exactly these rulebits,
¦    which contain the instructions for every single configuration
¦    a cell and its two neighbouring cells can have.
¦    (1 cell + 2 neighb.: 2^3 = 8 configurations,
¦    two outcomes for a cell: 2^8 = 256 rules)
¦    The behaviour of a specific rule is not always clear and some even be able to
¦    create total randomness, even from simple initial conditions (cf. rule 30).
¦
¦    The sources used for this small project can be accessed by typing 'articles'.
¦    The articles linked there provide more in-depth information and explanations.
¦
¦    This script was originally written purely out of interest to the topic,
¦    though it also served as an excellent extracurricular programming exercise.
¦    (That also explains why the code is ugly and inefficient)
¦
¦    This script's capabilities include but are not limited to:
¦    - Simulation of all 256 ECA rules in arbitrary space
¦     + Random, complementary and mirrored rules or seeds
¦     + Direct rule modifications and common seed manipulations
¦    - Second-order ECA rules and their reversion
¦    - Basic Rule 110 glider syntax and ether detection
¦    - Basic image export of generated patterns
¦    Information, examples and sources can be accessed, respectively
¦    A full list of commands can be viewed using 'commands' or 'cmd'
¦
¦ Written by Lucas W. in Python 3.7.0
¦ Special thanks to: My comrade Dave for not not supporting me
¦                    My teacher Mr. Liebich for giving his computer science course
¦"""]
links = [
"""¦ General articles:
¦ - en.wikipedia.org/wiki/Elementary_cellular_automaton
¦ - mathworld.wolfram.com/ElementaryCellularAutomaton.html
¦ - Rules overview: plato.stanford.edu/entries/cellular-automata/supplement.html
¦ - Beginner-friendly thesis: brage.bibsys.no/xmlui/handle/11250/258721""",
"""¦ Rule 110:
¦ - Website dedicated to rule110: uncomp.uwe.ac.uk/genaro/Rule110.html
¦ - Universality in rule 110: wpmedia.wolfram.com/uploads/sites/13/2018/02/15-1-1.pdf
¦ - Glider notation: uncomp.uwe.ac.uk/genaro/rule110/listPhasesR110.txt
¦ - Gliders display: uncomp.uwe.ac.uk/genaro/rule110/glidersRule110.html""",
"""¦ Interesting pages from Stephen Wolfram's 'A New Kind of Science':
¦ - Sensitivity to initial conditions: wolframscience.com/nks/p250
¦ - Randomness in rule30: wolframscience.com/nks/p261
¦  + Randomness in rule90: wolframscience.com/nks/p264
¦  + Randomness in rule90/rule22: wolframscience.com/nks/p265
¦  + Randomness from simplicity: wolframscience.com/nks/p315
¦ - Cellular automaton in nature: wolframscience.com/nks/p423
¦ - 2.Order automata and reversibility: wolframscience.com/nks/p437
¦ - Probabilistic automata: wolframscience.com/nks/p591
¦ - Rule behaviour examples: wolframscience.com/nks/p597
¦ - Sequences in ECA: wolframscience.com/nks/p641
¦  + Prime-generating CA: wolframscience.com/nks/p640""",
"""¦ Scripts/sites to generate/view ECA patterns:
¦ - Browser: devinacker.github.io/celldemo/
¦ - Browser: xanxys.net/ecax/
¦ - Browser, pre-generated: emergentmind.com/elementary-cellular-automata
¦ - Browser, live script: khanacademy.org/computer-programming/showcase-elementary-cellular-automaton/5442204856221696
¦ - Wolfram: demonstrations.wolfram.com/CellularAutomatonExplorer
¦ - Python: youtube.com/watch?v=vhHuHXY04no
¦ - Python: rosettacode.org/wiki/Elementary_cellular_automaton#Python:_wrap""",
"""¦ Other articles:
¦ - Second order automata: en.wikipedia.org/wiki/Second-order_cellular_automaton
¦ - Additive rules: mathworld.wolfram.com/AdditiveCellularAutomaton.html""",
"""¦ PIL Help:
¦ - Pillow: pypi.org/project/Pillow
¦ - Pip install: pip.pypa.io/en/stable/installing""",
]
gliderlexicon = { #A collection of basic rule110 glider sequences
'e':'11111000100110', #14
'A':'111110', #6
'B':'11111010', #8
'B-':'1111100010110111100110', #22
'B^':'111110001011011110011001111111000100110', #39
'C':'111110000', #9
'C2':'11111000000100110', #17
'C3':'11111011010', #17
'D':'11111000010', #11
'D2':'1111101011000100110', #19
'E':'1111100000000100110', #19
'E-':'111110000100011111010', #21
'F':'111110001011010', #15
'G':'111110100111110011100110', #24
'H':'11111000101100000000111110001001101001111111000100110', #53
'Gun':'11111010110011101001100101111100000100110', #41
}
examples = {
'1' : ["Slanted Sierpinski Fractal (rule 60)", "60;0;10000000000000000000000000000000000000000000000000000000000000000;64;wrap;0"],
'2' : ["Pascal's triangle modulo 2 (rule 90)", "90;0;00000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000;50;wrap;0"],
'3' : ["Particle collision simulation (rule 184)", "184;0;10011000010110001010111001001011010010110100100110101101011101111110010111100000101000001110101111110;50;wrap;0"],
'4' : ["Triangular fractal pattern (rule 150)", "150;0;000000000000000000000000010000000000000000000000000;50;wrap;0"],
'5' : ["Chaos even from simple conditions (rule 30)", "30;0;000000000000000000000000010000000000000000000000000;50;wrap;0"],
'6' : ["Rule with growth behaviour of sqrt(x) (rule 106)", "106;0;00000000000000000000000011000000000000000000000000;50;wrap;0"],
'7' : ["Rule 110 example; type 'rule110 ether' to hide repeating tiles! (rule 110)", "110;0;11111011111000100110111110000001001101111100010011011111010;100;wrap;0"],
'8' : ["Example of a 2nd-order, reversible seed (rule 214R)", "214;1;011000100100111111110101010000111000100001000011110;50;wrap;custom;100100000110000010101111001011111011100001110000011"],
'9' : ["Interesting looking rule with individual compartments (rule 73R)", "73;1;11011010010100000001111000111101110011111001100011100001011010110000011110001110100010011010100101100;100;wrap;seed"],
'10' : ["Carpet-pattern-rule (rule 150R)", "150;1;0000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000;151;0;0"],
'11' : ["Chaotic rule distantly resembling organic tissue (rule 105R)", "105;1;110000110000110100110011101101001011111000101011011;50;wrap;seed"],
'12' : ["Rule that turn out to be example 4 but rotated 90 degrees (rule 60R)", "60;1;1000000000000000000000000000000000000000000000000000000000000000;64;wrap;0"],
'13' : ["'Inverted'-rule-version of example 9 (rule 146)", "146;1;0100011011000110111111010010100011000110001011010100011111010010;64;wrap;seed"],
'14' : ["An interesting 2nd-order rule (rule 210R)", "210;1;000000000000000000000000010000000000000000000000000;25;wrap;seed"],
'15' : ["Another interesting 2nd-order rule (rule 202R)", "202;1;0111000010101000010101000000011010011101010101110001111011110010;64;wrap;0"],
'16' : ["And another one (rule 218R)", "218;1;1010001110110100100100001110011001001001111111001100010010001000;64;wrap;0"],
'17' : ["Pattern with horizontal symmetry axis (rule 90R)", "90;1;11110001111000111100011001111111101010111011011011;50;wrap;seed"],
}
trivia = [
"¦ Rules that are their own mirror images\n¦ are called 'amphichiral' (64 out of the 256 rules have that property)",
"¦ Every 2nd-order automaton is reversible.",
"¦ The middle column of rule 30 was used as\n¦ a Pseudo Random Number Generator for Mathematica\n¦ (modern technical computing system by Stephen Wolfram).",
"¦ Rule 90 is Pascal's Triangle modulo 2 with empty cells between every number.",
"¦ Rule 110 is so-called 'Turing complete' or 'universal',\n¦ because give infinite sample space, it could simulate any possible algorithm.",
"¦ Rule 30 patterns appear on th shell of Conus Textile,\n¦ a species of sea snails.",
"¦ Rule 184 can be used as a simple model for traffic flow in a single lane of a highway,\n¦ and forms the basis for many cellular automaton models of\n¦ traffic flow with greater sophistication (wikipedia.org/wiki/rule_184)",
"¦ There are Cellular Automata (not Elementary),\n¦ that are able to display all prime numbers\n¦ by using the Sieve of Eratosthenes method.",
"¦ An additive cellular automaton is a cellular automaton,\n¦ whose rule is compatible with an addition of states (mathworld.wolfram).\n¦ The 8 additive rules are: 0, 60, 90, 102, 150, 170, 204 and 240.",
"¦ There different kinds of randomness\n¦ that can be produced from different ECA rules.\n¦ For example, rule 30 will in nearly all casesproduce random behaviour,\n¦ even from simple rules, whereas rule 90 cannot intrinsically\n¦ produce random patterns on its own.",
"¦ The fastest that information can travel\n¦ through a cellular grid in an ECA is 1 cell per time step:\n¦ this is sometimes referred to as the 'speed of light'.",
"¦ Every pattern with a finite array provably has a finite periodicity.\n¦ The reason is easy to understand:\n¦ There are only finitely many different configurations an array can take on.\n¦ In the worst-case scenario a pattern will have a\n¦ repeating period of 2^n where n is the length of the array.",
]
cmdlexicon = {
'cells':{
 'names':['cells', 'cell'],
 'none' : "Manually change how cell states are printed in terminal"
},
'commands':{
 'names':['commands', 'cmd', 'cmds', 'command'],
 'none' : "Prints a complete list of all available commands"
},
'data':{
 'names':['data', 'debug', 'scriptvalues'],
 'none' : "Displays all settings of current script"
},
'edges':{
 'names':['edges', 'edge', 'boundary', 'boundaries'],
 'none' : "How the edges/boundaries of a row are treated\n¦     [type]: Either '0', '1' or 'wrap'"
 },
'examples':{
 'names':['examples', 'eg', 'example', 'ex'],
 'none' : "A list of examples that can be displayed\n¦     [number]: If given it will display the specific example"
 },
'exit':{
 'names':['exit', 'exit()'],
 'none' : "Quits the script"
 },
'funfact':{
 'names':['funfact', 'fact', 'funfacts'],
 'none' : "Tells one of several /interesting/ facts about cellular automata"
 },
'help':{
 'names':['help', '?'],
 'none':"Opens the Help Menu\n¦     [command]: If given will show help to the chosen command"
 },
'history':{
 'names':['history', 'predecessor'],
 'none' : "Lets user define pre-initial array (seed before starting seed)\n¦     [type]: Either '0', '1', 'seed' or a custom seed (with length equal to array)"
 },
'image':{
 'names':['image', 'png', 'save', 'show'],
 'none' : f"Saves last pattern as PNG and opens it (PIL status: {PILimported})\n¦  - 'save [filename]': Just saves the image and does not show it\n¦  - 'show': Just shows the image and does not save it\n¦     [filename]: Optional custom name for the file (with file extension: 'example.png')\n¦     PIL help: Try installing PIL (Python Imaging Library) and restarting the script:\n¦     > 'pip install Pillow' (alternatively > 'python -m pip install --user Pillow')\n¦     If this doesn't fix the problem please view the info under 'links'->'PIL Help'"
 },
'imagepath':{
 'names':['imagepath', 'path'],
 'none' : "The subfolder in which the images are saved\n¦     <path>: The path, starting from where this script is located (of the form: 'folder/[subfolders/]')"
 },
'info':{
 'names':['info', 'information', 'about', 'eca'],
 'none' :  "Shows information about elementary cellular automata and this script"
 },
'iterations':{
 'names':['iterations', 'iter', 'generations', 'gen', 'height', 'rows'],
 'none' : "Defines how many rows are generated\n¦     [number]: If given will directly define iteration count"
 },
'limit':{
 'names':['limit', 'displaylimit', 'terminaldisplaylimit'],
 'none' : "Sets limit of how many cells per pattern can be printed in terminal\n¦     <number>: Total cell count"
 },
'linenumbers':{
 'names':['linenumbers', 'rows', 'rownumbers', 'label', 'rowlabel'],
 'none' : "Displays line/generation/row-number when printing the pattern\n¦     <number>: Every n-th row will be labeled"
 },
'links':{
 'names':['links', 'link', 'articles', 'sources'],
 'none' : "Shows a list of articles that provide credit and better explanations"
 },
'merge':{
 'names':['merge', 'compare', 'comparison'],
 'none' : "Prints a comparison pattern of the previous run based on the marked pattern",
 'set': "Sets the base pattern to which make comparisons",
 'image' : "Saves and displays comparison image and a difference map\n¦  + 'merge save': Causes the image to just be saved and not displayed"
 },
'order':{
 'names':['order'],
 'none' : "Toggles the order of the cellular automaton (first <-> second)"
 },
'preset':{
 'names':['preset', 'presets', 'pre'],
 'none': "Opens menu from which further subcommands of 'preset' can be accessed",
 'pattern' : "Possibility to generate a pattern preset with square size and specific seed",
 'cells' : "Presets on how to print the cell states (1s and 0s) in terminal",
 'get' : "Generates an information string to load a pattern using 'preset insert'",
 'load' : "Loads pattern from information string generated using 'preset get'"
 },
'print':{
 'names':['print'],
 'none' : "Prints the pattern in terminal",
 'small' : "Prints the pattern using unicode block characters \n      (note: empty tiles depend on the normal texture for a 0-state cell)",
 'small2' : "Same functionality as 'small' but with double the width"
},
'print_all':{
 'names':['print_all'],
 'none' : "Applies current settings to each of the 256 ECA rules and prints them all",
 '+save' : "Prints_all and saves them (subfolder must be entered, e.g. 'subfolder/')\n¦    (note: 'justsave' instead of 'save' causes the images to just be saved and not printed)"
 },
'python':{
 'names':['python', 'py', 'exec', 'execute', 'python3'],
 'none' : "Simulates a Python shell"
},
'reset':{
 'names':['reset'],
 'none' : "Used to reset all script values"
 },
'rr':{
 'names':['rr', 'randomrule', 'randrule'],
 'none' : "Randomises the rule and directly prints the pattern (see 'rule random')"
 },
'rs':{
 'names':['rs', 'randomseed', 'randseed'],
 'none' : "Randomises the seed (using current item pool) and directly prints the pattern (see 'seed random')"
 },
'rs+':{
 'names':['rs+', 'randomseed+', 'randseed+'],
 'none' : "Randomises the seed (using current item pool+) and directly prints the pattern (see 'seed random+')"
 },
'rule':{
 'names':['rule'],
 'none' : "Sets the rule using its decimal number (Wolfram notation; whole number from 1 to 255)\n¦     [number]: If given will directly set rule",
 'mirror' : "Mirrors the rule's properties in the vertical axis",
 'random' : "Generates a random rule (whole number from 1 to 255)",
 'invert' : "Returns the complementary rule",
 'manual' : "Lets one define a standard ECA rule",
 'bits' : "Lets the user define arbitrary rulebits (e.g. '211 0')"
 },
'rule110':{
 'names':['rule110', 'r110'],
 'none': "User can input gliders and own strings for rule 110\n¦    (in Cook's notation or in binary, e.g. 'e e B^ 010100 C C2 Gun e')",
 'ether' : "Toggles display of 'ether'-tiles in rule 110 patterns"
 },
'run':{
 'names':['run', '<enter>', 'pattern'],
 'none' : "Generates the pattern resulting from the current settings (and tries to print it)",
 'continue' : "Takes last row from the previous pattern as new seed and runs it",
 'reverse' : "Takes the last pattern and runs it backwards (iff 2nd-order)"
},
'seed':{
 'names':['seed', 'array', 'width', 'columns'],
 'none' : "The initial state for the pattern (binary number with arbitrary length)\n¦    (states other than 1 or 0 must be entered manually (see 'rule bits')\n¦    or else will return an error when trying to generate a pattern)",
 'random' : "Generates a random seed\n¦    (e.g. an input '00011' will return a random seed with 60% 0s and 40% 1s)",
 'random+' : "Generates a random seed\n¦    (e.g. an input '000;11' will return a random seed with 50% '000's and 50% '11's)",
 'mirror' : "Mirrors the seed in vertical axis",
 'invert' : "Inverts the current seed",
 'single' : "Generates a seed with a single cell on the left, right or in the center",
 'length' : "Extends current seed (with 0s) or crops to desired length",
 'decode' : "Takes a non-binary-digit input and decodes it into a binary seed",
 'center' : "Takes a certain seed and fits it into the center of an array of zeroes"
},
'settings':{
 'names':['settings', 'sett', 'current', 'options'],
 'none' : "Displays the current settings"
},
'shift':{
 'names':['shift', 'slant'],
 'none' : "Moves each row a certain value to the right after each generation\n¦     <number>: (Can be negative to shift to the left)"
},
}

"""Functions"""
def binary(number):
    try:
        return "{:08b}".format(number)
    except ValueError:
        return "N/A"
def new_ruletable(rulenum): #sets a new rule (integer) x as a dictionary of standard rulebits
    rule_bin = binary(rulenum) #110 -> '01101110'
    bits = ['{:03b}'.format(i) for i in range(8)][::-1] #['111', '110', '101', '100', '011', '010', '001', '000']
    ruletable = {bits[i]:rule_bin[i] for i in range(8)}
    return ruletable
def new_ruletable_manual(): #A standard rule can be defined by manually inserting rulebits
    ruletable_template = new_rule(0) #standard: rule 0
    for i in ruletable_template:
        ui = input("¦ Insert new state for the configuration '%a'\n¦> " % i)
        if ui:
            ruletable_template[i] = ui[:1]
        else:
            break
    rulenum = int(''.join(ruletable.values()), 2)
    return new_ruletable(rulenum), rulenum
def rule110_convert(inputarray): #decodes a string of rule 110 notation into binary array
    inputarray = inputarray.split(' ')
    outputarray = ''
    for i in inputarray:
        if i in gliderlexicon:
            outputarray += gliderlexicon[i]
        elif i.replace('1','').replace('0','') == '': #adds the input if it is purely binary
            outputarray +=  i
    return outputarray
def rule110_ether(inputarray, history_1, history_2, history_3): #I spent a lot of time on trying to make this work and it finally did (very inefficiently)
    k = 7 #fixes some recognition errors on the sides
    x = inputarray[-k:] + inputarray + inputarray[:k]
    h_1 = history_1[-k:] + history_1 + history_1[:k]
    h_2 = history_2[-k:] + history_2 + history_2[:k]
    h_3 = history_3[-k:] + history_3 + history_3[:k]
    while x.count('1000'): #searches, whether there are any '1000'-sequences in array
        index = x.index('1000') #check this particular instance of '1000'
        if h_1[index+1:index+6] == '11110': #if it is part of a certain tile:
            x = x.replace('1000','3222',1) #replace with appropriate cell states
        else: #otherwise mark as done:
            x = x.replace('1000',';000',1)
    while x.count('1001'):
        index = x.index('1001')
        if h_2[index+1:index+6] == '11110':
            x = x.replace('1001','3223',1)
        else:
            x = x.replace('1001',';001',1)
    while x.count('10'):
        index = x.index('10')
        if h_3[index+1:index+6] == '11110':
            x = x.replace('10','32',1)
        else:
            x = x.replace('10',';0',1)
    x = x.replace(';','1') #resets all sequences previously marked as done
    for i in range(2): #TODO (efficiency)
        x = x.replace('0111110','0333310')
        x = x.replace('0111132','0333332')
        x = x.replace('2111110','2333310')
        x = x.replace('2111132','2333332')
        x = x.replace('2311110','2333310')
        x = x.replace('2311132','2333332')
    return x[k:-k]
def history(historytype, array, history_1): #Makes history
    historytypes = {
    'custom':history_1,
    '0':len(array)*'0',
    '1':len(array)*'1',
    'seed':array}
    if historytype in historytypes:
        return historytypes[historytype]
    else:
        return historytypes['0']
def script_id_generate(): # 64^4 = 16.777.216 different script ids
    return ''.join([ choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_') for i in range(4) ])
def preset_data_generate(): #generates compressed info string to 'save' patterns
    if historytype == 'custom':
        return "{0};{1};{2};{3};{4};{5};{6}".format(rulenum, order, array, iterations, boundary, historytype, history_1)
    else:
        return "{0};{1};{2};{3};{4};{5}".format(rulenum, order, array, iterations, boundary, historytype)
def insert_data(raw_data, history_1): #translates compressed info string to load patterns
    preset_data = raw_data.split(';')
    rulenum = int(preset_data[0])
    ruletable = new_ruletable(rulenum)
    order, array, iterations, boundary, HT_temp = int(preset_data[1]), preset_data[2], int(preset_data[3]), preset_data[4], preset_data[5]
    if HT_temp in ['0', '1', 'seed']:
        historytype = HT_temp
        history_1 = history(historytype, array, history_1)
    elif HT_temp == 'custom':
        try:
            assert len(preset_data[6]) == len(array)
            historytype = 'custom'
            history_1 = preset_data[6]
        except:
            historytype = '0'
            history_1 = history(historytype, array, history_1)
            print("¦ Faulty custom history data, history type changed to '0' (standard)")
    else:
        historytype = '0'
        history_1 = history(historytype, array, history_1)
    return ruletable, rulenum, order, array, iterations, boundary, historytype, history_1
def data_show(displaytype): #displays data
    scriptvalues = [
    'Current preset/pattern data : {}'.format(preset_data_generate()),
    f'Current rule is {rulenum}',
    f'(Rule in binary: {binary(rulenum)})',
    'All rule bits : {}'.format(', '.join([j+'-'+ruletable[j] for j in ruletable])),
    f'Current number of iterations/generations is {iterations}',
    f'Inital seed (length={len(array)}):\n¦ {array}',
    f'Pre-initial seed (type={historytype}):\n¦ {history_1}',
    f"`1`s are printed as {printdict['1']!r}",
    f"`0`s are printed as {printdict['0']!r}",
    f'Mode is currently set to {"second" if order else "first"}-order automaton',
    f'{"The automaton wraps around at the edges" if boundary == "wrap" else f"Automaton simulates a column of {boundary} at the edges"}',
    'Probability pool for random seeds : {}'.format(', '.join(probabilitypool)),
    'Advanced probabilitypool : {}'.format(', '.join(probabilitypoolplus)),
    f'{"Ether-tiles are diplayed normally" if displayether else "Ether-tiles are printed using state 2 and 3 cells (slightly lighter)"}',
    f'The rows/generations of a pattern are labeled every {linenumbers}. row (0 = no labeling)',
    f'Every row is shifted to the right by {shift}',
    #f'Last printed array of last pattern:\n¦ {lastarray}',
    #f'Last generated array of last pattern (not displayed):\n¦ {hiddenarray}',
    f'Current script ID: {scriptid}',
    f'Number of commands executed: {runid}',
    f'Name of last pattern: {imagedata[3]}',
    f'Images are automatically saved at: (script location)/'+imagepath,
    'Number of total cells in current pattern is {:,}'.format(len(array)*iterations),
    f'Cell display limit lies at {terminaldisplaylimit:,} cells',
    ]
    if displaytype == 'all':
        print("¦\n¦ ██▓▓▒▒░░ All Current Settings ░░▒▒▓▓██\n¦")
        for i in scriptvalues:
            print(i)
    elif displaytype == 'simple':
        specific_display = [1,2,4,5,7,8,9]
        print("¦\n¦ ██▓▓▒▒░░ Current Settings ░░▒▒▓▓█\n¦")
        for i in specific_display:
            print(f"¦ {scriptvalues[i]}\n¦")
def pattern_show(imgdata, prntdict):
    error_pattern = 0
    for row in range(imgdata[2]):
        try:
            print(''.join([ prntdict[str(i)] for i in imgdata[0][ row*imgdata[1]:(row+1)*imgdata[1] ] ]) + ('-'+str(row+1) if linenumbers and not (row+1)%linenumbers else ''))
        except:
            if not error_pattern:
                error_pattern = 1; print(" - WARNING: Array contains unknown cell states (have no texture). - ")
            for cell in imgdata[0][ row*imgdata[1]:(row+1)*imgdata[1] ]:
                try:
                    print(prntdict[str(cell)], end='')
                except:
                    prntdict[str(cell)] = str(cell)
                    print(cell, end='')
            print(('-'+str(row+1) if linenumbers and not (row+1)%linenumbers else ''))
def pattern_show_2x2(imgdata):
    chars = printdict['0']+'▘▝▀▖▌▞▛▗▚▐▜▄▙▟█'
    width, height = imgdata[1], imgdata[2]
    imgstring = [[imgdata[0][row*width+cell] for cell in range(width)] for row in range(height)]
    for row in range(0, height, 2):
        for cell in range(0, width, 2):
            try:
                four_cells = [ imgstring[row+1][cell+1], imgstring[row+1][cell], imgstring[row][cell+1], imgstring[row][cell] ]
            except:
                four_cells = []
                for d in [(1, 1), (0, 1), (1, 0), (0, 0)]:
                    dx, dy = d
                    try:
                        four_cells += imgstring[row+dy][cell+dx]
                    except:
                        four_cells += '0'
            print(chars[int(''.join(four_cells), 2)], end='')
        print()
def pattern_show_1x2(imgdata):
    chars = printdict['0']+'▀▄█'
    width, height = imgdata[1], imgdata[2]
    imgstring = [[imgdata[0][row*width+cell] for cell in range(width)] for row in range(height)]
    for row in range(0, height, 2):
        for cell in range(0, width):
            try:
                two_cells = [ imgstring[row+1][cell], imgstring[row][cell] ]
            except:
                two_cells = []
                for d in [1, 0]:
                    try:
                        two_cells += imgstring[row+d][cell]
                    except:
                        two_cells += '0'
            print(chars[int(''.join(two_cells), 2)], end='')
        print()
def merge_show(mode): #merges the two patterns and saves them/prints them accordingly
    imagestring = [int(cellstate) for cellstate in imagedata[0]]
    previmagestring = [int(cellstate) for cellstate in previmagedata[0]]
    differencemap = [ (imagestring[i] ^ j)^1 for i, j in enumerate(previmagestring) ] #creates an array with 0s for changed cells
    mergedimage = [ {1:3, 0:2}[j] if not differencemap[i] else j for i,j in enumerate(previmagestring) ] #changes cells that haven't changed into 2s and 3s (modulo corresponding cell state)
    if mode == 'print':
        imagedata_merged = [mergedimage, imagedata[1], imagedata[2], imagedata[3]]
        pattern_show(imagedata_merged, {'1':printdict['3'], '0':printdict['2'], '3':printdict['1'], '2':printdict['0']})
    elif mode in ['image', 'save']:
        displaydict = {1:64, 0:128, 3:0, 2:255}
        img = Image.new('L', (imagedata[1], imagedata[2]))
        img.putdata([displaydict[i] for i in mergedimage]) #mergedimage
        imagename_merged = previmagedata[3] + '_compared_with_' + imagedata[3]
        img.save(imagepath + imagename_merged)
        if mode != 'save': img.show()
        img = Image.new('1', (imagedata[1], imagedata[2]))
        img.putdata(differencemap) #differencemap
        imagename_differencemap = previmagedata[3] + '_differencemap_' + imagedata[3]
        img.save(imagepath + imagename_differencemap)
        if mode != 'save': img.show()
        print("¦ Generated and saved files as: %s, %s" % (imagename_merged, imagename_differencemap), end='')
        if imagepath: print(" (in subfolder %a)" % imagepath)
        else: print()
def ECA(array, history_1): #THE MAIN AUTOMATA: this function prints the whole pattern
    imagestring = []
    one_tenth = round(iterations/10)
    history_2 = history_3 = len(array)*'1'
    if not displayether and not order and rulenum == 110:
        history_1  = len(array)*'1'  #to hide ether correctly
    error_eca = None
    for iter in range(iterations):
        if not displayether and not order and rulenum == 110:
            imagestring += rule110_ether(array, history_1, history_2, history_3)
        else:
            imagestring += array
        if boundary == 'wrap':
            array = array[-1]+array+array[0]
        else:
            array = boundary + array + boundary
        try:
            if order:
                newarray = [ str( int(ruletable[array[(k-1):(k+2)]]) ^ int(history_1[k-1]) ) for k in range(1, len(array)-1) ]
            else:
                newarray = [ ruletable[array[(k-1):(k+2)]] for k in range(1, len(array)-1) ]
        except: #for unknown cell configurations
            if error_eca == None: #one-time error notice
                error_eca = " - WARNING: Array contains unknown cell configurations. - "
                print(error_eca)
            newarray = []
            for k in range(1, len(array)-1):
                try:
                    if order:
                        newarray += str(int(ruletable[array[(k-1):(k+2)]])^int(history_1[k-1]))
                    else:
                        newarray += ruletable[array[(k-1):(k+2)]]
                except:
                    newarray += '�'
        newarray = ''.join(newarray)
        if shift:
            newarray = newarray[-shift:] + newarray[:-shift]
            array = array[-shift:] + array[:-shift]
            history_1 = history_1[-shift:] + history_1[:-shift]
            history_2 = history_2[-shift:] + history_2[:-shift]
        history_3, history_2, history_1, array = history_2, history_1, array[1:-1], newarray
        if not printpattern and not (iter+1) % one_tenth: #percentage for patterns that go above terminal display limit
            print( "¦ %d %% done (iter.%s)" % (100*(iter+1)/iterations, iter+1) )
    imagename = 'Rule-{}{}_({}-{}).png'.format(rulenum, ('R' if order else ''), scriptid, runid)
    imagedata = [imagestring, len(array), iterations, imagename]
    return array, history_1, history_2, imagedata #array -> hiddenarray (not printed), history_1 -> lastarray (last printed), history_2 -> secondlastarray (yes)

"""Main Loop"""
print('\n',Version,'\n')
print(f" - W{elcome}!\n - You can access help through 'help'\n - Try out some examples by typing 'examples'!\n")
scriptid = script_id_generate()
runid = 0
while True:
    if cmd in ['test' ,'hi', 'hello', 'hallo', 'hey', 'hei', 'hej']:
            print("¦ Hello World!")
            import this
    if cmd in cmdlexicon['cells']['names']:
        ui = input("¦ Insert new representation/symbol for cell state '0' (previous = %s)\n¦> " % printdict['0'])
        if ui:
            printdict['0'] = ui
        ui = input("¦ Insert new representation/symbol for cell state '1' (previous = %s)\n¦> " % printdict['1'])
        if ui:
            printdict['1'] = ui
        print("¦ Other, arbitrary cell states can now be defined, press <enter> to finish:")
        while True:
            try:
                ui_state, ui_cell = input("¦ Insert state and how to print it in the form 'X Y' (eg. '4 ▓')\n¦> ").split()
                printdict[ui_state] = ui_cell
            except:
                print("¦ Settings applied:")
                for i in printdict:
                    print("¦ '%s' = '%s'" % (i, printdict[i]))
                break
    if cmd in cmdlexicon['commands']['names']:
        print("¦ ██▓▓▒▒░░ All Available Commands ░░▒▒▓▓██\n¦")
        for i in cmdlexicon:
            print("¦ %s (names: %s)" % (i.title(), ", ".join(cmdlexicon[i]['names']) ))
            print("¦ - '%s': %s" % (i, cmdlexicon[i]['none']))
            for j in cmdlexicon[i]:
                if j not in ['names', 'none']:
                    print("¦  + '%s %s': %s" % (i, j, cmdlexicon[i][j]))
    if cmd in cmdlexicon['data']['names']:
        data_show('all')
    if cmd in cmdlexicon['edges']['names']:
        if cmd2 == 'none':
            cmd2 = input("¦ Choose boundary option (current: %a):\n¦ 'wrap': simulates an array that connects to itself on both ends\n¦ '0': boundary will be treated as static column of 0 cells\n¦ '1': boundary will be treated as static column of 1 cells\n¦> " % boundary)
        if cmd2 == 'wrap':
            boundary = 'wrap'
            print('¦ Cellular Automaton will now simulate connected / circular array (wrap)')
        elif cmd2 != '':
            boundary = cmd2[:1]
            print('¦ Cellular Automaton will simulate edges with %a-column boundary' % boundary)
    if cmd in cmdlexicon['examples']['names']:
        if cmd2 in examples:
            print("\n - Current Example: %s (Ex.%s) - " % (examples[cmd2][0], cmd2) )
            ruletable, rulenum, order, array, iterations, boundary, historytype, history_1 = insert_data(examples[cmd2][1], history_1)
            seedlength = len(array)
            cmd = 'run'
            continue
        else:
            print("¦ Available Examples (view by typing 'example <number>'):\n¦")
            for i,j in enumerate(examples):
                try:
                    print('¦',i+1,examples[j][0])
                except:
                    pass #Purposely silenced exception
    if cmd in cmdlexicon['exit']['names']:
        break
    if cmd in cmdlexicon['funfact']['names']:
        print("¦\n¦ Funfact %d:" % (runid % 12))
        print(trivia[runid % 12],"\n¦")
    if cmd in cmdlexicon['help']['names']:
        try:
            assert cmd2 in cmdlexicon
            print("¦ Other names for %s: %s" % (cmd2, ", ".join(cmdlexicon[cmd2]['names']) ))
            print("¦ - '%s': %s" % (cmd2, cmdlexicon[cmd2]['none']))
            for j in cmdlexicon[cmd2]:
                if j not in ['names', 'none']:
                    print("¦  + '%s %s': %s" % (cmd2, j, cmdlexicon[cmd2][j]))
        except:
            print("""¦
¦ ██▓▓▒▒░░ Help Menu ░░▒▒▓▓██
¦
¦ - General information about this script can be viewed using 'info'
¦ - The following is a list of common commands (case-insensitive)
¦ ( You can access info about a command using 'help <command>' )
¦
¦ run      ¦ settings  ¦ info        ¦ help     ¦
¦ rule     ¦ seed      ¦ iterations  ¦ examples ¦
¦ rule110  ¦ order     ¦ preset      ¦ image    ¦
¦ links    ¦ debug     ¦ reset       ¦ exit     ¦
¦
¦ PS: commands are case-insensitive""")

#¦ {'run':<9} {'settings':<10} {'info':<12} {'help':<10}
#¦ {'rule':<9} {'seed':<10} {'iterations':<12} {'examples':<10}
#¦ {'rule110':<9} {'order':<10} {'preset':<12} {'image':<10}
#¦ {'links':<9} {'debug':<10} {'reset':<12} {'exit':<10}"""
    if cmd in cmdlexicon['history']['names']:
        if cmd2 == 'none':
            cmd2 = input("¦ Choose history option (current: %a):\n¦ '0' or '1': an array of zeroes or ones\n¦ 'seed': takes initial seed as pre-initial array\n¦ <custom>: insert custom array (must be exactly as long as current seed)\n¦> " % historytype)
        if cmd2 == 'seed':
            historytype = 'seed'
            history_1 = array
            print("¦ Pre-inital array has been set equal to starting array")
  #History 0
        elif cmd2 == '0':
            historytype = '0'
            history_1 = len(array)*'0'
            print("¦ Pre-inital array has been changed to row of 0s")
  #History 1
        elif cmd2 == '1':
            historytype = '1'
            history_1 = len(array)*'1'
            print("¦ Pre-inital array has been changed to row of 1s")
  #History <custom>
        elif len(cmd2) == len(array):
            historytype = 'custom'
            history_1 = cmd2
            print("¦ Pre-inital array has been defined manually")
        elif cmd2 != '':
            print("¦ Invalid history option, try 'seed', '0', '1' or custom (with equal length to array)")
    if cmd in cmdlexicon['image']['names']:
        if cmd2 != 'none':
            imagename = cmd2
        else:
            imagename = imagedata[3]
        try:
            errormsg = "Cannot import 'Image' module from PIL, please view the info below"
            from PIL import Image
            errormsg = "Pattern contains unknown cell states"
            print(" - Converting array... -")
            if '2' in imagedata[0] or '3' in imagedata[0]: #stackoverflow.com/questions/2111150/create-a-grayscale-image
                mode = 'L'
                displaydict = {'3':64, '2':128, '1':0, '0':255}
                imagestring = [ displaydict[cellstate] for cellstate in imagedata[0] ]
            else:
                mode = '1'
                imagestring = [{'0':1, '1':0}[cellstate] for cellstate in imagedata[0]]
            errormsg = "[unknown cause]"
            print(" - Generating file... -")
            img = Image.new(mode, (imagedata[1], imagedata[2])) #stackoverflow.com/questions/41323761/converting-an-array-to-image
            img.putdata(imagestring)
            save_message = '¦ Generated file as:'
            if cmd != 'show':
                img.save(imagepath + imagename)
                save_message = '¦ Generated and saved file as:'
            print(save_message, imagename, end='')
            if imagepath: print(" (in subfolder %a)" % imagepath, end='')
            print()
            if cmd != 'save':
                img.show()
        except:
            print(" - ERROR: %s - " % errormsg)
            if errormsg == "Cannot import 'Image' module from PIL, please view the info below":
                print(cmdlexicon['image']['none'][-256:])
    if cmd in cmdlexicon['imagepath']['names']:
        if cmd2 != 'none':
            imagepath = cmd2
            print("¦ Saving subfolder changed to (location of script)/%a" % imagepath)
        else:
            print("¦ Invalid input, try: 'imagepath <path>'")
    if cmd in cmdlexicon['info']['names']:
        print('¦ \n¦ ',Version)
        print(infotext[0])
    if cmd in cmdlexicon['iterations']['names']:
        try:
            iterations = int(cmd2)
            print("¦ New number of generations:",iterations)
        except:
            try:
                ui = input('¦ Number of generations (previous = %d)\n¦> ' % iterations)
                iterations = int(ui)
            except:
                if ui:
                    print("¦ Invalid input.")
    if cmd in cmdlexicon['limit']['names']:
        try:
            terminaldisplaylimit = int(cmd2)
            print("¦ Terminal display limit set to %d cells" % terminaldisplaylimit)
        except:
            print("¦ Invalid input, try 'limit <number>'.")
    if cmd in cmdlexicon['linenumbers']['names']:
        try:
            linenumbers = int(cmd2)
            print("¦ Line numbers will be displayed every %d. row" % linenumbers)
        except:
            print("¦ Invalid input, try 'linenumbers <number>'")
    if cmd in cmdlexicon['links']['names']:
        print("¦\n¦ ██▓▓▒▒░░ Online Articles ░░▒▒▓▓██")
        for i in links:
            print(f'¦\n', i, sep='')
    if cmd in cmdlexicon['merge']['names']:
  #Merge set
        if cmd2 == 'set':
            previmagedata = imagedata
            print("¦ Pattern for merging/comparison set to", imagedata[3])
  #Merge image / #Merge save
        else:
            try:
                errormsg = 'Patterns are different sizes'
                assert imagedata[1] == previmagedata[1] and imagedata[2] == previmagedata[2]
                errormsg = '[unknown cause]'
                if cmd2 in ['image', 'save']:
                    merge_show(cmd2)
                else:
                    merge_show('print')
            except:
                print(" - ERROR: %s - " % errormsg)
    if cmd in cmdlexicon['order']['names']:
        order = 1^order
        print(f'¦ Type changed to %a.-order cellular automaton' % (order+1))
    if cmd in cmdlexicon['preset']['names']:
  #Preset none
        if cmd2 == 'none':
            cmd2 = input("¦ Choose a preset option:\n¦ 'pattern': Generate a preset pattern with square size and defined seed\n¦ 'cells': Preset representations for cell states in a pattern\n¦ 'get': Generates an information string that can be loaded in 'insert'\n¦ 'insert': Takes an information string to load a pattern\n¦> ")
  #Preset pattern
        if cmd2 == 'pattern':
            try:
                ui = input("¦ Input size and type as '<size> <type>' (e.g. '100 center')\n¦ Size: Any number (iterations and seedlength will be set to that number)\n¦ Types: 'random': random seed, 'left','center' or 'right': single '1' cell in the seed in that position\n¦> ")
                presetsize, presetpos = ui.split()
                size = int(presetsize)
                position_names = {'random':'random', 'rand':'random', 'left':'left', 'l':'left', 'right':'right', 'r':'right', 'center':'center', 'centre':'center', 'c':'center'}
                position_table = {
                 'left':'1'+(size - 1)*'0',
                 'center':round(size/2 - .25)*'0'+'1'+round(size/2 - .25 )*'0',
                 'right':(size-1)*'0'+'1',
                 'random':''.join([choice(probabilitypool) for i in range(size)])}
                array, iterations = position_table[position_names[presetpos]], size
                history_1, seedlength = history(historytype, array, history_1), len(array)
                print("¦ Preset applied!")
            except:
                if ui:
                    print(f'¦ Invalid input.')
  #Preset cells
        elif cmd2 in ['cells', 'cells']:
            print("¦ Available presets:")
            for i in printdict_presets:
                print("¦\n¦ %s, 0¦1¦2¦3 = %s¦%s¦%s¦%s" % (i, printdict_presets[i]['0'], printdict_presets[i]['1'], printdict_presets[i]['2'], printdict_presets[i]['3']) )
            ui = input("¦> ")
            try:
                printdict = printdict_presets[ui].copy()
                print("¦ Preset applied: 1 = '%s' 0 = '%s'" % (printdict['1'],printdict['0']))
            except:
                if ui:
                    print(f'¦ Invalid input.')
  #Preset get
        elif cmd2 == 'get':
            preset_data = preset_data_generate()
            print("¦ \n¦ Current preset:\n¦ %s\n¦ " % preset_data)
  #Preset insert
        elif cmd2 in ['load', 'insert']:
            ui = input("¦ Insert preset data ('preset get')\n¦> ")
            if ui:
                try:
                    ruletable, rulenum, order, array, iterations, boundary, historytype, history_1 = insert_data(ui, history_1)
                    seedlength = len(array)
                    print("¦ Preset applied!")
                except:
                    print("¦ Invalid input.")
    if cmd in cmdlexicon['print']['names']:
        if cmd2 in ['small', 'small2']:
            try:
                if cmd2 == 'small': pattern_show_2x2(imagedata)
                elif cmd2 == 'small2': pattern_show_1x2(imagedata)
            except:
                print("\n - ERROR: pattern contains non-binary cell states -")
        elif printpattern:
            pattern_show(imagedata, printdict)
        else:
            print("\n - The pattern contained too many cells ({:,} > {:,}) and was not printed -\n - View pattern with 'image' or redefine display limit using 'limit <cell number>' -".format(len(array)*iterations, terminaldisplaylimit))
    if cmd in cmdlexicon['print_all']['names']:
        ruletable_temp, rulenum_temp = ruletable, rulenum
        if cmd2 in ['save', 'justsave']:
            imagepath_temp = input("¦ Define subfolder to save the files in (e.g. 'subfoldername/')\n¦> ")
        for i in range(256):
            rulenum = i
            ruletable= new_ruletable(rulenum)
            print(' - Rule %d%s -' % (rulenum, ('R' if order else '')) )
            hiddenarray_temp, lastarray_temp, secondlastarray_temp, imagedata_temp = ECA(array, history_1)
            if cmd2 != 'justsave':
                pattern_show(imagedata_temp, printdict)
  #Print All +Save images
            if cmd2 in ['save', 'justsave']:
                try:
                    from PIL import Image
                    img, imagename = Image.new('1', (imagedata_temp[1], imagedata_temp[2])), imagedata_temp[3]
                    img.putdata([int(i)^1 for i in imagedata_temp[0]])
                    img.save(imagepath_temp + imagename)
                    print("¦ Generated and saved file as:",imagepath_temp, imagename)
                except:
                    print(" - ERROR: Could not generate or save image file - ")
        ruletable, rulenum = ruletable_temp, rulenum_temp
    if cmd in cmdlexicon['python']['names']:
        python_code = ''
        ui = input("¦ Python 3.7.0\n>>> ")
        while ui != '\n':
            python_code += ui
            ui = '\n' + input("... ")
        try:
            exec(python_code)
        except:
            print(" - ERROR: Something went wrong! :( - \n¦ Entered code:\n¦ >>> %s" % (python_code))
    if cmd in cmdlexicon['reset']['names']:
        printpattern = 1
        rulenum = 110
        ruletable = {"111":'0',"110":'1',"101":'1',"100":'0',"011":'1',"010":'1',"001":'1',"000":'0'}
        array = '0'*scale + '1' + scale*'0'
        hiddenarray = array
        lastarray = 'none'
        secondlastarray = 'none'
        historytype = '0'
        history_1 = len(array)*'0'
        boundary = 'wrap'
        iterations = scale
        order = 0
        printdict = {'1':'█', '0':'░', '3':'▓', '2':'▒'}
        displayether = 1
        shift = 0
        linenumbers = 10
        probabilitypool = '10'
        probabilitypoolplus = ['00','11']
        seedlength = len(array)
        terminaldisplaylimit = 40000
        imagepath = ''
        imagedata = [noneimage, 17, 6, 'none.png']
        previmagedata = imagedata
        cmd, cmd2 = 'none', 'none'
        print("\n - RESET: All script data and values have been reset. - \n")
        continue
    if cmd in cmdlexicon['rr']['names']:
        rulenum = randint(1,255)
        ruletable = new_ruletable(rulenum)
        cmd = 'run'
        continue
    if cmd in cmdlexicon['rs']['names']:
        array = ''
        for m in range(0, seedlength):
            array = array+choice(probabilitypool)
        history_1 = history(historytype, array, history_1)
        cmd = 'run'
        continue
    if cmd in cmdlexicon['rs+']['names']:
        testarray, lasttestarray = '', ''
        while len(testarray) <= seedlength:
            testarray, lasttestarray = testarray+choice(probabilitypoolplus), testarray
        array = lasttestarray
        history_1 = history(historytype, array, history_1)
        cmd = 'run'
        continue
    if cmd in cmdlexicon['rule']['names']:
  #Rule <number>
        if cmd2 != 'none':
            try:
                rulenum = int(cmd2)
                ruletable = new_ruletable(rulenum)
                print(f'¦ New rule:',rulenum)
            except:
                pass
  #Rule none
        if cmd2 == 'none':
            try:
                ui = input(f'¦ Input rule number (integer between 1 and 255)(previous rule: %d)\n¦> ' % rulenum)
                rulenum = int(ui)
                ruletable = new_ruletable(rulenum)
                print(f'¦ New rule:',rulenum)
            except:
                if ui:
                    print("¦ Invalid input.")
  #Rule random
        elif cmd2 in ['random', 'rand']:
            rulenum = randint(1, 255)
            ruletable = new_ruletable(rulenum)
            print(f'¦ New rule:',rulenum)
  #Rule mirror
        elif cmd2 in ['mirror', 'mirrored'] and rulenum != 'custom':
            rule_bin = list(binary(rulenum))
            rule_bin[1],rule_bin[4] = rule_bin[4], rule_bin[1]
            rule_bin[3], rule_bin[6] = rule_bin[6], rule_bin[3]
            rulenum = int(''.join(rule_bin), 2)
            ruletable= new_ruletable(rulenum) #defines the mirrored rule
            print(f'¦ New rule:',rulenum)
  #Rule invert
        elif cmd2 in ['invert', 'complement', 'complementary'] and rulenum != 'custom':
            rule_bin = binary(rulenum).replace('1',';').replace('0','1').replace(';','0')[::-1]
            rulenum = int(rule_bin, 2)
            ruletable = new_ruletable(rulenum)
            print(f'¦ Note: to obtain the exact complementary pattern both rule and seed have to be inverted.\n¦ New (complementary) rule: ',rulenum)
  #Rule manual
        elif cmd2 == 'manual':
            #try:
                ruletable, rulenum = new_ruletable_manual()
                print(f'¦ New rule:',rulenum)
            #except:
                print("¦ Invalid input.")
  #Rule bits
        elif cmd2 in ['bits', 'bit']:
            print(f'¦ Current rule bits (%d):' % len(ruletable))
            for i in ruletable:
                print(f'¦ ',i,':',ruletable[i])
            print("¦ Rulebits have to be of the form 'XYZ W' to be accepted (e.g.'101 1')\n¦ An arbitrary amount of configurations can be defined, press <enter> to apply:")
            while True:
                try:
                    ui_config, ui_result = input("¦> ").split()
                    ruletable[ui_config[:3]] = ui_result[:1]
                except:
                    print("¦\n¦ Rulebit modifications completed (WARNING: saving custom rules is not supported)")
                    break
            print(f"¦ NOTICE: Rule is now marked as 'custom', type 'rule {rulenum}' to undo changes.")
            rulenum = 'custom'
    if cmd in cmdlexicon['rule110']['names']:
  #Rule110 none
        if cmd2 == 'none':
            ui = input("¦ Gliders must be of the following (Cook's) notation:\n¦ GLIDERS: A B B- B^ C C2 C3 D D2 E E- F G H\n¦ ETHER(T3 tiles): e ;GLIDER GUNS: Gun ;<OWN GLIDERS>: must be given in binary\n¦> ")
            if ui:
                array = rule110_convert(ui)
                history_1 = history(historytype, array, history_1)
                ruletable, rulenum = new_ruletable(110), 110
                seedlength = len(array)
                print(f'¦ New seed (length %d): %a' % (len(array), array))
  #Rule 110 ether
        elif cmd2 in ['ether', 't3']:
            displayether = displayether^1
            if displayether:
                print(f'¦ Ether tiles are displayed normally again')
            else:
                print(f'¦ Ether tiles will be shown differently')
    if cmd in cmdlexicon['run']['names']:
        if cmd2 in ['continue', 'c']:
            array, history_1 = hiddenarray,lastarray
        elif cmd2 in ['reverse', 'r']:
            array, history_1 = lastarray, hiddenarray
        print('\n - Rule %a%s (seedlength %a and %a iterations %s) -' % (rulenum, ('R' if order else ''), len(array), iterations, ("and shift {}".format(shift) if shift else '') ) )
        ECA_start = time()
        hiddenarray, lastarray, secondlastarray, imagedata = ECA(array, history_1)
        print('¦ (Finished pattern calculation after {:.3f} seconds)'.format(time() - ECA_start))
        cmd, cmd2 = 'print', 'none'
        continue
    if cmd in cmdlexicon['seed']['names']:
  #Seed none
        if cmd2 == 'none':
            ui = input(f'¦ Current seed (%d cells long):\n¦%s\n¦ Enter new seed (1s and 0s):\n¦> ' % (len(array),array) )
            if ui:
                array = ui
                history_1, seedlength = history(historytype, array, history_1), len(array)
                print("¦ New seed (length %d), type 'settings' to see it" % len(array))
  #Seed random
        elif cmd2 in ['random', 'rand']:
            ui = input("¦ Insert new probability pool (e.g.: 50% of each = '10' or '0110' etc.)\n¦> ")
            if ui:
                probabilitypool = ui
                array = ''
                for m in range(0,seedlength):
                    array = array+choice(probabilitypool)
                    history_1 = history(historytype, array, history_1)
                print(f'¦ New seed (length %d): "%s"' % (len(array), array))
  #Seed random+
        elif cmd2 in ['random+', 'rand+']:
            ui = input("¦ Insert new probability pool, seperate elements with commas (e.g.: '00,11')\n¦> ")
            if ui:
                probabilitypoolplus = ui.split(',')
                testarray, lasttestarray = '', ''
                while len(testarray) <= seedlength:
                    testarray, lasttestarray = testarray+choice(probabilitypoolplus), testarray
                array = lasttestarray
                history_1 = history(historytype, array, history_1)
                print(f'¦ New seed (length %d): "%s"' % (len(array), array))
  #Seed mirror
        elif cmd2 == 'mirror':
            array = array[::-1]
            history_1 = history(historytype, array, history_1)
            print(f'¦ New seed (length %d): "%s"' % (len(array), array))
  #Seed invert
        elif cmd2 == 'invert':
            array = array.replace('1',';').replace('0','1').replace(';','0')
            history_1 = history(historytype, array, history_1)
            print(f'¦ New seed (length %d): "%s"' % (len(array), array))
  #Seed single
        elif cmd2 == 'single':
            ui = input(f'¦ Should the single cell to be on the left, right or in the center?\n¦> ').lower()
            try:
                position_names = {'left':'left', 'l':'left', 'right':'right', 'r':'right', 'center':'center', 'centre':'center', 'c':'center'}
                position_table = {'left':'1'+(len(array)-1)*'0', 'center':round( len(array)/2-.25 )*'0'+'1'+round( len(array)/2-.25 )*'0', 'right':(len(array)-1)*'0'+'1'}
                array = position_table[position_names[ui]]
                history_1, seedlength = history(historytype, array, history_1), len(array)
                print(f'¦ New seed:',array)
            except:
                if ui:
                    print("¦ Invalid input.")
  #Seed length
        elif cmd2 == 'length':
            try:
                ui = input( f'¦ Desired length of seed (crops seed / extends with 0s) (previous: %d)\n¦> ' % len(array) )
                seedlength = int(ui)
                if len(array) < seedlength: #if array shorter than expected length
                    array = array + (seedlength-len(array))*'0'
                    print(f'¦ New seed (length %d): "%s"' % (len(array), array))
                elif len(array) > seedlength: #if array longer than expected length
                    array = array[:seedlength]
                    print(f'¦ New seed (length %d): "%s"' % (len(array), array))
                else: #if array already expected length
                    print(f'¦ Seed is already %d cells long!' % seedlength)
                history_1 = history(historytype, array, history_1)
            except:
                if ui:
                    print("¦ Invalid input.")
  #Seed decode
        elif cmd2 == 'decode':
            ui_seed = input(f'¦ Insert seed to decode\n¦> ')
            ui_one = input(f'¦ Input character/string 1\n¦> ')
            ui_zero = input(f'¦ Input character/string for 0\n¦> ')
            array = ui_seed.replace(ui_one,'1').replace(ui_zero,'0')
            history_1, seedlength = history(historytype, array, history_1), len(array)
            print(f'¦ New seed (length %d): "%s"' % (len(array), array))
  #Seed center
        elif cmd2 == 'center':
            ui = input("¦ Insert partial seed to center in an array of zeroes:\n¦> ")
            if ui:
                rest_of_seed = round( (seedlength-len(ui))/2-.25 )
                array = rest_of_seed*'0' + ui + rest_of_seed*'0'
                print(f'¦ New seed (length %d): "%s"' % (len(array), array))
    if cmd in cmdlexicon['settings']['names']:
        data_show('simple')
    if cmd in cmdlexicon['shift']['names']:
        try:
            shift = int(cmd2)
            print("¦ Rows will each be shifted to the right by %d (each generation)" % shift)
        except:
            print("¦ Invalid input, try 'shift <number>'")
    if len(array) < 3:
        print("\n - Array was too shorter than three cells and therefore reset. -")
        array = '0'*scale + '1' + scale*'0'
        seedlength = len(array)
    if iterations < 1:
        print("\n - Iteration number was smaller than 1 and therefore reset. -")
        iterations = scale
    printpattern = int(iterations*len(array) <= terminaldisplaylimit)
    main_ui = input(f'\n What would you like to do? /run/settings/info/help/\n> ').lower().strip()
    if main_ui:
        cmd, cmd2, *rest = main_ui.split()+['none']
    else:
        cmd, cmd2 = 'run', 'none'
    runid += 1
print('\n ██▓▓▒▒░░ Thank you for using this script! ░░▒▒▓▓██ ')
######### Changelog #########
# date of main update: highest version [major change]
# 29.12.18: 2.3 (.X)
# 21.12.18: 2.2 (.7) [print small]
# 10.12.18: 2.1 (.9) [merging]
# 03.12.18: 2.0 (.6) [shift, linenumbers and py]
# 19.11.18: 1.9 (.9) [image export]
# 07.11.18: 1.8 (.5) [examples]
# 05.11.18: 1.7 (.4) [a lot of debugging]
# 02.11.18: 1.6 (.1) [r110 ether detection tests]
# 02.11.18: 1.5 (.1) [presets, boundary and 2.order]
# ??.10.18: 1.2 - 1.4 [help menu]
# 22.10.18: 1.1 (.?) [added settings]
# 22.10.2018: 1.0 (.0) [first tests]
######### To Do #########
#!# Better code style (docs.python-guide.org/writing/style/ and youtu.be/x-kB2o8sd5c)
#!# Reusable code? (stackoverflow.com/questions/287204/python-program-start)
#!# Bytearray() instead of str()?
######### Features to (re)implement #########
# Delay between iterations
# Probabilistic automata
# Higher order automata
