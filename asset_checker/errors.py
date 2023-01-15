class InvalidAPICallError(Exception):

    def __str__(self, status_code):
        return "Connection to the API could not be made: status code {}".format(status_code)
