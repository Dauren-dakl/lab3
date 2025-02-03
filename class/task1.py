#1
class StringProcessor:
    def init(self):
        self.text = "" 

    def getString(self):
        self.text = input()  

    def printString(self):
        print(self.text.upper())  


if __name__ == "__main__":
    processor = StringProcessor() 
    processor.getString()  
    processor.printString() 
    