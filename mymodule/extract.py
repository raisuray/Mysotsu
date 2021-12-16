import re
import neologdn


def exct_experimental_section(doc):

    start   = 0
    end     = 0
    read    = 0
    pattern_start = re.compile("【実施例.*】|（実施例.*）")
    pattern_end  = re.compile("【発明.*】|（発明.*）|【図面の簡単な.*】")

    exp_texts = []

    for i, experiment in enumerate(doc):
        if(read == 0 and pattern_start.match(experiment) != None):   
            read = 1
            start = i
        if(read == 1 and pattern_end.match(experiment) != None):
            end = i
            break

    exp_texts = doc[start:end]

    for i in range(len(exp_texts)):
        exp_texts[i] = re.sub(r"【.*】|（.*） ?|〔[１２３４５６７８９０]?〕|<.*>|〈.*〉", "", exp_texts[i])
        exp_texts[i] = re.sub("\n| ?", "",exp_texts[i])
        exp_texts[i] = neologdn.normalize(exp_texts[i])

    while "" in exp_texts:
        exp_texts.remove("")

    return exp_texts


def exct_invention_section(doc):

    start   = 0
    end     = 0
    read    = 0
    pattern_start = re.compile("【発明の効果】|（発明の効果）")
    pattern_end  = re.compile("（図面の簡単な.*）|【図面の簡単な.*】")

    exp_texts = []

    for i, experiment in enumerate(doc):
        if(read == 0 and pattern_start.match(experiment) != None):   
            read = 1
            start = i
        if(read == 1 and pattern_end.match(experiment) != None):
            end = i
            break

    exp_texts = doc[start:end]

    for i in range(len(exp_texts)):
        exp_texts[i] = re.sub(r"【.*】|（.*） ?|〔[１２３４５６７８９０]?〕|<.*>|〈.*〉", "", exp_texts[i])
        exp_texts[i] = re.sub("\n| ?", "",exp_texts[i])
        exp_texts[i] = neologdn.normalize(exp_texts[i])

    while "" in exp_texts:
        exp_texts.remove("")

    return exp_texts