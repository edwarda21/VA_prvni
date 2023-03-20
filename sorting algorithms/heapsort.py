from math import floor

class Heap:
    def __init__(self, array):
        self.array = self.heapify(array)

    @staticmethod
    def heapify(array, max=True):
        output = []
        for i in array:
            inserting = True
            output.append(i)
            counter = len(output)-1
            while inserting:
                if output[floor(counter/2)] < output[counter]:
                    output[floor(counter/2)], output[counter] = output[counter], output[floor(counter/2)]
                    counter = floor(counter/2)
                else:
                    inserting = False
        return output


    def sort(self):
        output = []
        while len(self.array) > 0:
            output.insert(0,self.array.pop(0))
            self.heapify(self.array)
        self.array = output

