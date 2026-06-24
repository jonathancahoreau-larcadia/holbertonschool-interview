#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) process.exit(1);

const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function getJSON (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true, strictSSL: false }, (error, response, body) => {
      if (error) return reject(error);

      if (response.statusCode !== 200) {
        return reject(new Error(`Status ${response.statusCode}`));
      }

      resolve(body);
    });
  });
}

getJSON(filmUrl)
  .then(film => {
    const characters = film.characters || [];
    return Promise.all(characters.map(url => getJSON(url)));
  })
  .then(characterObjects => {
    characterObjects.forEach(character => console.log(character.name));
  })
  .catch(error => console.error(error));
