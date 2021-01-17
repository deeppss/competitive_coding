import os 
import sys
import glob

def change(old_ext,new_ext):
	[ os.rename( f,"%s.%s" % (os.path.splitext(f)[0],new_ext) ) for f in glob.glob(os.getcwd() + "/*." + old_ext) ]

if __name__ == "__main__":
	if len(sys.argv) > 2:
		change(sys.argv[1],sys.argv[2])
    
    #credits to Braksa Zakaria
