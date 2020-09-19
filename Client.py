from Helpers.UrlFormatter import UrlFormatter
import http.client

class Client:

    @staticmethod
    def close_connection(connection):
        connection.close()

    @staticmethod
    def make_connection(domain):
        return  http.client.HTTPSConnection(domain)

    def get(self, url):
        httpsless_url = UrlFormatter.remove_https_from_url(url)
        domain = UrlFormatter.get_domain_from_url(httpsless_url)
        path = UrlFormatter.get_path_from_url(httpsless_url)

        connection = Client.make_connection(domain)

        connection.request("GET", path)
        response = connection.getresponse()

        print("Status: {} and reason: {}".format(response.status, response.reason))

        Client.close_connection(connection)
