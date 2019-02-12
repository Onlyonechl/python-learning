
import sys

def get_minutes_number():
	"returns a positive number"
	min = int(sys.argv[1])
	if min >= 0 :
		return min
	else:
		raise ValueError

def Hours():
	try:
		h,m = divmod(get_minutes_number(),60)
		print("{} H, {} M".format(h,m))
	except ValueError:
		print("Please input a positive number")

if __name__ == '__main__':
	Hours()
