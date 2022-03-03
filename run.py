import optparse

par = optparse.OptionParser(
    usage = 'usage: %prog --bit 32 or --bit 64'
)

par.add_option(
    '--bit',help='Masukan bit hp mu contoh: --bit 64',default=None
)
(arg,opt) = par.parse_args()

if __name__ == "__main__":
	if(arg.bit=="64"):
		try:
			from ap64 import zmbf as co
			co.make()
		except Exception as e:
			exit(e)
	elif(arg.bit=="32"):
		try:
			from ap32 import zmbf as cok
			cok.make()
		except Exception as e:
			exit(e)
	else:
		exit("\n [+] gunakan python run.py --bit 64 jika hp kamu 64 bit \n [+] gunakan python run.py --bit 32 jika hp kamu 32 bit\n")
