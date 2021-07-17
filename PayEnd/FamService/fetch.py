from FamBase.controller import search_videos


class VideosFetcher:
    def __init__(self):
        pass

    @staticmethod
    def fetch_videos(query, page):
        results = search_videos(query, page)

        response = {
            "query": query,
            "page": page,
            "results": []
        }
        for fam_video in results:
            response["results"].append(fam_video)

        return response
