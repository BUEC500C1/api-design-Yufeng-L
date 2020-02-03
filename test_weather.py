#Copyright 2020 Yufeng Lin yflin@bu.edu
#Test function

import weathersearch
import pytest

def test():
	assert(weathersearch.getLoc("abcd")) == "Airportcode Not Found", "wrong output"
	assert isinstance(weathersearch.getLoc("KBOS"),list)

# if __name__ == "__main__":
# 	test()