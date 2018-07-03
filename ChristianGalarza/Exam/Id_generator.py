CE = "CE_0"
PE = "PE_0"


def generate_id(identifier, number: int):
    if identifier is CE or identifier is PE:
        return identifier + str(number)
