#!/usr/bin/env python3

print('Please input your favorite genres')
genres = []
genre = ''
# Accept user inputs for their favorite genre
while genre != 'stop':
    genre = input('type stop to stop')
    if genre == 'stop':
        pass
    else:
        genres.append(genre)

# print the genres.

for genre in genres:
    print(genre)
    