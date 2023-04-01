import operator
ops = {"+": operator.add, "-": operator.sub}

def arithmetic_arranger(inputs,display_answer=False):
  
    #initialise
    first_numbers = []
    second_numbers = []
    outputs = []
    operators = []
    count = 0
    largest_value = []
    line = []

    #split inputs and assign to their own lists
    for input in inputs:

        first_numbers.append(input.split()[0])
        second_numbers.append(input.split()[2])
        operators.append(input.split()[1])

        # Handle errors for input:
        if operators[count] != "+" and operators[count] != "-":
            return "Error: Operator must be '+' or '-'."
        if not first_numbers[count].isdigit() or not second_numbers[count].isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_numbers[count]) > 4 or len(second_numbers[count]) > 4:
            return "Error: Numbers cannot be more than four digits"
        if len(inputs) > 5:
            return "Error: Too many problems."
        
        #dins largest value at given index
        largest_value.append((max(int(first_numbers[count]), int(second_numbers[count]))))

        if operators[count] == "+":
            outputs.append(str(int(first_numbers[count]) + int(second_numbers[count])))
        else:
            outputs.append(str(int(first_numbers[count]) - int(second_numbers[count])))

        for output in outputs:
            if int(output) >= 0:
                output = " " + output
                
        count += 1

    for value in largest_value:
        line.append("-" * (int(len(str((value)))+2)))

    #base print function
    def base_print(largest, nums1, nums2, operator):
        if len(largest)==1:
            x = (nums1[0].rjust(int(len(str(largest[0])))+2))
            y = ((operator[0] + " " + nums2[0]).rjust(int(len(str(largest[0])))+2))
            z = (line[0].rjust(int(len(str(largest[0])))+2))
        elif len(largest)==2:
            x = (nums1[0].rjust(int(len(str(largest[0])))+2) + nums1[1].rjust(int(len(str(largest[1])))+6))
            y = (operator[0].ljust(2) + nums2[0].rjust(int(len(str(largest[0])))) + "    " + ((operator[1].ljust(2) + nums2[1].rjust(int(len(str(largest[1])))))))
            z = (line[0].rjust(int(len(str(largest[0])))+2) + line[1].rjust(int(len(str(largest[1])))+6))
        elif len(largest)==3:
            x = (nums1[0].rjust(int(len(str(largest[0])))+2) + nums1[1].rjust(int(len(str(largest[1])))+6) + nums1[2].rjust(int(len(str(largest[2])))+6))
            y = (operator[0].ljust(2) + nums2[0].rjust(int(len(str(largest[0])))) + "    " + ((operator[1].ljust(2) + nums2[1].rjust(int(len(str(largest[1])))))) + "    " + ((operator[2].ljust(2) + nums2[2].rjust(int(len(str(largest[2])))))))
            z = (line[0].rjust(int(len(str(largest[0])))+2) + line[1].rjust(int(len(str(largest[1])))+6) + line[2].rjust(int(len(str(largest[2])))+6))
        elif len(largest)==4:
            x = (nums1[0].rjust(int(len(str(largest[0])))+2) + nums1[1].rjust(int(len(str(largest[1])))+6) + nums1[2].rjust(int(len(str(largest[2])))+6) + nums1[3].rjust(int(len(str(largest[3])))+6))
            y = (operator[0].ljust(2) + nums2[0].rjust(int(len(str(largest[0])))) + "    " + ((operator[1].ljust(2) + nums2[1].rjust(int(len(str(largest[1])))))) + "    " + ((operator[2].ljust(2) + nums2[2].rjust(int(len(str(largest[2])))))) + "    " + ((operator[3].ljust(2) + nums2[3].rjust(int(len(str(largest[3])))))))
            z = (line[0].rjust(int(len(str(largest[0])))+2) + line[1].rjust(int(len(str(largest[1])))+6) + line[2].rjust(int(len(str(largest[2])))+6) + line[3].rjust(int(len(str(largest[3])))+6))
        elif len(largest)==5:
            x = (nums1[0].rjust(int(len(str(largest[0])))+2) + nums1[1].rjust(int(len(str(largest[1])))+6) + nums1[2].rjust(int(len(str(largest[2])))+6) + nums1[3].rjust(int(len(str(largest[3])))+6) + nums1[4].rjust(int(len(str(largest[4])))+6))
            y = (operator[0].ljust(2) + nums2[0].rjust(int(len(str(largest[0])))) + "    " + ((operator[1].ljust(2) + nums2[1].rjust(int(len(str(largest[1])))))) + "    " + ((operator[2].ljust(2) + nums2[2].rjust(int(len(str(largest[2])))))) + "    " + ((operator[3].ljust(2) + nums2[3].rjust(int(len(str(largest[3])))))) + "    " + ((operator[4].ljust(2) + nums2[4].rjust(int(len(str(largest[4])))))))
            z = (line[0].rjust(int(len(str(largest[0])))+2) + line[1].rjust(int(len(str(largest[1])))+6) + line[2].rjust(int(len(str(largest[2])))+6) + line[3].rjust(int(len(str(largest[3])))+6) + line[4].rjust(int(len(str(largest[4])))+6))
        return f"{x}\n{y}\n{z}"

    #results print function
    def result_print(largest, results):
        if len(largest)==1:
            x = (results[0].rjust(int(len(str(largest[0])))+2))
        elif len(largest)==2:
            x = (results[0].rjust(int(len(str(largest[0])))+2) + results[1].rjust(int(len(str(largest[1])))+6))
        elif len(largest)==3:
            x = (results[0].rjust(int(len(str(largest[0])))+2) + results[1].rjust(int(len(str(largest[1])))+6) + results[2].rjust(int(len(str(largest[2])))+6))
        elif len(largest)==4:
            x = (results[0].rjust(int(len(str(largest[0])))+2) + results[1].rjust(int(len(str(largest[1])))+6) + results[2].rjust(int(len(str(largest[2])))+6) + results[3].rjust(int(len(str(largest[3])))+6))
        elif len(largest)==5:
            x = (results[0].rjust(int(len(str(largest[0])))+2) + results[1].rjust(int(len(str(largest[1])))+6) + results[2].rjust(int(len(str(largest[2])))+6) + results[3].rjust(int(len(str(largest[3])))+6) + results[4].rjust(int(len(str(largest[4])))+6))
        return x

    #call functions
    arranged_problems = base_print(largest_value, first_numbers, second_numbers, operators)
    if display_answer == True:
        arranged_problems += "\n" + result_print(largest_value, outputs)
    

    print(arranged_problems)
    return arranged_problems
    

#arithmetic_arranger(['3801 - 2', '123 + 49'])
#arithmetic_arranger(['1 + 2', '1 - 9380'])
#arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])
#arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
#arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
#arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
#arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])
#arithmetic_arranger(['3 + 855', '988 + 40'], True)
#arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)