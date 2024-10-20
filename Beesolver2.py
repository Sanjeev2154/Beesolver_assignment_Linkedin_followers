import pandas as pd
import requests
import json
import time
import random


def GetFollowers(url, out_file, slug):
    """
    Fetches the follower count of a LinkedIn profile and writes the data to a JSON file.

    This function sends a request to the LinkedIn API using specified cookies and headers
    to retrieve the follower count of a user identified by their unique member identity.
    It writes the follower count along with the profile URL to the specified output file in JSON format.

    Parameters:
    url (list): A list containing the LinkedIn profile URL.
    out_file (file object): The output file where the follower count will be written in JSON format.
    u (str): The unique member identity extracted from the LinkedIn profile URL.

    Returns:
    None: This function writes the follower count and URL to the output file but does not return any value.

    Exceptions:
    Catches any exceptions that occur during the API request and prints the profile URL
    being processed along with the error message.
    """
    try:
        cookies = {
            'li_rm': 'AQEuI28TNSvmbwAAAZKZTOV_P1j-ZiUayRXORhUACM6KFL7Kp_aD-Q5KMmwZZE1g7XlKjZjIWZbAGTc6vhzXTt7vVbxWdwPL-lFOoiwuJx9j4No6525yOGK1',
            'bcookie': '"v=2&0a648ace-8389-480f-8f18-d923949e7cf3"',
            'bscookie': '"v=1&20241017070646d6daacef-b088-40e5-82c6-d23e3716fb1cAQG0s3-Sk0gmMtit72Qka3DrCK7WS021"',
            'aam_uuid': '36635696476321415932286236830725046319',
            'timezone': 'Asia/Calcutta',
            'li_theme': 'light',
            'li_theme_set': 'app',
            'dfpfpt': 'e10b7e9dfd4a4a159db46da4c0ccd6cb',
            'li_sugr': 'df0eadac-e4c8-4bea-b1b7-2ae6cc1069f3',
            '_guid': '7ff0d4cd-d795-4a53-8f8e-7b88bb1da47d',
            'AnalyticsSyncHistory': 'AQJKGFNqY8bz8gAAAZKZTZAZO4GIx-iChAzbFC_cwtIairEglAcoHkvr4luP9smqvJK4SypdY5jzpvT-Dvylag',
            'lms_ads': 'AQErO3VW_5LwJwAAAZKZTZFRQGwIWdb9Cl6ntqivNhgqcj5uvMuIo1F7ntxH7kWTdia6Tz9U4hIDb4fJR3zVqszT0cfO58J7',
            'lms_analytics': 'AQErO3VW_5LwJwAAAZKZTZFRQGwIWdb9Cl6ntqivNhgqcj5uvMuIo1F7ntxH7kWTdia6Tz9U4hIDb4fJR3zVqszT0cfO58J7',
            'visit': 'v=1&M',
            'g_state': '{"i_l":0}',
            'fcookie': 'AQHatNE6X6bJfAAAAZKdx59wIg8eEejPshcYRxTTvTkWsKFxk9DfPjlysnYIyY37vUyTPVyW8EvXHKb99Rf7FoSs1sGv4aPKYc3qBGEupz6VVC1OdickAP1Wmp2ZtMOni4dM7U9ABSHgPEBJ36YeL18iEm-1U5JyhJn7VUpS1g0N8nJJ6eHh_rQRT4OpHo1EN-lMdV1EMoQh4ZWnNeX-Q5vyeI9rIUZaMZMrziuV6uLSlQdRgJbzdCVJNFfQc_JGpNgnPBIaMRiH-EsQ04itqLHb45H1tzItB7drmEALjc8nMBnYf8CUt+lNlFlSwNR4SSkPvqJwWLfTvgI8g+mr6O6cmBg/R1fjFVZJbKFLLRKDVB/83422gA==',
            'fid': 'AQEuQycpuAhJ3gAAAZKdx6K8AZS0YqkAXx9FhGoB8quemL0zKZChsJwbsUkjif6RB1VqH8iB3JAdjA',
            '_gcl_au': '1.1.977150871.1729148815.601689132.1729259165.1729259165',
            'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
            'fptctx2': 'taBcrIH61PuCVH7eNCyH0FC0izOzUpX5wN2Z%252b5egc%252f4ApR0Od6eH3r0jo7%252fEZPy8HDF5nK7ijgHk5theJH5CpXSFMStnJahVhWU%252bMgKvWhiGdYXglR8GUBw21%252beXxkV%252fCXR5VJsGgJGtgZH%252fLLXru9x%252bdkpnOAcw2YbQyU0HqYS0xCDNANrkWdOs47jMjmUvuDUPjlbHalvYv%252fQqlUNnmSqr%252fObSmJQAG8hWeK7F75yjExZsXOSfei5x%252fGN5SJtjeANNw%252fJtt32gH0UPQS%252fQqOMUG4vYMEnJE6tZ05G9ZPJkbX4%252bWdQpOBZqdnRwf5Nh7Qk6RiTOWEwwLvABSHbXBXYveWqm6OddCZfmUS6au%252bM%253d',
            'li_g_recent_logout': 'v=1&true',
            'lang': 'v=2&lang=en-us',
            'liap': 'true',
            'li_at': 'AQEDAVPvloQFxJHFAAABkqRH_S8AAAGSyFSBL00AzK93njr7G1DfnnvGSnL-FxsVh9mdy5FdYQdq1RELrYR1qxqPX22r4w0kHf2WlBEu5NFpnjAtG46-0PDFjqkqepJU7oVptUr4F4HLGIVNQZG0d4hU',
            'JSESSIONID': '"ajax:8855592180555482446"',
            'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C20016%7CMCMID%7C36098308986617689142266849329349850084%7CMCAAMLH-1729937842%7C12%7CMCAAMB-1729937842%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1729340242s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1826105269',
            'UserMatchHistory': 'AQLPWp05Zd8X3wAAAZKkS-M9iBmR2miyIfGP_3ry9uGChzpNvCpt_KtIxJo-9R-nOe8j1Z-fYGem2ou9bnfzCjB6dlP-BI-FGE8a6O4wrpqoPVFqjvlw0tVRXLzO5spvL_h8apXx24N2msiE3GOzNpkeSZsYSnoFe4tyZaJIiFS7x-V9dwvzSSuEbAgDyk9Scse0HUrxOywaKfAJTsWMJtGoiWBbAHPwBC5sKMBhEybQTQRbsxIKRejXe-auSo25D7i3JjMjRdcJj9bBchSwbt1SN5-V_nwnAnCXan9CbBBOLjHhBsedvDd9OZEJPSL1Yd6tNtkMdrgdGku8NPUsezW--HMNJoS5uItEBe-yXMdUrfZlGQ',
            'lidc': '"b=TB64:s=T:r=T:a=T:p=T:g=3607:u=1:x=1:i=1729333292:t=1729419434:v=2:sig=AQER1SeNeKDA_qZnBcMeFASJsZKmIZB7"',
        }

        headers = {
            'accept': 'application/vnd.linkedin.normalized+json+2.1',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            # 'cookie': 'li_rm=AQEuI28TNSvmbwAAAZKZTOV_P1j-ZiUayRXORhUACM6KFL7Kp_aD-Q5KMmwZZE1g7XlKjZjIWZbAGTc6vhzXTt7vVbxWdwPL-lFOoiwuJx9j4No6525yOGK1; bcookie="v=2&0a648ace-8389-480f-8f18-d923949e7cf3"; bscookie="v=1&20241017070646d6daacef-b088-40e5-82c6-d23e3716fb1cAQG0s3-Sk0gmMtit72Qka3DrCK7WS021"; aam_uuid=36635696476321415932286236830725046319; timezone=Asia/Calcutta; li_theme=light; li_theme_set=app; dfpfpt=e10b7e9dfd4a4a159db46da4c0ccd6cb; li_sugr=df0eadac-e4c8-4bea-b1b7-2ae6cc1069f3; _guid=7ff0d4cd-d795-4a53-8f8e-7b88bb1da47d; AnalyticsSyncHistory=AQJKGFNqY8bz8gAAAZKZTZAZO4GIx-iChAzbFC_cwtIairEglAcoHkvr4luP9smqvJK4SypdY5jzpvT-Dvylag; lms_ads=AQErO3VW_5LwJwAAAZKZTZFRQGwIWdb9Cl6ntqivNhgqcj5uvMuIo1F7ntxH7kWTdia6Tz9U4hIDb4fJR3zVqszT0cfO58J7; lms_analytics=AQErO3VW_5LwJwAAAZKZTZFRQGwIWdb9Cl6ntqivNhgqcj5uvMuIo1F7ntxH7kWTdia6Tz9U4hIDb4fJR3zVqszT0cfO58J7; visit=v=1&M; g_state={"i_l":0}; fcookie=AQHatNE6X6bJfAAAAZKdx59wIg8eEejPshcYRxTTvTkWsKFxk9DfPjlysnYIyY37vUyTPVyW8EvXHKb99Rf7FoSs1sGv4aPKYc3qBGEupz6VVC1OdickAP1Wmp2ZtMOni4dM7U9ABSHgPEBJ36YeL18iEm-1U5JyhJn7VUpS1g0N8nJJ6eHh_rQRT4OpHo1EN-lMdV1EMoQh4ZWnNeX-Q5vyeI9rIUZaMZMrziuV6uLSlQdRgJbzdCVJNFfQc_JGpNgnPBIaMRiH-EsQ04itqLHb45H1tzItB7drmEALjc8nMBnYf8CUt+lNlFlSwNR4SSkPvqJwWLfTvgI8g+mr6O6cmBg/R1fjFVZJbKFLLRKDVB/83422gA==; fid=AQEuQycpuAhJ3gAAAZKdx6K8AZS0YqkAXx9FhGoB8quemL0zKZChsJwbsUkjif6RB1VqH8iB3JAdjA; _gcl_au=1.1.977150871.1729148815.601689132.1729259165.1729259165; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; fptctx2=taBcrIH61PuCVH7eNCyH0FC0izOzUpX5wN2Z%252b5egc%252f4ApR0Od6eH3r0jo7%252fEZPy8HDF5nK7ijgHk5theJH5CpXSFMStnJahVhWU%252bMgKvWhiGdYXglR8GUBw21%252beXxkV%252fCXR5VJsGgJGtgZH%252fLLXru9x%252bdkpnOAcw2YbQyU0HqYS0xCDNANrkWdOs47jMjmUvuDUPjlbHalvYv%252fQqlUNnmSqr%252fObSmJQAG8hWeK7F75yjExZsXOSfei5x%252fGN5SJtjeANNw%252fJtt32gH0UPQS%252fQqOMUG4vYMEnJE6tZ05G9ZPJkbX4%252bWdQpOBZqdnRwf5Nh7Qk6RiTOWEwwLvABSHbXBXYveWqm6OddCZfmUS6au%252bM%253d; li_g_recent_logout=v=1&true; lang=v=2&lang=en-us; liap=true; li_at=AQEDAVPvloQFxJHFAAABkqRH_S8AAAGSyFSBL00AzK93njr7G1DfnnvGSnL-FxsVh9mdy5FdYQdq1RELrYR1qxqPX22r4w0kHf2WlBEu5NFpnjAtG46-0PDFjqkqepJU7oVptUr4F4HLGIVNQZG0d4hU; JSESSIONID="ajax:8855592180555482446"; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20016%7CMCMID%7C36098308986617689142266849329349850084%7CMCAAMLH-1729937842%7C12%7CMCAAMB-1729937842%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1729340242s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1826105269; UserMatchHistory=AQLPWp05Zd8X3wAAAZKkS-M9iBmR2miyIfGP_3ry9uGChzpNvCpt_KtIxJo-9R-nOe8j1Z-fYGem2ou9bnfzCjB6dlP-BI-FGE8a6O4wrpqoPVFqjvlw0tVRXLzO5spvL_h8apXx24N2msiE3GOzNpkeSZsYSnoFe4tyZaJIiFS7x-V9dwvzSSuEbAgDyk9Scse0HUrxOywaKfAJTsWMJtGoiWBbAHPwBC5sKMBhEybQTQRbsxIKRejXe-auSo25D7i3JjMjRdcJj9bBchSwbt1SN5-V_nwnAnCXan9CbBBOLjHhBsedvDd9OZEJPSL1Yd6tNtkMdrgdGku8NPUsezW--HMNJoS5uItEBe-yXMdUrfZlGQ; lidc="b=TB64:s=T:r=T:a=T:p=T:g=3607:u=1:x=1:i=1729333292:t=1729419434:v=2:sig=AQER1SeNeKDA_qZnBcMeFASJsZKmIZB7"',
            'csrf-token': 'ajax:8855592180555482446',
            'priority': 'u=1, i',
            'referer': 'https://www.linkedin.com/in/dimitrios-papis-447aa02b/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-li-lang': 'en_US',
            'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base_recent_activity_content_view;J3soPRCmSkGQZGtSYVGTgA==',
            'x-li-track': '{"clientVersion":"1.13.25033","mpVersion":"1.13.25033","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Calcutta","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1366,"displayHeight":768}',
            'x-restli-protocol-version': '2.0.0',
        }

        response = requests.get(
            'https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(memberIdentity:{})&queryId=voyagerIdentityDashProfiles.59c1e4246cab388d8dd276192b87d6ef'.format(
                slug),
            cookies=cookies,
            headers=headers,
        )
        if response.status_code == 200:
            jd = response.json()
            if jd.get('included'):
                followers = jd.get('included', [{}])[0].get('followerCount', '')
                out_file.write(json.dumps(dict(followers=followers, url=url[0])) + '\n')
                # print(followers)
                # print(url[0])
            else:
                out_file.write(json.dumps(dict(followers='Not Available', url=url[0])) + '\n')
        else:
            print(url[0])
    except Exception as e:
        print(url[0])
        print(str(e))


# Open output file
out_file = open('followersfile.json', 'w')

# Load URLs from CSV file
urls = pd.read_csv(r'file:///C:\Users\lenovo\Downloads\follower%20scraped%20-%20Sheet1.csv').values.tolist()

for url in urls:
    time.sleep(random.randint(5, 8))  # Random sleep to avoid rate limiting
    slug = url[0].split('/')[-1]  # Here, finding to change in the response to work dynamically for each url

    GetFollowers(url, out_file, slug)

# Close the output file
out_file.close()
