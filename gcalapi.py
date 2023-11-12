calendar = {
    'summary' : 'calendarSummary',
    'timeZone':'America/Los_Angeles'
}

created_calendar = service.calendars().insert(body==calendar).execute()

print created_calendar['id']
