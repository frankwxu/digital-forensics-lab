"""
Explanation of the Code
Listing Package IDs :
- The script uses os.listdir() to list all directories in the Pixel 3/data/data folder. Each directory corresponds to an installed app's package ID.
Fetching App Details :
- For each package ID, the script constructs the Google Play Store URL (https://play.google.com/store/apps/details?id=<package>).
- It uses the requests library to fetch the HTML content of the app's details page.
Parsing the HTML :
- The script uses BeautifulSoup from the bs4 module to parse the HTML response.
- It looks for the <h1> tag with the attribute itemprop="name" to extract the app name.
Output :
- The script prints the app name and its corresponding package ID.
"""
import os
import requests
import re
def get_android_apps():
    # Path to the directory containing package IDs
    data_dir = "Pixel 3/data/data"
    # List all package IDs (directories) in the specified path
    try:
        packages = [name for name in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, name))]
    except FileNotFoundError:
        print(f"Directory '{data_dir}' not found.")
        return
    # Base URL for Google Play Store app details
    base_url = "https://play.google.com/store/apps/details?id="
    for package in packages:
        try:
            # Fetch the app details page
            url = base_url + package
            print(url)
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to fetch details for package: {package}")
                continue
            # Extract the app name using a regular expression
            # print(response.text)
            match = re.search(r'itemprop="name">(.*?)</span>', response.text)
            app_name = match.group(1) if match else "Unknown"
            # Print the app name and package ID
            print(f"App Name: {app_name}, Package ID: {package}")
        except Exception as e:
            print(f"Error processing package {package}: {str(e)}")

if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    get_android_apps()