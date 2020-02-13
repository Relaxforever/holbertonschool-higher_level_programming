$(function () {
  let starwarsApi = "https://swapi.co/api/people/5/?format=json";
  $.ajax({
    type: 'GET',
    url: starwarsApi,
    success: function (names) {
      $('div#character').text(names['name']);
      console.log('Success', names);
    }
  })
});
