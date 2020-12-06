from functools import total_ordering
import math

@total_ordering
class Seat:
    
    def __init__(self, row = 0, column = 0):
        self.row = row
        self.column = column
        self.seat_id = self.calculate_seat_id()
    
    def calculate_seat_id(self):
        return self.row * 8 + self.column
        
    def __eq__(self, other):
        return (self.seat_id == other.seat_id)

    def __ne__(self, other):
        return (self.seat_id != other.seat_id)

    def __lt__(self, other):
        return (self.seat_id < other.seat_id)

    def __repr__(self):
        return "%d: (%d,%d)" % (self.seat_id, self.row, self.column)


class BinaryBoardingCalculator:

    def __init__(self):
        self.input_path = "day-five-input.txt"

    def get_max_seat(self):
        max_seat = Seat()

        for line in open(self.input_path, "r"):
            current_seat = self.calculate_seat(line)

            if (current_seat > max_seat):
                max_seat = current_seat
        
        return max_seat

    def calculate_seat(self, binary_location):
        max_row = 127
        min_row = 0

        max_column = 7
        min_column = 0

        for b in binary_location:
            if (b == "F"): 
                max_row = self.get_seat_range(min_row, max_row)
            
            elif (b == "B"):
                min_row = self.get_seat_range(min_row, max_row, False)

            if (b == "L"): 
                max_column = self.get_seat_range(min_column, max_column)
            
            elif (b == "R"):
                min_column = self.get_seat_range(min_column, max_column, False)

        return Seat(min_row, min_column)

    def get_seat_range(self, min, max, is_upper = True):
        base = (min + max)/2

        if (is_upper):
            return math.floor(base)
        
        return math.ceil(base)

if __name__ == "__main__":
    calc = BinaryBoardingCalculator()
    max_seat = calc.get_max_seat()

    print(max_seat)