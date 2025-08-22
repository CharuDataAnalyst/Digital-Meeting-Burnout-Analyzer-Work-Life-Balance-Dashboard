"""
#Digital Meeting Burnout Dataset Generation
------------------------------------------
#Purpose: Create a realistic, simulated dataset of employee meetings and communications
#to analyze digital fatigue and calculate a Burnout Risk Index (BRI). 
"""

import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker and seed for reproducibility
fake = Faker()
np.random.seed(42)
random.seed(42)

# Departments and meeting types
departments = ['HR','Tech','Sales','Ops','Finance']
meeting_types = ['1:1','Team','Client','All-Hands']

# Generate 10,000+ realistic records
data = []
for i in range(10000):
    emp_id = random.randint(1000, 2000)
    dept = random.choice(departments)
    meeting_datetime = fake.date_time_this_year()
    duration = np.random.randint(15, 120)
    m_type = random.choice(meeting_types)
    participants = np.random.randint(2, 15)
    msg_count = np.random.randint(0, 250)
    after_hours = random.choice(['Yes','No'])
    productivity = np.random.randint(50, 100)
    context_switches = np.random.randint(0, 20)

    # Burnout Risk Index (weighted)
    bri = (0.4 * (1 if after_hours == 'Yes' else 0) +
           0.3 * (duration / 120) +
           0.2 * (context_switches / 20) +
           0.1 * (msg_count / 250))

    data.append([emp_id, dept, meeting_datetime, duration, m_type,
                 participants, msg_count, after_hours, productivity,
                 context_switches, round(bri, 3)])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'EmployeeID','Department','MeetingDateTime','MeetingDuration',
    'MeetingType','NumberOfParticipants','MessageCount',
    'AfterHoursMeetings','ProductivityScore','ContextSwitchCount','BurnoutRiskIndex'
])

# Save CSV
df.to_csv('digital_meeting_burnout_dataset.csv', index=False)

print("Dataset generated successfully! ")
