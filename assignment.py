# print("lets start programming")
print(">>>>>Covid-19 Data<<<<<")

states = {
    "Maharashtra": {"Confirmed": 4343727, "Active": 674770, "Recovered": 3601796},
    "Kerala": {"Confirmed": 1427546, "Active": 232808, "Recovered": 1189267},
    "UP": {"Confirmed": 1120176, "Active": 304199, "Recovered": 804563},
    "Delhi": {"Confirmed": 1097672, "Active": 92358, "Recovered": 940930},
    "Punjab": {"Confirmed": 345366, "Active": 49894, "Recovered": 286942},
}
# print(states["Delhi")
# print(states)

input_state = input("Enter the name of state:")
if input_state == "Maharashtra" or "Kerala" or "UP" or "Delhi" or "Punjab":
    print("All, Confirmed, Active or Recovered ")
    input_case = input("Which cases do you want to see???")
    if input_case == "All":
        print("covid-19 cases in", input_state, " are", states[input_state])
    elif input_case == "All" or "Confirmed" or "Active" or "Recovered":
        enter_state = states[input_state][input_case]
        print()
        print("covid-19", input_case, "cases in", input_state, " are", enter_state)
    else:
        print("You've entered wrong input!!!")
else:
    print("You've entered wrong input!!!")
