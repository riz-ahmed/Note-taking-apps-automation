
from notion.client import NotionClient

client = NotionClient(token_v2="d6b9ab703230d18cc35e17646c5167b6974175dae576309ddf026f9cb11e0271ca9b12ed3c1444ea98a842ae24c9e65972d2868d66862a050efe97c846bcdc90063c646b955eebcc70bb9b318f5f")

# url of the page to be edited
list_url = "https://www.notion.so/rizahmed/CODE-b113f8f889f0488b87be6201b3a93cd8"
page = client.get_block(list_url)