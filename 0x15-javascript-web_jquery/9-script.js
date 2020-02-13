$(function () {
  let HelloINFrog = "https://fourtonfish.com/hellosalut/?lang=fr";
  $.ajax({
    type: 'GET',
    url: HelloINFrog,
    success: function (names) {
      $('div#hello').text(names['hello']);
      console.log('Success', names);
    }
  })
});
