from bs4 import BeautifulSoup
from flask import Flask, request, render_template
import requests
import re
application = Flask(__name__) 

@application.route("/check_usernames", methods=["GET", "POST"]) 


def check_username():
    if request.method == "POST":
        usernames = request.form.get("usernames")

        usernames_list = re.split(r'[,\s]+', usernames.strip())

        # Here you would check the username's availability For example, you can call your existing username checking function or 
        # API Assuming you have a function called check_username_availability
        availability_info = []
        for username in usernames_list[:50]:
            info = show_google_content(username)

            if info:
                availability_info.append(info)
                print('--------')
                print(availability_info)

        return render_template("result.html", results=availability_info)

    return render_template("form.html")


def show_google_content(username):
    try:
        # Make a GET request to Google
        response = requests.get('https://fragment.com/username/' + str(username))
        # Check if the request was successful
        if response.status_code == 200:

             soup = BeautifulSoup(response.content, "html.parser")

             paragraphs = soup.find_all("span","subdomain")[0].text
             print(paragraphs)

             status_element = soup.find('span', class_='tm-section-header-status tm-status-unavail')
             status_element_auc = soup.find('span', class_='tm-section-header-status tm-status-avail')
             status_element_taken = soup.find('span', class_='tm-section-header-status tm-status-taken')
             status_element_available = soup.find('span', class_='tm-section-header-status tm-status-avail')

             if status_element and status_element.text.strip() == 'Sold':
                 print("The item is sold.")
                 status='Sold'
             elif status_element_auc and status_element_auc.text.strip() == 'On auction':
                 status='On auction'
             elif status_element_taken and status_element_taken.text.strip() == 'Taken':
                 status='Already taken'
    #            print('already taken')
             elif status_element_auc and status_element_auc.text.strip() == 'For sale':
                 status='For sale'
             elif status_element_available and status_element_auc.text.strip() == 'Available':
                 status='Mint'
             else:
                 status='Unknown'
                 print("The item is not sold or the status element does not exist.")


             if status=='Sold':
                 elements = soup.find_all("table","table tm-table tm-table-fixed")
                 username = soup.find_all("span","subdomain")[0].text

                 if elements:
                     columns = elements[1].find_all('td')  # This retrieves all <td> tags

                     for column in columns:
                         print('1: '+ column.text.strip())  # Print the text content of each <td>
                         if (column.text.strip()=='Unavailable'):
                             print('yeap, unavailable')

                 price = columns[0].text.strip()
                 if columns[0].text.strip()=='Show more':
                     price = columns[1].text.strip()

                 return {
                        'username': username,
                        'result': price,
                        'availability': 'Sold'
                 } 

             elif status=='Already taken':
                    username = soup.find_all("span","subdomain")[0].text

                    return {
                        'username': username,
                        'result': '--',
                        'availability': 'Already taken'
                    }

             elif status=='On auction':
                 elements = soup.find_all("table","table tm-table tm-table-fixed")
                 username = soup.find_all("span","subdomain")[0].text
                 if elements:
                     columns = elements[1].find_all('td')  # This retrieves all <td> tags

                 return {
                        'username': username,
                        'result': columns[0].text.strip(),
                        'data_end': columns[1].text.strip(),
                        'availability': 'On auction'
                }

             elif status=='Mint':
                 elements = soup.find_all("table","table tm-table tm-table-fixed")
                 username = soup.find_all("span","subdomain")[0].text
                 price = soup.find_all("div","table-cell-value tm-value icon-before icon-ton")[0].text

                 with open('usernames.txt', 'a') as f:
                     f.write(str(username) + ' ' + 'Mint' + ' ' + str(price) +'\n')
                 return {
                        'username': username,
                        'result': price,
                        'availability': 'Available for mint'
                 }

             elif status=='For sale':
                 elements = soup.find_all("span","icon-before icon-ton tm-amount")
 
                 username = soup.find_all("span","subdomain")[0].text

                 if elements:
                     print(elements[0].text)
                 with open('usernames.txt', 'a') as f:
                     f.write(str(username) + ' ' + 'Sale' + ' ' + str(elements[0].text) +'\n')
                 return {
                        'username': username,
                        'result': elements[0].text,
                        'availability': 'For Sale'
                }

             else:
                elements = soup.find_all("table","table tm-table tm-table-fixed")
                username = soup.find_all("span","subdomain")[0].text
                print(username)
                if elements:
                    columns = elements[0].find_all('td') 
                    print(columns)
                     # This retrieves all <td> tags
                    # Print the text of each <td> found
    #                print(len(columns))

                    for column in columns:
                        print('1: '+ column.text.strip())  # Print the text content of each <td>
                        if (column.text.strip()=='Unavailable'):
                            print('yeap, unavailable')

                            with open('usernames.txt', 'a') as f:
                                f.write(str(username) + ' ' + 'Available' +'\n')  # Write each username on a 

                            return {
                                    'username': username,
                                    'result': '--',
                                    'availability': 'Available to register'
                            }








             return status

# Return the HTML content of the page
        # Example: Extract all paragraph texts
        





        else:
            return f"Error fetching content: {response.status_code}", response.status_code
    except Exception as e:
        return f"An error occurred: {str(e)}", 500







if __name__ == "__main__":
   application.run(host='0.0.0.0')
