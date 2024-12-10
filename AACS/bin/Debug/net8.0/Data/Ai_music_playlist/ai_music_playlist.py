from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import numpy as np

client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def generate_playlist(seed_track_uri, num_tracks=10):
  track = sp.track(seed_track_uri)
  audio_features = sp.audio_features(seed_track_uri)[0]
  playlist_tracks = [seed_track_uri]
  for _ in range(num_tracks - 1):
    recommendations = sp.recommendations(
      seed_tracks=[seed_track_uri],
      limit=100,
      market='US',
      min_energy=audio_features['energy'] * 0.8,
      min_danceability=audio_features['danceability'] * 0.8,
      # Add other features as needed
    )
    recommended_tracks = [track['uri'] for track in recommendations['tracks']]
    playlist_tracks.append(np.random.choice(recommended_tracks))
  return playlist_tracks

# Example usage
seed_track_uri = 'spotify:track:YOUR_SEED_TRACK_URI'
playlist_tracks = generate_playlist(seed_track_uri)
print(playlist_tracks)