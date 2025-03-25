import requests
import csv

# API endpoint for RemoteOK job listings
url = "https://remoteok.io/api"

# Set headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Make the request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    jobs = response.json()

    # The first item in the JSON response is metadata, so we skip it
    if len(jobs) > 1:
        jobs = jobs[1:]
    else:
        print("No job listings found.")
        exit()

    # Define CSV file name
    csv_filename = "remoteok_jobs.csv"

    # Open the CSV file for writing
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Job Title", "Company", "Location", "Apply Link"])

        # Loop through the first 10 jobs and write details to CSV
        for job in jobs[:10]:
            title = job.get("position", "Unknown Position")
            company = job.get("company", "Unknown Company")
            location = job.get("location", "Remote")
            job_url = f"https://remoteok.io{job.get('url', '#')}"

            writer.writerow([title, company, location, job_url])

    print(f" Job listings saved to {csv_filename}")

else:
    print(f"Failed to retrieve jobs. Status Code: {response.status_code}")


# What This Script Does:
#
# 1. Sends a GET request to RemoteOK's API to fetch job listings.
# 2. Extracts job details such as:
#    - Job Title
#    - Company Name
#    - Job Location
#    - Application Link
# 3. Saves the first 10 job listings into a CSV file (`remoteok_jobs.csv`).
# 4. Uses a `User-Agent` header to avoid request blocking.
# 5. If the request fails, it prints an error message with the HTTP status code.
#
# This script is useful for anyone looking to automate job data collection from RemoteOK!


