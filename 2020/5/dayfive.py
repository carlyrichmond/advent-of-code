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
        self.seats = []
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

        seat = Seat(min_row, min_column)
        self.seats = self.seats + [seat]
        return seat

    def get_seat_range(self, min, max, is_upper = True):
        base = (min + max)/2

        if (is_upper):
            return math.floor(base)
        
        return math.ceil(base)

    def get_my_seat(self):
        self.seats.sort()
        previous_seat = self.seats[0]

        for i in range(1, len(self.seats)):
            difference = int(self.seats[i].seat_id) - int(previous_seat.seat_id)
            if (difference > 1):
               return previous_seat.seat_id + 1
            previous_seat = self.seats[i]

if __name__ == "__main__":
    calc = BinaryBoardingCalculator()
    max_seat = calc.get_max_seat()

    print(max_seat)

    my_seat = calc.get_my_seat()
    print(my_seat)
