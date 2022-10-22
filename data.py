from setup import *

# method to extract ip address [list] from json data received via jira ticket issue
def extractIpAddress(data):
    regex_pattern = "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    # print("Ip adress list: ", re.findall(regex_pattern, data))
    return re.findall(regex_pattern, data)

# get data we need from related Jira ticket issue
def extractFromJira(url):
    response = requests.get(
        url,
        headers=headers,
        auth=(username,password),
        verify=False
    )
    # If any ticket doesn't exist in given ID range
    if response.status_code != 404:
        data = response.json()
        ticketId = data["key"]
        summary = data["fields"]["summary"]
        desc = data["fields"]["description"]
        # print(ticketId, "\n" ,summary, "\n", desc)
        return ticketId,summary,desc
    else:
        pass

#Asset id search by ip address in Nexpose
def findAssetId(x):
    search_data = {
        "match": "all",
        "filters": [
            {
                "field":"ip-address",
                "operator":"is",
                "value": x
            }
        ]
    }
    assetUrl = '{}/assets/search'.format(nexpose)

    response = requests.post(
        assetUrl,
        headers = headers,
        auth=(username,password),
        verify=False,
        json=search_data
    )

    if response.status_code == 200 or response.status_code == 201:
        search_data = response.json()
        search_data = search_data["resources"]
        print(search_data[0]["id"])
    else:
        print(x, " is not found. Not successfull")
        pass

