class CreditCard():

    def __init__(self,card_number):
        self.__card_number = card_number
        self.__credit = 0
        
    def assign_credit(self,credit):
        if credit < 100:
            raise ValueError("Credit below limit")
        else:
            self.__credit = credit

    def get_credit(self):
        return self.__credit

    def get_card_number(self):
        return self.__card_number