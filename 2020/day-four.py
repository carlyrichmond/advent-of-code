import re

class Passport:

    def __init__(self, attributes):
        self.birth_year = int(attributes["byr"]) if "byr" in attributes else None
        self.issue_year = int(attributes["iyr"]) if "iyr" in attributes else None 
        self.expiration_year = int(attributes["eyr"]) if "eyr" in attributes else ""
        self.height = attributes["hgt"] if "hgt" in attributes else ""
        self.hair_colour = attributes["hcl"] if "hcl" in attributes else ""
        self.eye_colour = attributes["ecl"] if "ecl" in attributes else ""
        self.passport_id = attributes["pid"] if "pid" in attributes else ""
        self.country_id = attributes["cid"] if "cid" in attributes else ""

    def is_valid(self):
        return (self.is_birth_year_valid() and self.is_issue_year_valid() 
            and self.is_expiration_year_valid() and self.is_height_valid() 
            and self.is_hair_colour_valid() and self.is_eye_colour_valid() 
            and self.is_passport_id_valid())

    # Helper function for diagnosing validation issues
    def validity_output(self):
        print(self.passport_id)
        print("byr: %s", self.is_birth_year_valid())
        print("iyr: %s", self.is_issue_year_valid())
        print("eyr: %s", self.is_expiration_year_valid())
        print("hgt: %s", self.is_height_valid())
        print("hcl: %s", self.is_hair_colour_valid())
        print("ecl: %s", self.is_eye_colour_valid())
        print("pid: %s", self.is_passport_id_valid())
        
        return

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def is_birth_year_valid(self):
        return self.birth_year in range(1920, 2003)
    
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    def is_issue_year_valid(self):
        return self.issue_year in range(2010, 2021)
        
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    def is_expiration_year_valid(self):
        return self.expiration_year in range(2020, 2031)

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    def is_height_valid(self):
        height_expression = re.compile("^[0-9]{3}cm$|^[0-9]{2}in$")

        if (not height_expression.match(self.height)):
            return False

        height_number = int(self.height[0:-2])

        if ("cm" in self.height):
            return height_number in range(150, 194)
        
        else: 
            return height_number in range(59, 77)
        
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    def is_hair_colour_valid(self):
        hair_colour_expression = re.compile("^#(?:[a-f0-9]{6})$")
        return hair_colour_expression.match(self.hair_colour)

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    def is_eye_colour_valid(self):
        return self.eye_colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    def is_passport_id_valid(self):
        passport_id_expression = re.compile("^\d{9}$")
        return passport_id_expression.match(self.passport_id)

def main():

    current_attributes = {}
    valid_passport_count = 0

    filename = "2020/input/day-four.txt"

    # issue with checking the last passport
    # adding an extra new line to end of file to ensure it is validated
    # although this does introduce problems on reruns
    open(filename, "a").write("\n")

    for line in open(filename, "r"):
        if (line != "\n"):
            elements = line.split(" ")
            
            for e in elements:
                attribute_pair = e.replace("\n", "").split(":")
                current_attributes[attribute_pair[0]] = attribute_pair[1]
            
        else:
            passport = Passport(current_attributes)

            if (passport.is_valid()):
                valid_passport_count += 1

            current_attributes = {}

    print(valid_passport_count)

if __name__ == "__main__":
    main()