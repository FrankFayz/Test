
# ANTENATAL CLINIC SIMULATION

# 1. Define the simulation times in minutes
clinic_duration = 240       # 1 PM to 5 PM = 4 hours
arrival_interval = 5        # A mother arrives every 5 minutes
measurements_time = 5
laboratory_time = 15
doctor_service_time = 10

# 2. Create an empty list to store simulation results
results = []

# 3. Track when the doctor will be available
doctor_available = 0

# 4. Generate mothers and simulate their movement
mother_number = 0

for arrival_time in range(0, clinic_duration, arrival_interval):

    mother_number += 1

    # Time when the mother is ready for the doctor
    ready_time = arrival_time + measurements_time + laboratory_time

    # Doctor starts when both the mother and doctor are ready
    doctor_start = max(ready_time, doctor_available)

    # Calculate when the examination finishes
    doctor_finish = doctor_start + doctor_service_time

    # Calculate how long the mother waits for the doctor
    waiting_time = doctor_start - ready_time

    # Store the results
    results.append([
        mother_number,
        arrival_time,
        ready_time,
        doctor_start,
        doctor_finish,
        waiting_time
    ])

    # Update the doctor's next available time
    doctor_available = doctor_finish


# 5. Convert minutes after 1 PM into clock time
def convert_time(minutes):
    total_minutes = (13 * 60) + minutes

    hours = total_minutes // 60
    mins = total_minutes % 60

    if hours >= 12:
        period = "PM"
    else:
        period = "AM"

    hours = hours % 12

    if hours == 0:
        hours = 12

    return f"{hours}:{mins:02d} {period}"


# 6. Display the simulation results
print("ANTENATAL CLINIC SIMULATION")
print("-" * 85)

print(f"{'Mother':<10}{'Arrival':<15}{'Ready':<15}"
      f"{'Doctor Start':<18}{'Doctor Finish':<18}{'Waiting'}")

print("-" * 85)

for row in results:
    print(f"{row[0]:<10}"
          f"{convert_time(row[1]):<15}"
          f"{convert_time(row[2]):<15}"
          f"{convert_time(row[3]):<18}"
          f"{convert_time(row[4]):<18}"
          f"{row[5]} minutes")


# 7. Calculate performance measures
total_mothers = len(results)

total_waiting_time = sum(row[5] for row in results)

average_waiting_time = total_waiting_time / total_mothers

maximum_waiting_time = max(row[5] for row in results)

mothers_completed_by_5 = sum(
    1 for row in results if row[4] <= clinic_duration
)

mothers_served_after_5 = total_mothers - mothers_completed_by_5

doctor_busy_during_clinic = 220
doctor_utilisation = (doctor_busy_during_clinic / clinic_duration) * 100


# 8. Display the summary
print("\nSIMULATION SUMMARY")
print("-" * 40)

print("Total mothers accepted:", total_mothers)
print("Average doctor waiting time:", average_waiting_time, "minutes")
print("Maximum doctor waiting time:", maximum_waiting_time, "minutes")
print("Mothers completed by 5 PM:", mothers_completed_by_5)
print("Mothers served after 5 PM:", mothers_served_after_5)
print("Doctor utilisation during clinic hours:",
      round(doctor_utilisation, 2), "%")
print("Final examination completion time:",
      convert_time(results[-1][4]))
