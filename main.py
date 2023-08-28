import json

import requests

url = "https://jobsapi-internal.m-cloud.io/api/job"
limit = 50


def processOffset(offset):
    print(f"Processing offset: {offset}")
    params = {
        "callback": "jobsCallback",
        "offset": offset,
        "sortfield": "open_date",
        "sortorder": "descending",
        "Limit": limit,
        "Organization": "2110",
        "useBooleanKeywordSearch": "true"
    }
    response = requests.get(url, params=params)
    parsedJson = json.loads(response.text.replace("jobsCallback(", "")[:-1])
    for result in parsedJson['queryResult']:
        data = {
            "id": result['id'],
            "function": result['function'],
            "title": result['title'],
            "primary_city": result['primary_city'],
            "primary_state": result['primary_state'],
            "primary_zip": result['primary_zip'],
            "primary_country": result['primary_country'],
            "primary_category": result['primary_category'],
            "job_type": result['job_type'],
            "store_id": result['store_id'],
            "employment_type": result['employment_type'],
            "parent_category": result['parent_category'],
            "department": result['department'],
            "level": result['level'],
        }
        print(data['id'])


def main():
    params = {
        "callback": "jobsCallback",
        "offset": "100",
        "sortfield": "open_date",
        "sortorder": "descending",
        "Limit": limit,
        "Organization": "2110",
        "useBooleanKeywordSearch": "true"
    }
    response = requests.get(url, params=params)
    parsedJson = json.loads(response.text.replace("jobsCallback(", "")[:-1])
    # print(json.dumps(parsedJson,indent=4))
    totalHits = parsedJson['totalHits']
    for i in range(0, totalHits, limit):
        processOffset(i)


if __name__ == '__main__':
    main()
    # processOffset(10)
