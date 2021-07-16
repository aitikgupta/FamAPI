class FamVideo:
    """Schema for each fetched/saved video"""

    def __init__(
        self,
        id,
        title,
        description,
        published_at,
        thumbnail_defaultres,
        thumbnail_highres,
    ):
        # force `videoId` from YouTube API
        # instead of MongoDB's default _id
        self._id = id
        self.title = title
        self.description = description
        self.published_at = published_at
        self.thumbnail_defaultres = thumbnail_defaultres
        self.thumbnail_highres = thumbnail_highres
