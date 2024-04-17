import subprocess
import os

# set (absolute) paths of necessary files
acrobatPath = os.path.abspath("C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe")
textbookPath = os.path.abspath("C:\\Users\\josep\\Downloads\\Algebra_2_and_Trigonometry.pdf")

# input preprocessing
x = int(input("enter the page: "))
y = f"page={x + 10}"

# open process
process = subprocess.Popen([acrobatPath, '/A', y, textbookPath], shell=False, stdout=subprocess.PIPE)
process.wait()