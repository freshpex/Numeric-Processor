import json
import urllib.request


class NumericProcessor:
    def __init__(self, computations_list):
        self.computations_list = computations_list
        # You can add more initialization code here if you'd like.

    def run_computations(self):
        for computation in self.computations_list:
            self.ans = self.run_one_computation(computation)
            # this calls the method "run_one_computation" to run one calculation each
            

        # You will write code here, to go through the self.computations_list.
    


    # this calculate the values as a list 
        # because the dictionary has a key 
        # that is a list that has a dictionary 
        # that contains the "values " to be calculated has a list
        # then return the corresponding function
    def add(self, values):
        
        add = float(values[0]) + float(values[1])        
        return add
    
    def multiply(self, values):
        multiply =float(values[0]) * float(values[1])
        return multiply
        
    def subtract(self, values):
        substract = float(values[0]) - float(values[1])
        return substract
        
    def divide(self, values):
        divide = float(values[0]) / float(values[1])
        return divide
        
    def display(self, values):
        print(values[0])
        display = float(values[0])
        return display

    def api_compute(self, values):
        first_value = values[0]
        url = get_mathjs_api_url(first_value)
        response = urllib.request.urlopen(url)
        result = response.read().decode('utf-8')
        return float(result)

        #  this adds the last answer into a list,
        #  so it can be called back for the next calculatons 
    def values_list(self, values):
        ans_list = []
        for ans in values:
            if ans == 'ANS':
                ans_list.append(self.ans)

            else:
                ans_list.append(ans)
        
        return ans_list


        # this chooses the computation that is called 
        # and passes the corresponding method

    def run_one_computation(self, computation):
        values = self.values_list(computation['values'])
        if computation['operation'] == 'add':
            return self.add(values)

        if computation['operation'] == 'multiply':
            return self.multiply(values)

        if computation['operation'] == 'subtract':
            return self.subtract(values)

        if computation['operation'] == 'divide':
            return self.divide(values)

        if computation['operation'] == 'display':
            return self.display(values)

        if computation['operation'] == 'api-compute':
            return self.api_compute(values)
               


def load_computations_list_from_file(filename):
    with open(filename, 'r') as f:
        contents = json.load(f)
        return contents['computations']



def get_mathjs_api_url(expression):
    # Expression is a string such as '1 + 1'.
    # Some characters need to be transformed when they are sent to the api.
    # urllib.parse.quote does this.
    # For example, it turns '+' into the code '%2B' so that the api can receieve it.
    expression = urllib.parse.quote(expression)
    url = 'http://api.mathjs.org/v4/?expr=' + expression
    return url


# this class inherits from "NmumericProcesxor"
# it shows the amount of time each computation is called 
# and also stores the computatiuon ran in a dictionary
#  so it can be called in the show statitics methode 
class OperationCounterNumericProcessor(NumericProcessor):
    def __init__(self, filename):
        super().__init__(filename)
        self.count_operations = {}
    
    def run_one_computation(self, computation):
        counter = computation['operation']
        if counter in self.count_operations:
            self.count_operations[counter] += 1
        else:
            self.count_operations[counter] = 1
        
        return super().run_one_computation(computation)
    
    def show_statistics(self):
        for operation in self.count_operations:
            count = self.count_operations[operation]
            print(f'operation: {operation}, count: {count}')




if __name__ == '__main__':
    computations = load_computations_list_from_file('example.json')
    processor = NumericProcessor(computations)
    processor.run_computations()

    print("________")

    count = OperationCounterNumericProcessor(computations)
    count.run_computations()
    count.show_statistics()


