from Model import Model


class Track(Model):
    # tracks = []
    #
    # def __init__(self, tid, gid):
    #     self.tid = tid  # track id
    #     self.gid = gid  # genre id ??
    #     self.playlist = []
    #
    # @classmethod
    # def createTrack(cls):
    #     count = len(cls.tracks)
    #     t = Track(count, -1)
    #     cls.tracks.append(t)
    #     return t

    def added_to_playlist(self, p):
        self.contains.append(p)

    def number_of_appearance(self):
        return len(self.contains)