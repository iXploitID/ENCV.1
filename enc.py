#modul
import marshal, zlib, base64, os, sys

try:
   r = sys.argv[1]
except:
   exit("usage : python2 enc.py file.py")
if not os.path.isfile(r):
     exit("File Tydack di temukan")

a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64/nexec(marshal.oads(zlib.dcompress(base64.b64decode("{}"))))'


open("run.py","w").write(sv.format(d))
exit("berhasil : save to as run.py")
