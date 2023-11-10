

def download_repository_zip(access_token: str):
    """
    curl -X GET -H 'Authorization: token {ここにPersonal Access Token}' 'https://api.github.com/search/repositories?q=language:C&stars:50000..*&sort=stars&order=desc'
    """
    url = "https://api.github.com/search/repositories?q=language:C&stars:50000..*&sort=stars&order=desc"
    

