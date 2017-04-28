class ConsecutiveRunParser(object):
	VALID_RUN_DIFFS=[-1,1]
	
	@staticmethod
	def findRuns(numbers, length=3, noResultsFoundText="No Runs Found"):
		"""
		Takes in a list of numbers and searchs for runs of specified length.
		A run is a defined as a series of numbers that all increment or 
		decrement by 1.
		@param numbers, the list of numbers to process
		@param length, the required length of the run
		@param noResultsFoundText, what the output will be if no runs are found
		"""
		def isRun(subset):
			"""
			Helper function to determine if a specified subset is a run or not
			@param subset, a subset of the list of numbers provided to findRuns
			"""
			if len(subset) != length:
				return False
				
			diffs = [subset[i+1] - subset[i] for i in range(length-1)]
			return len(set(diffs)) == 1 and diffs[0] in ConsecutiveRunParser.VALID_RUN_DIFFS
		
		indecies = [index for index in range(len(numbers)) if isRun(numbers[index:index+length])]
		return indecies if len(indecies) else noResultsFoundText
		
def runTest(input, expected):
	indecies = ConsecutiveRunParser.findRuns(input)
	print "Running with: {}".format(input)
	print "Expected: {}".format(str(expected))
	print "Actual:{}\n".format(indecies)
	assert(str(expected) == str(indecies))
			
def runTests():	
	runTest([1,2,3,5,10,9,8,9,10,11,7,8,7], [0,4,6,7])
	runTest([], "No Runs Found")
	runTest([1,2], "No Runs Found")
	runTest([-1,-2,-3], [0])
	runTest([0,0,0], "No Runs Found")
	runTest([0,2,4,6], "No Runs Found")
	runTest([0,1,2,3,4,5,6,7], [0,1,2,3,4,5])
	runTest([7,6,5,4,3,2,1,0], [0,1,2,3,4,5])
			
if __name__ == '__main__':
	import sys
	import re
	
	if len(sys.argv) != 2:
		print "Invalid usage. Expected python find_consecutive_runs.py <list_of_numbers>"
		sys.exit(1)
		
	if type(sys.argv[1]) is str and sys.argv[1].upper() == '--RUN-TESTS':
		runTests()
	else:
		numbers = [int(n) for n in re.findall(r'\b\d+\b', sys.argv[1])]
		print str(ConsecutiveRunParser.findRuns(numbers))
		