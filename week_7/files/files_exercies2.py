# question 4

def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
        ]       
        
    with open(filename, "w", encoding="utf-8") as file: 
        for name, grades in students:
            grades_str_list = []
            for grade in grades:
                grades_str_list.append(str(grade))
    
            line = name + "," + ",".join(grades_str_list)
    
            file.write(line + "\n")


def calculate_averages(filename):
    averages = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            
            parts = line.split(",")
            name = parts[0].strip()
            
            try:
                grade_parts = parts[1:]

                if len(grade_parts) == 0 or (len(grade_parts) == 1 and grade_parts[0].strip() == ""):
                    raise ValueError("Missing grades")

                grades = []
                for g in grade_parts:
                    cleaned = g.strip()
                    if cleaned != "":  
                        grades.append(int(cleaned))

                if len(grades) == 0:
                    raise ValueError("No valid numerical grades found")

                averages[name] = sum(grades) // len(grades)

            except ValueError:
                print(f"Warning: Corrupted data on line {line_num}. Skipping.")
                continue
                
    return averages



# question 5


def save_results(averages, output_filename):

    sorted_averages = sorted(averages.items(), key=lambda item: item[1], reverse=True)
    
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write("=== Student Results ===\n")
        for i, (name, avg) in enumerate(sorted_averages, 1):
            file.write(f"{i}. {name}: {avg:.1f}\n")
    
    total_sum = sum(avg for name, avg in sorted_averages)
    class_average = total_sum / len(sorted_averages)
    
    name_max, max_g = sorted_averages[0]
    name_min, min_g = sorted_averages[-1]
    
    passed = sum(1 for name, avg in sorted_averages if avg >= 60)

    with open(output_filename, "a", encoding="utf-8") as file:
        file.write("=== Statistics ===\n")
        file.write(f"Class average: {class_average:.1f}\n")
        file.write(f"Highest: {name_max} ({max_g:.1f})\n")
        file.write(f"Lowest: {name_min} ({min_g:.1f})\n")
        file.write(f"Passing (>=60): {passed}/{len(sorted_averages)}\n")




create_grades_file('grades.txt')
averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')

with open('results.txt', 'r', encoding="utf-8") as file:
    print(file.read())