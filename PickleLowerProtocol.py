import pandas as pd
import pickle
def PickleLowerProtocol(filepath, protocol=2):
	'''
	Use this function to load in a given pickle file and rewrite it with any other protocol.
	This is particularly useful when one is working across python 2 and 3.
	'''
	x = pd.read_pickle(filepath)
	with open(filepath, 'wb') as pfile:
		pickle.dump(x, pfile, protocol=protocol)
