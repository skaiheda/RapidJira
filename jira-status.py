from setup import *

# ticket status id
# 21 = in progress
# 41 = done
# 61 = open
# 81 = pending
# 91 = rejected

url='https://jira-support.kapitalbank.az/rest/api/2/issue/NEX-3481/transitions'
status_data = { "transition":
    {
        "id": "61"
    }
}

response = requests.post(
    url,
    headers=headers,
    json=status_data,
    auth=(username,password),
    verify=False
    )

# if response.status_code != 200:
print(response.status_code)
