import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            print(f'The application at {url} is UP and running.')
            return True
        else:
            print(f'The application at {url} is DOWN. HTTP Status Code: {response.status_code}')
            return False
    except requests.ConnectionError:
        print(f'The application at {url} is DOWN. Connection Error.')
        return False

# Example usage:
application_url = 'https://example.com'
check_application_health(application_url)
