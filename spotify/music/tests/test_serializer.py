from django.test import TestCase
from music.models import Artist, Album
from music.serializers import ArtistSerializer, SongSerializer


class TestArtistSerializer(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="Example Artist")
        self.artist2 = Artist.objects.create(name="Example Artist2")

    def test_data(self):
        data = ArtistSerializer(self.artist).data
        assert data['id'] is not None
        assert data['name'] == "Example Artist"
        assert data['picture'] == ""


class TestSongSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Test Artist")
        self.album = Album.objects.create(artist=self.artist, title="Test Album")

    def test_is_valid(self):
        data = {
            'title': 'Test Song',
            'album': self.album.id,
            'cover': '',
            'source': 'http://example.com//music.mp3',
            'listened': 0
        }
        serializer = SongSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_is_not_valid(self):
        data = {
            'title': 'Test Song',
            'album': self.album.id,
            'cover': '',
            'source': 'http://example.com//music',
            'listened': 0
        }

        serializer = SongSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEquals(str(serializer.errors['source'][0]), 'Mp3 file is required')
