def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    credit_hours = 0
    total_cost = 0
    for course, students in c_rosters.items():
        if id in students:
            credit_hours += c_hours[course]
            if s_in_state[id]:
                total_cost += c_hours[course] * 225
            else:
                total_cost += c_hours[course] * 850
    return credit_hours, total_cost

def display_hours_and_bill(hours, cost):
    print(f"Course load: {hours} credit hours")
    print(f"Enrollment cost: ${cost:.2f}")
