#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const swapiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(swapiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to fetch character names and print them
  const printCharacters = (characterUrls, index = 0) => {
    if (index >= characterUrls.length) {
      return;
    }

    const characterUrl = characterUrls[index];
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Fetch next character
      printCharacters(characterUrls, index + 1);
    });
  };

  // Start fetching and printing character names
  printCharacters(characters);
});
