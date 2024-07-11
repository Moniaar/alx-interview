#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.error('Usage: node 0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Failed to retrieve movie:', response.statusCode);
        return;
    }

    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    characterUrls.forEach((url) => {
        request(url, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error:', charError);
                return;
            }

            if (charResponse.statusCode !== 200) {
                console.error('Failed to retrieve character:', charResponse.statusCode);
                return;
            }

            const character = JSON.parse(charBody);
            console.log(character.name);
        });
    });
});
