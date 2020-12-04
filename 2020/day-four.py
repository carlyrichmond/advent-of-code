class Passport:

    def __init__(self, attributes):
        self.birth_year = attributes["byr"] if "byr" in attributes else ""
        self.issue_year = attributes["iyr"] if "iyr" in attributes else "" 
        self.expiration_year = attributes["eyr"] if "eyr" in attributes else ""
        self.height = attributes["hgt"] if "hgt" in attributes else ""
        self.hair_colour = attributes["hcl"] if "hcl" in attributes else ""
        self.eye_colour = attributes["ecl"] if "ecl" in attributes else ""
        self.passport_id = attributes["pid"] if "pid" in attributes else ""
        self.country_id = attributes["cid"] if "cid" in attributes else ""

    def is_valid(self):
        return (self.birth_year and self.issue_year and self.expiration_year and 
            self.height and self.hair_colour and self.eye_colour and self.passport_id)

def main():

    current_attributes = {}
    valid_passport_count = 0

    ## issue with checking the last passport
    # adding an extra new line to end of file to ensure it is validated
    open("2020/input/day-four.txt", "a").write("\n")

    for line in open("2020/input/day-four.txt", "r"):
        if (line != "\n"):
            elements = line.split(" ")
            
            for e in elements:
                attribute_pair = e.replace("\n", "").split(":")
                current_attributes[attribute_pair[0]] = attribute_pair[1]
            
        else:
            passport = Passport(current_attributes)
            print("%s: %s" % (passport.passport_id, passport.is_valid()))

            if (passport.is_valid()):
                valid_passport_count += 1

            current_attributes = {}

    print(valid_passport_count)

if __name__ == "__main__":
    main()