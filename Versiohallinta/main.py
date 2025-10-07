def funktio(a, b):
    return a + b


class Luokka:
    def __init__(self, kirjain):
        self.__kirjain = kirjain
    
    def nayta_kirjain(self):
        print(self.__kirjain)


        
if __name__ == "__main__":
    print(funktio(3, 8))