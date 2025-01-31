import json
from datetime import datetime, timedelta

def generate_employee_time(overtime_minutes, userinput):
    userinput += " AM"

    duty_start = datetime.strptime(userinput, "%I:%M %p")

    # Calculate total duty time in minutes
    duty_duration = 465

    # Add overtime to duty duration
    total_minutes = duty_duration + overtime_minutes

    # Generate random in-time between 10:00 AM and 11:00 AM
    in_time = duty_start

    # Calculate out-time by adding total_minutes to in-time
    out_time = in_time + timedelta(minutes=total_minutes)

    return in_time.strftime("%I:%M %p"), out_time.strftime("%I:%M %p")

def handler(event, context):
    # Get data from the event (query parameters or request body)
    try:
        overtime_minutes = int(event['queryStringParameters']['overtime'])
        userinput = event['queryStringParameters']['in_time']

        if overtime_minutes < 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Overtime cannot be negative"})
            }

        in_time, out_time = generate_employee_time(overtime_minutes, userinput)

        return {
            "statusCode": 200,
            "body": json.dumps({"in_time": in_time, "out_time": out_time})
        }
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid input"})
        }
