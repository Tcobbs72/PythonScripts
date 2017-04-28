class ConsecutiveRunParser(object):
	VALID_RUN_DIFFS=[-1,1]
	
	@staticmethod
	def findRuns(numbers, length=3, noResultsFoundText="No Runs Found"):
		def isRun(subset):
			if len(subset) != length:
				return False
				
			diffs = [subset[i+1] - subset[i] for i in range(length-1)]
			return len(set(diffs)) == 1 and diffs[0] in ConsecutiveRunParser.VALID_RUN_DIFFS
			
		indecies = [index for index in range(len(numbers)) if isRun(numbers[index:index+length])]
		return indecies if len(indecies) != 0 else noResultsFoundText
		
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
	runTest([0,2,0,2], "No Runs Found")
	runTest([0,1,2,3,4,5,6,7], [0,1,2,3,4,5])
	runTest([7,6,5,4,3,2,1,0], [0,1,2,3,4,5])
			
if __name__ == '__main__':
	runTests()