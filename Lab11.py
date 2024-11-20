import matplotlib.pyplot as plt
import os
#os.listdir("path")
def display_menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    print("")

def main():
    while True:
        display_menu()
        selection = input("Enter your selection: ")

        if selection == "1":
            Grade = 0
            name = input("What is the student's name: ")
            with open("data/students.txt", "r") as file:
                count = 0
                for line in file:
                    if name == line[3:-1]:
                        id = line[:3]
                    else:
                        count += 1
            file.close()
            if count != 30:
                submissions = os.listdir("data/submissions")
                for line in submissions:
                    with open(f"data/submissions/{line}", "r") as file:
                        ids = ""
                        for lane in file:
                            if id in lane:
                                ids = lane
                                assignment_id = ids[4:9]
                                score = ids[10:]
                                with open("data/assignments.txt", "r") as file:
                                    for line in file:
                                        if assignment_id in line:
                                            weight = file.readline().strip()
                                            Grade += (float(score) * float(weight))/100
                                file.close()
                    file.close()
                Grade /= 10
                Grade = round(Grade, 2)
                print(f"{Grade}%")
            else:
                print("Student not found\n")

        elif selection == "2":
            assignment_name = input("What is the assignment name: ")
            with open("data/assignments.txt", "r") as file:
                count = 0
                for line in file:
                    if assignment_name == line[0:-1]:
                        id = file.readline().strip()
                    else:
                        count += 1
            file.close()
            print(count)
            if count != 57:
                with open("data/submissions/0a5873b6-c6c4-4481-be33-ec7adc44ecd0.txt", "r") as file:
                    for line in file:
                        min = line[10:]
                        max = line[10:]
                file.close()
                submissions = os.listdir("data/submissions")
                avg = 0
                count2 = 1
                for line in submissions:
                    with open(f"data/submissions/{line}", "r") as file:
                        for line in file:
                            if line[4:9] == id:
                                count2 += 1
                                if line[10:] < min:
                                    min = line[10:]
                                if line[10:] > min:
                                    max = line[10:]
                                avg += int(line[10:])
                    file.close()
                avg /= count2
                print(f"min: {min}")
                print(f"max: {max}")
                print(f"avg: {avg:.2f}")
            else:
                print("Assignment not found")

        elif selection == "3":
            assignment_name = input("What is the assignment name: ")
            with open("data/assignments.txt", "r") as file:
                count = 0
                for line in file:
                    if assignment_name == line[0:-1]:
                        id = file.readline().strip()
                    else:
                        count += 1
            file.close()
            if count != 57:
                scores = []
                submissions = os.listdir("data/submissions")
                for line in submissions:
                    with open(f"data/submissions/{line}", "r") as file:
                        for line in file:
                            if line[4:9] == id:
                                scores.append(int(line[10:]))
                    file.close()

                plt.hist(scores, bins=[0,25,50,75,100])
                plt.show()

            else:
                print("Assignment not found")






if __name__ == "__main__":
    main()