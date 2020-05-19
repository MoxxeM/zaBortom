class Api:
    @staticmethod
    def get_current_name(query, request):
        pass

    @staticmethod
    def get_create_room(query, request):
        pass

    # more functions

    queries = {
        'current-name': get_current_name,
        'create-room': get_create_room,
    }

    @staticmethod
    def query_is_valid(query):
        return Api.queries.get(query) is not None

    @staticmethod
    def get_data(query, request):
        if Api.query_is_valid(query):
            return Api.queries.get(query)(query, request)
