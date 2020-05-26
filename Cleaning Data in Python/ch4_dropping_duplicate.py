# Create a new DataFrame called tracks that contains the following columns from billboard: 'year', 'artist', 'track', and 'time'.
# Print the info of tracks. This has been done for you.
# Drop duplicate rows from tracks using the .drop_duplicates() method. Save the result to tracks_no_duplicates.
# Print the info of tracks_no_duplicates. This has been done for you, so hit 'Submit Answer' to see the results!

# Create the new DataFrame: tracks
tracks = billboard[['year','artist','track','time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())
