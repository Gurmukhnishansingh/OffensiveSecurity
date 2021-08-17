from keystone import *

CODE = (
" jmp esp;"
)
# Initialize engine in 32bit 
ks = Ks(KS_ARCH_X86, KS_MODE_32)
encoding, count = ks.asm(CODE)
egghunter = ""
for dec in encoding: 
    egghunter += "\\x{0:02x}".format(int(dec)).rstrip("\n")
print("egghunter = (\"" + egghunter + "\")")