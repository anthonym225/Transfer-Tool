import pandas as pd
ColList = pd.DataFrame({"College": ["Princeton University", "Harvard University", "Columbia University", "Massachusetts Institute of Technology", "University of Chicago", "Yale University", "Stanford University", "Duke University", "University of Pennsylvania", "Johns Hopkins University", "Northwestern University", "California Institute of Technology", "Dartmouth College", "Brown University", "Vanderbilt University", "Cornell University", "Rice University", "University of Notre Dame", "University of California - Los Angeles", "Washington University in St. Louis", "Emory University", "Georgetown University", "University of California - Berkeley", "University of Southern California", "Carnegie Mellon University", "University of Virginia", "Tufts University", "University of Michigan - Ann Arbor", "Wake Forest University", "New York University", "University of California - Santa Barbara", "University of North Carolina - Chapel Hill", "University of California - Irvine", "University of Rochester", "Brandeis University", "Georgia Institute of Technology", "University of Florida", "Boston College", "College of William and Mary", "University of California - Davis", "University of California - San Diego", "Boston University", "Case Western Reserve University", "Northeastern University", "Tulane University", "Pepperdine University", "University of Georgia", "University of Illinois - Urbana-Champaign", "Rensselaer Polytechnic Institute", "University of Texas - Austin", "University of Wisconsin - Madison", "Villanova University"],
               "Transfer Rate": [0.91, 1.00, 6.70, 4.10, 5.40, 2.50, 1.40, 6.70, 8.10, 10.20, 15.10, 1.90, 0.50, 5.10, 29.70, 17.90, 9.70, 26.60, 25.90, 20.20, 25.60, 15.90, 23.20, 24.30, 6.90, 39.70, 9.60, 37.90, 24.70, 25.80, 55.70, 34.50, 52.70, 29.20, 31.40, 37.80, 41.10, 16.60, 44.90, 61.50, 54.30, 52.00, 23.40, 26.10, 26.50, 29.80, 72.80, 45.80, 49.40, 36.80, 51.70, 31.70],
               "Transfers Applied": [1429, 1553, 2536, 581, 881, 1240, 2234, 1197, 2715, 1105, 1872, 155, 829, 1862, 1359, 4762, 555, 884, 22050, 1131, 1000, 2175, 18609, 8833, 825, 2591, 1131, 4141, 373, 7820, 16619, 3526, 19557, 1053, 599, 1909, 7194, 1384, 858, 16763, 17823, 3931, 487, 3519, 1149, 717, 2537, 4940, 451, 8189, 3858, 877],
               "Transfers Accepted": [13, 16, 170, 24, 48, 31, 31, 80, 221, 113, 282, 3, 4, 95, 404, 852, 54, 235, 5720, 228, 256, 346, 4316, 2143, 57, 1028, 109, 1571, 92, 2014, 9261, 1218, 10309, 308, 188, 721, 2954, 230, 385, 10317, 9682, 2044, 114, 920, 305, 214, 1848, 2263, 223, 3012, 1996, 278],
               "State": ["New Jersey", "Massachusetts", "New York", "Massachusetts", "Illinois", "Connecticut", "California", "North Carolina", "Pennsylvania", "Maryland", "Illinois", "California", "New Hampshire", "Rhode Island", "Tennessee", "New York", "Texas", "Indiana", "California", "Missouri", "Georgia", "District of Columbia", "California", "California", "Pennsylvania", "Virginia", "Massachusetts", "Michigan", "North Carolina", "New York", "California", "North Carolina", "California", "New York", "Massachusetts", "Georgia", "Florida", "Massachusetts", "Virginia", "California", "California", "Massachusetts", "Ohio", "Massachusetts", "Louisiana", "California", "Georgia", "Illinois", "New York", "Texas", "Wisconsin", "Pennsylvania"],
               "Cost (OOS + R&B)": [66150, 69600, 74199, 67430, 75735, 71290, 69109, 71764, 71715, 69863, 72980, 68901, 71827, 71050, 67392, 70321, 63158, 69395, 61915, 71975, 66950, 71580, 65003, 72209, 70094, 62633, 70600, 62176, 69130, 71790, 64125, 51152, 61872, 70108, 70943, 49366, 43409, 70588, 59012, 63743, 60177, 70302, 65384, 71067, 73296, 73002, 44394, 46202, 73813, 51786, 49885, 68231],
               "Type": ["Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Private", "Public", "Private", "Private", "Private", "Public", "Private", "Private", "Public", "Private", "Public", "Private", "Private", "Public", "Public", "Public", "Private", "Private", "Public", "Public", "Private", "Public", "Public", "Public", "Private", "Private", "Private", "Private", "Private", "Public", "Public", "Private", "Public", "Public", "Private"],
               "Average Financial Aid": [44128, 48195, 46127, 41674, 39032, 48126, 47782, 47055, 43856, 38083, 38593, 36632, 45867, 40116, 40382, 35445, 36192, 38080, 19693, 38927, 38254, 40346, 18541, 34145, 30614, 19017, 37747, 16865, 40596, 32505, 20774, 17758, 18506, 31194, 33806, 11835, 6379, 38399, 17928, 18523, 17303, 34255, 28253, 38906, 45405, 40356, 14351, 12921, 42575, 11021, 6461, 29321]})

# c = ColList.style.format({'Transfer Rate': '{:.2%}'.format}) Delete later
pd.options.display.float_format = '{:,.2f}%'.format
gpaT = input("Enter your cumulative college GPA: ")
gpa = float(gpaT)
state = input("Enter the state you are a resident of: ")
type = input("Enter if you would like Public, Private, or both: ")

if gpa > 3.95:
    if type == "both":
        print("At this point, if you have over a year of college coursework, you have as best a chance as any at getting into any of these universities. Please understand that the extremely selective universities on this list will be a reach for anyone.\n {}".format(ColList[(ColList['Transfer Rate'] >= 0.00)]))
    else:
        print("At this point, if you have over a year of college coursework, you have as best a chance as any at getting into any of these universities. Please understand that the extremely selective universities on this list will be a reach for anyone.\n {}".format(ColList[(ColList['Transfer Rate'] >= 0.00) & (ColList['Type'] == type)]))
    print("Strongly consider these in-state universities!\n {}".format(ColList[(ColList['State'] == state)]))
elif gpa > 3.80 and gpa < 3.95:
    if type == "both":
        print(ColList[(ColList['Transfer Rate'] >= 5.00)])
    else:
        print(ColList[(ColList['Transfer Rate'] >= 5.00) & (ColList['Type'] == type)])
    print("Strongly consider these in-state universities!\n {}".format(ColList[(ColList['State'] == state) & (ColList['Transfer Rate'] >= 5.00)]))
elif gpa > 3.50 and gpa < 3.80:
    if type == "both":
        print(ColList[(ColList['Transfer Rate'] >= 30.00)])
    else:
        print(ColList[(ColList['Transfer Rate'] >= 30.00) & (ColList['Type'] == type)])
    print("Strongly consider these in-state universities!\n {}".format(ColList[(ColList['State'] == state) & (ColList['Transfer Rate'] >= 30.00)]))

# print(ColList[(ColList['Transfer Rate'] <= 2.00) & (ColList['Cost (OOS + R&B)'] < 70000)])
# How To Print Specific Columns --> print(ColList[(ColList['Transfer Rate'] <= '2.0') & (ColList['College'] != 'Princeton University')])
