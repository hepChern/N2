# Please write the main file for this algorithm
# A demo is:
from Chern import ChernExec
inputfile = inputs["input"]+"/tree1.root"
outputfile = outputs["output"]+"/tree.root"
ps = ChernExec("root -l -q {}/selection.C".format(path), path)
ps.send(inputfile)
ps.send(outputfile)
ps.exit()