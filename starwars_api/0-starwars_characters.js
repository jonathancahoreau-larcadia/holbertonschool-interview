#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
if (!movieId) process.exit(1);

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

function getJSON(url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true, strictSSL: false }, (err, res, body) => {
      if (err) return reject(err);
      if (res.statusCode !== 200)
        return reject(new Error(`Status ${res.statusCode}`));
      resolve(body);
    });
  });
}

getJSON(filmUrl)
  .then((film) => {
    const chars = film.characters || [];
    return Promise.all(chars.map((url) => getJSON(url)));
  })
  .then((charObjs) => {
    charObjs.forEach((c) => console.log(c.name));
  })
  .catch((err) => console.error(err));
