import unittest
from dayfive import BinaryBoardingCalculator, Seat

class DayFiveTests(unittest.TestCase):

    def setUp(self):
        self.calculator = BinaryBoardingCalculator()

     # BFFFBBFRRR: row 44, column 5, seat ID 357.
    def test_walkthrough(self):
        location = "FBFBBFFRLR"
        result = self.calculator.calculate_seat(location)
        expected_seat = Seat(44, 5) 

        # Change to result once verified
        self.assertEqual(result.row, expected_seat.row)
        self.assertEqual(result.column, expected_seat.column)
        self.assertEqual(result.seat_id, 357)

    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    def test_first_example(self):
        location = "BFFFBBFRRR"
        result = self.calculator.calculate_seat(location)
        expected_seat = Seat(70, 7) 

        self.assertEqual(result.row, expected_seat.row)
        self.assertEqual(result.column, expected_seat.column)
        self.assertEqual(result.seat_id, 567)


    # FFFBBBFRRR: row 14, column 7, seat ID 119.
    def test_second_example(self):
        location = "FFFBBBFRRR"
        result = self.calculator.calculate_seat(location)
        expected_seat = Seat(14, 7) 

        self.assertEqual(result.row, expected_seat.row)
        self.assertEqual(result.column, expected_seat.column)
        self.assertEqual(result.seat_id, 119)

    # BBFFBBFRLL: row 102, column 4, seat ID 820.
    def test_third_example(self):
        location = "BBFFBBFRLL"
        result = self.calculator.calculate_seat(location)
        expected_seat = Seat(102, 4) 

        self.assertEqual(result.row, expected_seat.row)
        self.assertEqual(result.column, expected_seat.column)
        self.assertEqual(result.seat_id, 820)

if __name__ == "__main__":
    unittest.main()