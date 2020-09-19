class UrlFormatter:

    @staticmethod
    def remove_https_from_url(url):
        return url.split("https://")[-1]

    @staticmethod
    def get_domain_from_url(url):
        return url.split("/")[0]

    @staticmethod
    def get_path_from_url(url):
        path = url.split("/")[1:]
        return "/".join(path)
