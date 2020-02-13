$(function () {
  let starwarsApi = "https://swapi.co/api/films/?format=json";
  $.ajax({
    type: 'GET',
    url: starwarsApi,
    success: function (titles) {
      let titlesDict = titles.results;
      for (let cont = 0; cont < titlesDict[cont].title; cont++) {
        console.log('success', titlesDict.results[cont].title);
        $('ul#list_movies').append('<li>' + titlesDict[cont].title + '</li>');
      }
    }
  })
});
