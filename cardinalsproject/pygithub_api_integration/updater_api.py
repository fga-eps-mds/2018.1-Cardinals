import aiohttp
import asyncio
import requests

base_address = 'http://updater:3000/'


def getRepoAndContributors(repo_name):
    url = base_address + 'repository/' + repo_name
    response = requests.get(url)
    response_data = response.json()
    
    repo = response_data["Repository"]
    contributors = response_data["Contributors"]

    return repo, contributors

async def _getRepoFromUpdater(repo_name):

    address = "http://updater:3000/request/?address=" + "https://github.com/" + repo_name
    print ("\n address \n")
    print (address)

    async with aiohttp.ClientSession(conn_timeout=30, read_timeout=35) as client:
        try:
            async with client.get(address) as response:
                content = await response.json()
                return content, response.status
        except Exception:
            pass


def getAsyncRepoId(repo_name):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task( _getRepoFromUpdater(repo_name) )
    loop.run_until_complete(task)

    result = task.result()
    repo_id = None

    print("\n Hi THERE !!\n")
    print (result)    

    if result is not None:

        content, status = task.result()

        print ("\n Status:")
        print (status)
        print ("\n")

        if status == 200:
            print(content)
            print(content['dbId'])
            repo_id = content['dbId']
    
    return repo_id