import sys
import os

def init(name):
    start = "\\documentclass{article}\n\n"
    start += "\\usepackage[utf8]{inputenc}\n"
    start += "\\usepackage[a4paper]{geometry}\n"
    start += "\\usepackage[T1]{fontenc}\n"
    start += "\\usepackage{float}\n"
    start += "\\usepackage{placeins}\n\n"
    start += "\\title{System Programming - " +  name + " homework}\n"
    start += "\\author{Quentin Barbarat}\n\n"
    start += "\\usepackage{natbib}\n"
    start += "\\usepackage{graphicx}\n\n"
    start += "\\begin{document}\n\n"
    start += "\\maketitle\n\n"

    return start

def ins_pic(name):
    inc = "\\begin{figure}[ht!]\n"
    inc += "\t\\includegraphics[width=\linewidth]{" + name + "}\n"
    inc += "\t\\caption{Question " + rem_ext(name) + "}\n"
    inc += "\t\\label{fig:" + rem_ext(name) + "}\n"
    inc += "\\end{figure}\n\n"

    return inc

def rem_ext(fname):
    return fname.split('.')[0]

res_file = open(sys.argv[1] + ".tex", 'w')

res_file.write(init(sys.argv[1]))

screens = os.listdir(sys.argv[1])
screens.sort()

for fname in screens:
    res_file.write(ins_pic(fname))

res_file.write("\\end{document}\n")
